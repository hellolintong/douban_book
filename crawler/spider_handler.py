#coding=utf8
import time
import random
#import traceback
#import pdb
from db.douban_book import douban_book_model
from db.douban_tag import douban_tag_model

from spider import crawler_tag
from spider import crawler_book

from cache import redis_handler
from log.crawler import crawler_log


def book_handler(book_redis_handler, tag_redis_handler):
    #pdb.set_trace()
    while book_redis_handler.queue_len():
        elem = book_redis_handler.pop_queue()
        book_id = elem.split(',')[0]
        search_tag_id = elem.split(',')[1]
        #有可能队列中会填入重复的书籍
        if book_redis_handler.check_set_member(book_id):
            continue
        book_id = unicode(book_id)
        try:
            book = crawler_book(book_id)
            if not book:
                #print book_id + ":fail"
                continue
        except Exception, e:
            #traceback.print_exc(file=open('dbg.txt', 'w+'))
            continue

        #反查book中是否包含tag
        if search_tag_id not in book['tag_list']:
            continue
        # 按照先后顺序添加一个标签到搜索队列，因为前面的标签更加靠谱
        tag_add_flag = False
        for tag in book['tag_list']:
            if not tag_redis_handler.check_set_member(tag):
                tag_redis_handler.push_queue(tag)
                book['tag_list'] = [search_tag_id]
                tag_add_flag = True
                break

        if tag_add_flag:
            try:
                douban_book_model.add_book(**book)
            except Exception, e:
                #traceback.print_exc(file=open('dbg.txt', 'w+'))
                continue
            #logger.info(traceback.print_exc())
            #print book_id + ":success"
            book_redis_handler.add_set_member(book_id)
            crawler_log.log_info(book['name'])


def tag_handler(tag_redis_handler, book_redis_handler):
    while tag_redis_handler.queue_len():
        tag_id = tag_redis_handler.pop_queue()
        if tag_redis_handler.check_set_member(tag_id):
            continue
        tag_redis_handler.add_set_member(tag_id)
        try:
            tag = crawler_tag(tag_id)
            if not tag:
                continue
        except Exception, e:
            #traceback.print_exc(file=open('dbg.txt', 'w+'))
            continue

        for book_id in tag['book_list']:
            if not book_redis_handler.check_set_member(book_id):
                book_redis_handler.push_queue(unicode(book_id) + u',' + unicode(tag_id))
            else:
                book = douban_book_model.get_book(book_id=book_id)
                if book:
                    douban_book_model.add_tag(book[0], tag_id)
        try:
            douban_tag_model.add_tag(**tag)
        except Exception, e:
            #traceback.print_exc(file=open('dbg.txt', 'w+'))
            pass


def handler(book_id, tag_id):
    books = douban_book_model.get_book()
    tags = douban_tag_model.get_tag()
    book_name_list = []
    for book in books:
        book_name_list.append(book.book_id)
    tag_name_list = []
    for tag in tags:
        tag_name_list.append(tag.name)
    book_redis_handler = redis_handler.get_book_redis_handler()
    book_redis_handler.batch_add_set_member(book_name_list)

    tag_redis_handler = redis_handler.get_tag_redis_handler()
    tag_redis_handler.batch_add_set_member(tag_name_list)

    book_redis_handler.push_queue(unicode(book_id) + u',' + unicode(tag_id))

    while True:
        length = random.randint(30, 60)
        book_handler(book_redis_handler, tag_redis_handler)
        tag_handler(tag_redis_handler, book_redis_handler)
        time.sleep(length)

if __name__ == "__main__":
    import pdb;pdb.set_trace()
    handler(2243615, u'\u8bbe\u8ba1\u6a21\u5f0f')
