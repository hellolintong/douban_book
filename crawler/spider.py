#coding:utf8
#import sys
#sys.path.append('/home/lintong/Flask/github/')
import random
import requests
import urllib
import time
from bs4 import BeautifulSoup
from spider_config import SpiderConfig
#from log.crawler import spider_log


def get_request(url):
    ret = {
        'result': False,
        'r': None,
    }
    for i in xrange(3):
        try:
            length = random.randint(SpiderConfig.crawler_interval_min, SpiderConfig.crawler_interval_max)
            time.sleep(length)
            r = requests.get(url, timeout=30)
        except requests.exceptions.ConnectionError:
            continue
        except requests.exceptions.Timeout:
            continue
        ret['result'] = True
        ret['r'] = r
        break
    return ret


def crawler_tag(tag_id):
    if not isinstance(tag_id, unicode):
        tag_id = unicode(tag_id)
    index = 0
    tag = dict()
    tag['name'] = tag_id
    tag['book_list'] = []
    while True:
        url = "http://book.douban.com/tag/" + urllib.quote(tag_id.encode('utf-8')) + "?start=" + str(index) + "&type=T"
        url = unicode(url)
        index += 20
        if index > SpiderConfig.tag_filter:
            break
        ret_ = get_request(url)
        if not ret_['result']:
            return None
        soup = BeautifulSoup(ret_['r'].text)

        book_list = soup.find_all('li', class_='subject-item')
        if not book_list:
            break
        for book in book_list:
            tag['book_list'].append(int(book.find('div', class_='pic').find('a')['href'].split('/')[-2]))
    return tag


def fetch_number(string):
    result = list()
    if isinstance(string, unicode):
        string = string.encode('utf-8')
    for char in string:
        if char.isdigit() or char == '.':
            result.append(char)
    return ''.join(result)


def crawler_book(book_id):
    if not isinstance(book_id, unicode):
        book_id = unicode(book_id)
    url = u'http://book.douban.com/subject/' + book_id
    ret_ = get_request(url)
    if not ret_['result']:
        return None
    soup = BeautifulSoup(ret_['r'].text)

    book = {
        'score': 0.0,
        'score_num': 0,
        'img_url': u'',
        'book_id': 0,
        'name': u'',
        'introduce': u'',
        'author': u'',
        'public_date': u'',
        'page': 0,
        'price': 0.0,
        'ISBN': u'',
        'read_num': 0,
        'tag_list': [],
        'star_info': [0, 0, 0, 0, 0],
    }
    #获取评分信息
    score = soup.find('div', class_='rating_wrap')
    book['score'] = float(fetch_number(score.find('strong', class_='ll rating_num ', property='v:average').text))
    book['score_num'] = int(score.find('span', property='v:votes').text)
    #过滤评分太少的书籍
    if book['score'] < SpiderConfig.score_limit or book['score_num'] < SpiderConfig.score_number_limit:
        return None


    #获取书籍基本信息
    book['img_url'] = unicode(soup.find('a', class_='nbg').img['src'])
    book['book_id'] = int(book_id)
    book['name'] = unicode(soup.find('span', property='v:itemreviewed').string)
    introduce = soup.find('div', class_='intro')
    introduce = introduce.find_all('p')
    content = list()
    for elem in introduce:
        content.append(unicode(elem.string))
        content.append(u'<br/>')
    book['introduce'] = u''.join(content)

    info_list = soup.find('div', id='info')
    info_list = info_list.find_all('span', class_='pl')

    for elem in info_list:
        if elem.string == u' 作者':
            book['author'] = unicode(elem.next_sibling.next_sibling.string)
        elif elem.string == u'出版年:':
            book['public_date'] = unicode(elem.next_sibling.string)
        elif elem.string == u'页数:':
            book['page'] = int(fetch_number(elem.next_sibling.string))
        elif elem.string == u'定价:':
            book['price'] = float(fetch_number(elem.next_sibling.string))
        elif elem.string == u'ISBN:':
            book['ISBN'] = unicode(elem.next_sibling.string)

    #获取读书人数信息
    read_num_list = soup.find('div', id='collector').find_all('p', class_='pl')
    for read_num in read_num_list:
        book['read_num'] += int(fetch_number(read_num.find('a').string[0:-3]))

    #获取书签信息
    tag_info = list()
    tag_list = soup.find('div', id='db-tags-section').find('div', class_='indent').find_all('span')
    for tag in tag_list:
        if tag.find('a'):
            tag_info.append(unicode(tag.find('a').string))
    book['tag_list'] = tag_info

    #获取书单信息
    url = u"http://book.douban.com/subject/" + book_id + u"/doulists"
    ret_ = get_request(url)
    if ret_['result']:
        soup = BeautifulSoup(ret_['r'].text)
        paginator = soup.find('div', class_='paginator')
        book['book_list_num'] = int(fetch_number(paginator.find_all('a')[-2].text)) * 20
    if book['book_list_num'] < SpiderConfig.list_number_limit:
        return None

    #获取评论信息
    index = 0
    while True:
        url = u'http://book.douban.com/subject/' + book_id + u'/reviews?score=&start=' + unicode(index)
        index += 25
        ret_ = get_request(url)
        if not ret_['result']:
            break
        r = ret_['r']
        soup = BeautifulSoup(r.text)
        commend_list = soup.find_all('div', class_='ctsh')
        #所有页面都搜索完毕
        if not commend_list:
            break
        for commend in commend_list:
            commend = commend.find('div', class_='tlst')
            #判断用户是否已注销
            if commend.find('div', class_='ilst').find('a')['title'] == u'已注销':
                continue
            #判断评论是否为空
            commend_text = unicode(commend.find('div', class_='review-short').find('span').string)
            if not commend_text:
                continue
            try:
                score = commend.find('div', class_='clst').find('span', class_='ll user').find_all('span')[-1]['title']
            except Exception:
                #print "error"
                continue
            if score == u'力荐':
                book['star_info'][0] += 1
            elif score == u'推荐':
                book['star_info'][1] += 1
            elif score == u'还行':
                book['star_info'][2] += 1
            elif score == u'较差':
                book['star_info'][3] += 1
            elif score == u'很差':
                book['star_info'][4] += 1
            else:
               # print "error2"
                continue
    if (lambda star_info: star_info[0] + star_info[1] + star_info[2] + star_info[3] + star_info[3])(book['star_info']) < SpiderConfig.star_number_limit:
        return None
    return book
