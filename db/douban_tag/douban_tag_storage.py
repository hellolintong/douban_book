#coding:utf8
__author__ = 'lintong'

import mongoengine
from ..base import BaseMongoStorage
from config import Config

mongoengine.connect(Config.DB_NAME, host=Config.DB_HOST, port=Config.DB_PORT)


class DoubanTagStorage(BaseMongoStorage, mongoengine.Document):
    """Store user info
        name 标签名
        book_list 标签相关书籍列表
    """
    name = mongoengine.StringField(max_length=256, unique=True, required=True)
    book_list = mongoengine.ListField(mongoengine.IntField())