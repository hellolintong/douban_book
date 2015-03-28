#coding:utf8
__author__ = 'lintong'

import mongoengine
from ..base import BaseMongoStorage
from config import Config

mongoengine.connect(Config.DB_NAME, host=Config.DB_HOST, port=Config.DB_PORT)


class UserStorage(BaseMongoStorage, mongoengine.Document):
    """Store user info
        name 用户名
        password 用户密码
        collect_tags(用户收藏的标签)
    """
    name = mongoengine.StringField(max_length=256, unique=True, required=True)
    password = mongoengine.StringField(max_length=256, required=True)
    collect_tags = mongoengine.ListField(mongoengine.StringField(max_length=256))
