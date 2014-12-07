# coding:utf-8
import redis

g_book_redis_handler = None
g_tag_redis_handler = None


class RedisHandler():
    def __init__(self, name):
        self.connection = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
        self.set_name = name + '_set'
        self.queue_name = name + '_queue'

    def batch_add_set_member(self, elem_list):
        for elem in elem_list:
            self.connection.sadd(self.set_name, elem)

    def push_queue(self, elem):
        self.connection.rpush(self.queue_name, elem)

    def pop_queue(self):
        return self.connection.lpop(self.queue_name)

    def queue_len(self):
        return self.connection.llen(self.queue_name)

    def check_set_member(self, elem):
        return self.connection.sismember(self.set_name, elem)

    def add_set_member(self, elem):
        return self.connection.sadd(self.set_name, elem)


def get_book_redis_handler():
    global g_book_redis_handler
    if not g_book_redis_handler:
        g_book_redis_handler = RedisHandler('book')
    return g_book_redis_handler


def get_tag_redis_handler():
    global g_tag_redis_handler
    if not g_tag_redis_handler:
        g_tag_redis_handler = RedisHandler('tag')
    return g_tag_redis_handler