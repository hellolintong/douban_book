#coding=utf8
__author__ = 'lintong'
import mongoengine
import hashlib
from user_storage import UserStorage
from config import Config


mongoengine.connect(Config.DB_NAME, host=Config.DB_HOST, port=Config.DB_PORT)


##########user operation#############
def add_user(**kwargs):
    user = UserStorage()
    user.name = kwargs['name']
    user.password = _encrypt(kwargs['name'], kwargs['password'])
    user.collect_tags = []
    try:
        user.save()
    except Exception:
        return None
    return user


def get_user(**kwargs):
    return UserStorage.get(**kwargs)


def del_user(user):
    user.delete()


########password operataion#######
def check_user(user, password):
    return user.password == _encrypt(user.name, password)


def update_password(user, old_password, new_password):
    if user.password != _encrypt(user.name, old_password):
        return False
    user.password = _encrypt(user.name, new_password)
    return True


#####tag operation##########
def add_tag(user, tag):
    if tag not in user.collect_tags:
        user.collect_tags.append(tag)
        user.save()


def del_tag(user, tag):
    user.collect_tags.remove(tag)
    user.save()


def update_tag(user, tags):
    user.collect_tags = tags
    user.save()


def _encrypt(name, password):
    """
        encrpy the password by name
    """
    return hashlib.md5(password.encode('utf8') + name.encode('utf8')).hexdigest().upper()