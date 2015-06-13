#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
#     FileName: hacker_list.py
#         Desc: 2015-15/3/20:下午2:46
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      History: 
# =============================================================================

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



class atk_list(tornado.web.RequestHandler):
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
        try:
            page = int(self.get_argument("page"))
            if page <= 0:
                page = -page
        except:
            page = 1

        if page == 1:
            data = hacker_data.objects.all()
            sl = data.order_by("-datetime").limit(10)
        else:
            skip_num = page * 10
            data = hacker_data.objects.all()
            sl = data.order_by("-datetime").skip(skip_num).limit(10)
        count_sum = [x for x in range(1, data.count()/10+1)]

        old_sum = len(count_sum)

        page_list = [1]


        start_num = page-5

        if start_num >= 0:
            if page <= 5:
                for i in range(2, 9):
                    page_list.append(i)

            else:
                if start_num == 1:
                    start_num += 1

                    for i in range(start_num, page+5):
                        page_list.append(i)
                else:
                    for i in range(start_num, page+5):
                        page_list.append(i)
        else:
            if page <= 5:
                for i in range(2, 10):
                    page_list.append(i)
            else:
                for i in range(start_num, page+5):
                    page_list.append(i)

        page_list.append(old_sum)

        next = page + 1 if page < old_sum else None
        previous = page - 1 if page > 1 else None

        self.render("hacker_list.html", data=sl, page=page_list, current=page, next=next, previous=previous)