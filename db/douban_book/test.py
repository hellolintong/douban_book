#coding=utf-8
from douban_book_model import get_book

if __name__ == "__main__":
    books = get_book()
    print len(books)
