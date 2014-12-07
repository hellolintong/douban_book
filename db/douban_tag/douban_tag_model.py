#coding=utf8
__author__ = 'lintong'
import mongoengine
from douban_tag_storage import DoubanTagStorage
from config import Config


mongoengine.connect(Config.DB_NAME, host=Config.DB_HOST, port=Config.DB_PORT)


##########user edit#############
def add_tag(**kwargs):
    tag = DoubanTagStorage()
    tag.name = kwargs['name']
    tag.book_list = kwargs['book_list']
    try:
        tag.save()
    except Exception:
        return None
    return tag


def update_tag(tag, **kwargs):
    if kwargs.get('name'):
        raise AttributeError("Can't update tag name")
    tag.update(**kwargs)


def delete_tag(tag):
    tag.delete()


def get_tag(**kwargs):
    return DoubanTagStorage.get(**kwargs)

def add_book(tag, book_id):
    if  book_id not in tag.book_list:
        tag.book_list.append(book_id)
        tag.save()

def add_book_list(tag, book_list):
    tag.book_list = book_list
    tag.save()
