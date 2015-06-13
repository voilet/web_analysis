#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2013-02-20 14:52:11
#      History:
#=============================================================================


import os
from os.path import abspath, dirname

import redis
import tornado.httpserver
import tornado.web
from tornado.log import app_log
from tornado.options import define, options
from urls import handlers
from mongoengine import *


PROJECT_DIR = dirname(dirname(abspath(__file__)))
TEMPLATE_DIR = os.path.join(PROJECT_DIR, 'templates')
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')



# define('redis_host', default='localhost')
# define('redis_db', default=2, type=int)
define('redis_channel', default='web_chat', help='message pubsub channel')
define("debug", default=True, type=bool)
define("port", default=8001, type=int)
connect("hacker_atk", host="127.0.0.1", port=27017)

class Application(tornado.web.Application):

    _CLIENTS_MAP = {}

    def __init__(self):


        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            "login_url": "/",
            "debug": options.debug,
            "cookie_secret": "8i$2jaau-_w%yqwazz7xikka*^ekkvmn$4+25v8&amp;ngz+$&amp;qy#3",
            "xsrf_cookies": False,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def run():
    """
    start chat application

    """
    tornado.options.parse_command_line()
    port = os.environ.get("PORT", options.port)
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port)
    # app_log.info("application run on {0}".format(port))
    tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
    application = Application()

