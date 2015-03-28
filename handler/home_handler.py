from flask import render_template
from flask import Blueprint
from flask import redirect
from db.douban_book import douban_book_model
from db.douban_tag import douban_tag_model
from db.user import user_model
from user_handler import login_check
from user_handler import get_login_user_id
from config import Config
from cache import redis_handler

home = Blueprint('home', __name__, template_folder=Config.PARENT_DIR+'/templates', static_folder=Config.PARENT_DIR+'/static')


@home.route('/page/<int:page>')
def page(page):
    if page < 0:
        page = 0

    #get books and tags number
    book_redis_handler = redis_handler.get_book_redis_handler()
    tag_redis_handler = redis_handler.get_tag_redis_handler()
    book_num = book_redis_handler.get_set_len()
    tag_num = tag_redis_handler.get_set_len()

    #get tags by page number
    tags = douban_tag_model.get_tag(start=page*20, end=(page+1)*20)

    #check if user login
    user_id = None
    login = login_check()
    if login:
        user_id = get_login_user_id()
        user = user_model.get_user(id=user_id)[0]
        new_tag_back_up = list()
        for tag in tags:
            if tag.name not in user.collect_tags:
                new_tag_back_up.append(tag)
        tags = new_tag_back_up

    return render_template('index.html', tags=tags, login=login, user_id=user_id, book_num=book_num, tag_num=tag_num, page=page)

@home.route('/')
def index():
    return  redirect('/page/0')


@home.route('/tag/<tag_name>/<int:page>')
def tag(tag_name, page):
    #get login user
    login = login_check()
    user_id = None
    if login:
        user = user_model.get_user(id=get_login_user_id())[0]
        user_id = user.id

    #get tag
    tag = douban_tag_model.get_tag(name=tag_name)[0]
    book_list = list()

    #get book by tag name
    if len(tag.book_list) > (page + 1) * 20:
        tag.book_list = tag.book_list[page*20:(page+1)*20]
    for book_id in tag.book_list:
        book = douban_book_model.get_book(book_id=book_id)
        if book:
            book = book[0]
            book.relate_book_dir = {}
            for relate_book_id in book.relate_book_list:
                relate_book = douban_book_model.get_book(book_id=relate_book_id)
                if relate_book:
                    book.relate_book_dir[relate_book_id] = relate_book[0].title
            book_list.append(book)
    book_list.sort(key=lambda book: book.final_score, reverse=True)
    return render_template('book.html', books=book_list, tag=tag_name, login=login, user_id=user_id, page=page)

@home.route('/about')
def about():
    login = login_check()
    user_id = get_login_user_id()
    return render_template('about.html', login=login, user_id=user_id)
