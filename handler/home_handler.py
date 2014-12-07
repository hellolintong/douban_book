from flask import render_template
from flask import Blueprint
from db.douban_book import douban_book_model
from db.douban_tag import douban_tag_model
from db.user import user_model
from user_handler import login_check
from user_handler import get_login_user_id
from config import Config
from cache import redis_handler

home = Blueprint('home', __name__, template_folder=Config.PARENT_DIR+'/templates', static_folder=Config.PARENT_DIR+'/static')


@home.route('/')
def index():
    import pdb; pdb.set_trace()
    book_redis_handler = redis_handler.get_book_redis_handler()
    tags = douban_tag_model.get_tag()
    new_tags = list()
    for tag in tags:
        number = 0
        for book_id in tag.book_list:
            if book_redis_handler.check_set_member(book_id):
                number += 1
        print number
        if number > 10:
            tag.book_number = number
            new_tags.append(tag)

    user_id = None
    login = login_check()
    if login:
        user_id = get_login_user_id()
        user = user_model.get_user(id=user_id)[0]
        new_tag_back_up = list()
        for tag in new_tags:
            if tag.name not in user.collect_tags:
                new_tag_back_up.append(tag)
        new_tags = new_tag_back_up

    new_tags.sort(key=lambda x: x.book_number, reverse=True)
    return render_template('index.html', tags=new_tags, login=login, user_id=user_id)


@home.route('/tag/<tag_name>')
def tag(tag_name):
    login = login_check()
    user_id = None
    if login:
        user = user_model.get_user(id=get_login_user_id())[0]
        user_id = user.id
    tag = douban_tag_model.get_tag(name=tag_name)[0]
    book_list = list()
    for book_id in tag.book_list:
        book = douban_book_model.get_book(book_id=book_id)
        if book:
            book_list.append(book[0])
    book_list.sort(key=lambda book : book.final_score, reverse=True)
    return render_template('book.html', books=book_list, tag=tag_name, login=login, user_id=user_id)

@home.route('/about')
def about():
    login = login_check()
    user_id = get_login_user_id()
    return render_template('about.html', login=login, user_id=user_id)
