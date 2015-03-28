#coding=utf8
__author__ = 'lintong'
import mongoengine
from douban_book_storage import DoubanBookStorage
from config import Config


mongoengine.connect(Config.DB_NAME, host=Config.DB_HOST, port=Config.DB_PORT)


##########user edit#############
def add_book(**kwargs):
    book = DoubanBookStorage()
    book.img_url = kwargs['img_url']
    book.book_id = kwargs['book_id']
    book.title = kwargs['name']
    book.author = kwargs['author']
    book.public_date = kwargs['public_date']
    book.page = kwargs['page']
    book.price = kwargs['price']
    book.ISBN = kwargs['ISBN']
    book.introduce = kwargs['introduce']
    book.score = kwargs['score']
    book.score_num = kwargs['score_num']
    book.star_info = kwargs['star_info']
    book.read_num = kwargs['read_num']
    book.book_list_num = kwargs['book_list_num']
    book.tag_list = kwargs['tag_list']
    book.relate_book_list = kwargs['relate_book_list']
    book.final_score = cal_real_score(**kwargs)
    try:
        book.save()
    except Exception:
        return None
    return book


def update_book(book, **kwargs):
    if kwargs.get('id'):
        raise AttributeError("Can't update book id")
    book.update(**kwargs)


def delete_book(book):
    book.delete()


def get_book(**kwargs):
    start = kwargs.pop("start", 0)
    end = kwargs.pop("end", 20)
    return DoubanBookStorage.get(**kwargs)[start:end]


def cal_real_score(**kwargs):

    def get_cal(num, weight):
        return (num * 1.0 / ((100 + num) * 1.0)) * weight

    final_score = 0
    final_score += get_cal(kwargs['score_num'], 0.7)
    final_score *= kwargs['score']
    final_score += get_cal(kwargs['read_num'], 0.1)
    final_score += get_cal(kwargs['book_list_num'], 0.1)
    star_num = kwargs['star_info'][0] * 3 + kwargs['star_info'][1] * 2 + kwargs['star_info'][2] * -1 + kwargs['star_info'][3] * -2 + kwargs['star_info'][4] * -3
    final_score += get_cal(star_num, 0.1)
    return final_score
