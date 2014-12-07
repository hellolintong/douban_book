# coding:utf-8
from log.log_base import init
from log.log_base import write_info

g_logger = None


def get_logger():
    global g_logger
    if not g_logger:
        g_logger = init("crawler_logger", "log/crawler/crawler.log")
    return g_logger


def log_info(information):
    write_info(get_logger(), information)