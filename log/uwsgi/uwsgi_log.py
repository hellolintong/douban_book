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
    write_info(get_logger(), information)*** Starting uWSGI 2.0.8 (64bit) on [Sat Dec  6 19:57:19 2014] ***
compiled with version: 4.8.2 on 26 November 2014 16:23:35
os: Linux-3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014
nodename: iZ28t0a1iakZ
machine: x86_64
clock source: unix
detected number of CPU cores: 1
current working directory: /home/Flask
detected binary path: /usr/local/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
uWSGI running as root, you can use --uid/--gid/--chroot options
*** WARNING: you are running uWSGI as root !!! (use the --uid flag) *** 
your processes number limit is 7786
your memory page size is 4096 bytes
detected max file descriptor number: 65535
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uwsgi socket 0 bound to TCP address 0.0.0.0:5000 fd 3
Python version: 2.7.6 (default, Mar 22 2014, 23:03:41)  [GCC 4.8.2]
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0x1763a30
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 145520 bytes (142 KB) for 1 cores
*** Operational MODE: single process ***
added /home/Flask/ to pythonpath.
WSGI app 0 (mountpoint='') ready in 0 seconds on interpreter 0x1763a30 pid: 1729 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 1729)
spawned uWSGI worker 1 (pid: 1733, cores: 1)
{address space usage: 79679488 bytes/75MB} {rss usage: 17498112 bytes/16MB} [pid: 1733|app: 0|req: 1/1] 219.245.66.153 () {40 vars in 661 bytes} [Sat Dec  6 19:57:33 2014] GET / => generated 2306 bytes in 330 msecs (HTTP/1.1 200) 2 headers in 80 bytes (1 switches on core 0)
{address space usage: 79679488 bytes/75MB} {rss usage: 17752064 bytes/16MB} [pid: 1733|app: 0|req: 2/2] 219.245.66.153 () {42 vars in 703 bytes} [Sat Dec  6 19:57:34 2014] GET /static/css/bootstrap.min.css => generated 114011 bytes in 6 msecs via sendfile() (HTTP/1.1 200) 7 headers in 287 bytes (0 switches on core 0)
{address space usage: 79679488 bytes/75MB} {rss usage: 17846272 bytes/17MB} [pid: 1733|app: 0|req: 3/3] 219.245.66.153 () {42 vars in 687 bytes} [Sat Dec  6 19:57:34 2014] GET /static/css/theme.css => generated 101 bytes in 2 msecs via sendfile() (HTTP/1.1 200) 7 headers in 282 bytes (0 switches on core 0)
{address space usage: 79941632 bytes/76MB} {rss usage: 17846272 bytes/17MB} [pid: 1733|app: 0|req: 4/4] 219.245.66.153 () {42 vars in 684 bytes} [Sat Dec  6 19:57:34 2014] GET /static/js/bootstrap.min.js => generated 34653 bytes in 2 msecs via sendfile() (HTTP/1.1 200) 7 headers in 284 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18116608 bytes/17MB} [pid: 1733|app: 0|req: 5/5] 219.245.66.153 () {40 vars in 612 bytes} [Sat Dec  6 19:57:35 2014] GET /favicon.ico => generated 233 bytes in 11 msecs (HTTP/1.1 404) 2 headers in 71 bytes (1 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18145280 bytes/17MB} [pid: 1733|app: 0|req: 6/6] 219.245.66.153 () {42 vars in 692 bytes} [Sat Dec  6 19:57:37 2014] GET / => generated 2306 bytes in 2 msecs (HTTP/1.1 200) 2 headers in 80 bytes (1 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18173952 bytes/17MB} [pid: 1733|app: 0|req: 7/7] 219.245.66.153 () {48 vars in 848 bytes} [Sat Dec  6 19:57:37 2014] GET /static/css/bootstrap.min.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 188 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18182144 bytes/17MB} [pid: 1733|app: 0|req: 8/8] 219.245.66.153 () {48 vars in 830 bytes} [Sat Dec  6 19:57:37 2014] GET /static/css/theme.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 186 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18194432 bytes/17MB} [pid: 1733|app: 0|req: 9/9] 219.245.66.153 () {48 vars in 828 bytes} [Sat Dec  6 19:57:37 2014] GET /static/js/bootstrap.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 187 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18194432 bytes/17MB} [pid: 1733|app: 0|req: 10/10] 219.245.66.153 () {42 vars in 692 bytes} [Sat Dec  6 20:04:35 2014] GET / => generated 2306 bytes in 2 msecs (HTTP/1.1 200) 2 headers in 80 bytes (1 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18198528 bytes/17MB} [pid: 1733|app: 0|req: 11/11] 219.245.66.153 () {46 vars in 817 bytes} [Sat Dec  6 20:04:35 2014] GET /static/css/bootstrap.min.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 188 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18202624 bytes/17MB} [pid: 1733|app: 0|req: 12/12] 219.245.66.153 () {46 vars in 799 bytes} [Sat Dec  6 20:04:35 2014] GET /static/css/theme.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 186 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18202624 bytes/17MB} [pid: 1733|app: 0|req: 13/13] 219.245.66.153 () {46 vars in 797 bytes} [Sat Dec  6 20:04:35 2014] GET /static/js/bootstrap.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 187 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18202624 bytes/17MB} [pid: 1733|app: 0|req: 14/14] 219.245.66.153 () {42 vars in 692 bytes} [Sat Dec  6 20:04:37 2014] GET / => generated 2306 bytes in 2 msecs (HTTP/1.1 200) 2 headers in 80 bytes (1 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18210816 bytes/17MB} [pid: 1733|app: 0|req: 15/15] 219.245.66.153 () {48 vars in 848 bytes} [Sat Dec  6 20:04:37 2014] GET /static/css/bootstrap.min.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 188 bytes (0 switches on core 0)
{address space usage: 80101376 bytes/76MB} {rss usage: 18214912 bytes/17MB} [pid: 1733|app: 0|req: 16/16] 219.245.66.153 () {48 vars in 830 bytes} [Sat Dec  6 20:04:37 2014] GET /static/css/theme.css => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 186 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18223104 bytes/17MB} [pid: 1733|app: 0|req: 17/17] 219.245.66.153 () {48 vars in 828 bytes} [Sat Dec  6 20:04:37 2014] GET /static/js/bootstrap.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 187 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 18/18] 219.245.66.153 () {42 vars in 692 bytes} [Sat Dec  6 20:04:50 2014] GET / => generated 2306 bytes in 2 msecs (HTTP/1.1 200) 2 headers in 80 bytes (1 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 19/19] 219.245.66.153 () {48 vars in 848 bytes} [Sat Dec  6 20:04:50 2014] GET /static/css/bootstrap.min.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 188 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 20/20] 219.245.66.153 () {48 vars in 830 bytes} [Sat Dec  6 20:04:50 2014] GET /static/css/theme.css => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 186 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 21/21] 219.245.66.153 () {48 vars in 828 bytes} [Sat Dec  6 20:04:50 2014] GET /static/js/bootstrap.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 187 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 22/22] 219.245.66.153 () {42 vars in 692 bytes} [Sat Dec  6 20:04:56 2014] GET / => generated 2306 bytes in 2 msecs (HTTP/1.1 200) 2 headers in 80 bytes (1 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 23/23] 219.245.66.153 () {48 vars in 848 bytes} [Sat Dec  6 20:04:56 2014] GET /static/css/bootstrap.min.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 188 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 24/24] 219.245.66.153 () {48 vars in 830 bytes} [Sat Dec  6 20:04:56 2014] GET /static/css/theme.css => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 186 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 25/25] 219.245.66.153 () {48 vars in 828 bytes} [Sat Dec  6 20:04:56 2014] GET /static/js/bootstrap.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 187 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 26/26] 219.245.66.153 () {42 vars in 692 bytes} [Sat Dec  6 20:04:57 2014] GET / => generated 2306 bytes in 2 msecs (HTTP/1.1 200) 2 headers in 80 bytes (1 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 27/27] 219.245.66.153 () {48 vars in 848 bytes} [Sat Dec  6 20:04:57 2014] GET /static/css/bootstrap.min.css => generated 0 bytes in 1 msecs (HTTP/1.1 304) 4 headers in 188 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 28/28] 219.245.66.153 () {48 vars in 830 bytes} [Sat Dec  6 20:04:57 2014] GET /static/css/theme.css => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 186 bytes (0 switches on core 0)
{address space usage: 80363520 bytes/76MB} {rss usage: 18231296 bytes/17MB} [pid: 1733|app: 0|req: 29/29] 219.245.66.153 () {48 vars in 828 bytes} [Sat Dec  6 20:04:57 2014] GET /static/js/bootstrap.min.js => generated 0 bytes in 0 msecs (HTTP/1.1 304) 4 headers in 187 bytes (0 switches on core 0)
Sat Dec  6 20:07:45 2014 - uWSGI worker 1 screams: UAAAAAAH my master disconnected: i will kill myself !!!
