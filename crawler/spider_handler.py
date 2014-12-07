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
        book_id = book_redis_handler.pop_queue()
        #有可能队列中会填入重复的书籍
        if book_redis_handler.check_set_member(book_id):
            continue
        try:
            book = crawler_book(book_id)
            if not book:
                #print book_id + ":fail"
                continue
        except Exception, e:
            #traceback.print_exc(file=open('dbg.txt', 'w+'))
            continue

        for tag in book['tag_list']:
            tag_list = douban_tag_model.get_tag(name=tag.name)
            if not tag_list:
                douban_tag_model.add_tag(name=tag.name, book_list=[book_id])
                tag_redis_handler.push_queue(tag.name)
            else:
                douban_tag_model.add_book(tag_list[0], book_id)

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
        try:
            tag = crawler_tag(tag_id)
            if not tag:
                continue
        except Exception, e:
            #traceback.print_exc(file=open('dbg.txt', 'w+'))
            continue

        for book_id in tag['book_list']:
            book_redis_handler.push_queue(book_id)
        try:
            douban_tag_model.add_tag(**tag)
        except Exception, e:
            #traceback.print_exc(file=open('dbg.txt', 'w+'))
            pass
        tag_redis_handler.add_set_member(tag_id)


def handler(book_id):
    books = douban_book_model.get_book()
    tags = douban_tag_model.get_tag()
    book_name_list = [book.book_id for book in books]
    tag_name_list = [tag.name for tag in tags if len(tag.book_list) == 1]

    book_redis_handler = redis_handler.get_book_redis_handler()
    book_redis_handler.batch_add_set_member(book_name_list)

    tag_redis_handler = redis_handler.get_tag_redis_handler()
    tag_redis_handler.batch_add_set_member(tag_name_list)

    book_redis_handler.push_queue(unicode(book_id))

    while True:
        length = random.randint(30, 60)
        book_handler(book_redis_handler, tag_redis_handler)
        tag_handler(tag_redis_handler, book_redis_handler)
        time.sleep(length)

if __name__ == "__main__":
    handler(2243615)
