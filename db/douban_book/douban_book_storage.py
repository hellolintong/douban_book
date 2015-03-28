#coding:utf8
__author__ = 'lintong'

import mongoengine
from db.base import BaseMongoStorage
from config import Config

mongoengine.connect(Config.DB_NAME, host=Config.DB_HOST, port=Config.DB_PORT)


class DoubanBookStorage(BaseMongoStorage, mongoengine.Document):
    """Store book info
        #书籍的基本信息
        title: 书籍内容
        url: 书籍图片url
        book_id：书籍id
        author：作者
        public date：出版年份
        page：页数
        price：定价
        ISBN：ISBN号
        introduce：书籍简介
        #书籍评分信息
        score：评分
        score_num: 评分人数
        star_info: 具体评价
        read_num:读书人数
        book_list_num:书单数量
        relate_book_list: 关联的书籍
        #标签信息
        tag_list: 相关联的标签列表
    """
    img_url = mongoengine.StringField(max_length=100)
    title = mongoengine.StringField(max_length=100)
    book_id = mongoengine.IntField(unique=True, required=True)
    author = mongoengine.StringField(max_length=100)
    public_date = mongoengine.StringField(max_length=20)
    page = mongoengine.IntField()
    price = mongoengine.FloatField()
    ISBN = mongoengine.StringField(unique=True, max_length=20)
    introduce = mongoengine.StringField(max_length=5000)
    score = mongoengine.FloatField()
    score_num = mongoengine.IntField()
    star_info = mongoengine.ListField(mongoengine.IntField())
    read_num = mongoengine.IntField()
    book_list_num = mongoengine.IntField()
    tag_list = mongoengine.ListField(mongoengine.StringField(max_length=30))
    relate_book_list = mongoengine.ListField(mongoengine.IntField())
    final_score = mongoengine.FloatField()
    meta = {
        'ordering': ['-final_score']
    }

