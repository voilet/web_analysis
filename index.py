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
import tornado.ioloop
import tornado.web
import time
from urls import *
import re
from mongoengine import *
import requests
import tornado.websocket
import datetime
from tornado.concurrent import run_on_executor
from data.models import hacker_data
from concurrent.futures import ThreadPoolExecutor
from models.hack_city import search_city
import tornado.gen
EXECUTOR = ThreadPoolExecutor(max_workers=4)



class BaseHandle(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHeandler(tornado.web.RequestHandler):
    """
    攻击饼图展示
    """
    executor = ThreadPoolExecutor(100)
    
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        """
        首页渲染数据
        """
        yield self.mongo_data()

    @run_on_executor
    def mongo_data(self):

        start_time = ((datetime.datetime.now()-datetime.timedelta(days=1)))
        stop_time = datetime.datetime.now()
        sl = hacker_data.objects(datetime__gte=start_time, datetime__lt=stop_time)
        pie_data = []
        pie_count = {}
        ip_count = {}
        for i in sl:
            pie_data.append(i.atk_type)
            if ip_count.get(i.atk_ip):
                ip_count[i.atk_ip] = ip_count[i.atk_ip] +1
            else:
                ip_count[i.atk_ip] = 1

        for i in pie_data:
            if pie_data.count(i) > 1:
                pie_count[i] = pie_data.count(i)
        atk_count = sl.count()
        ip_list = sorted(ip_count.iteritems(), key=lambda d:d[1], reverse = True)[:10]
        self.render("waf_pie.html", pie_count=pie_count, atk_count=atk_count, ip_list = ip_list)




class ChatSocketHandler(tornado.websocket.WebSocketHandler):

    connects = set()
    def check_origin(self, origin):
        return True

    def open(self):
        print "socket opened"
        ChatSocketHandler.connects.add(self)

    def on_message(self, message):
        ChatSocketHandler.send_all(message)

    def on_close(self):
        print "socketed closed"

    @classmethod
    def send_all(cls, chat):
        for connect in cls.connects:
            try:
                connect.write_message(chat)
            except:
                pass


class Atk_Handler(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self):
        """
        首页渲染数据
        """
        self.render("atk_china_map.html")


class MapHeandler(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self):
        """
        首页渲染数据
        """

        data = search_city()

        self.render("waf.html", pie_count=data)


class BarHeandler(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self):
        """
        首页渲染数据
        """
        start_time = ((datetime.datetime.now()-datetime.timedelta(days=1)))
        stop_time = datetime.datetime.now()
        sl = hacker_data.objects(datetime__gte=start_time, datetime__lt=stop_time)
        # data = search_city()
        # self.write(sl)
        self.render("bar.html", pie_count=sl)




