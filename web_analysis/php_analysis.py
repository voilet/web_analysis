#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
#     FileName: php_analysis.py
#         Desc: 2015-15/3/13:上午11:23
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
from data.models import hacker_data, php_analysis

from concurrent.futures import ThreadPoolExecutor
from models.hack_city import search_city
EXECUTOR = ThreadPoolExecutor(max_workers=4)
import json
# self.get_argument("mac")


class php_map(tornado.web.RequestHandler):
    """
    攻击饼图展示
    """
    def get(self):
        name = self.get_argument("name")
        start_time = ((datetime.datetime.now()-datetime.timedelta(days=7)))
        stop_time = datetime.datetime.now()
        sl = php_analysis.objects(date_time__gte=start_time, date_time__lt=stop_time, name=name).order_by('date_time')

        self.render("analysis/php_p95.html", data=sl, name=name)

    executor = ThreadPoolExecutor(100)
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
        首页渲染数据
        """

        try:
            date_time = self.get_argument("date_time")
            name = self.get_argument("name")
            count = self.get_argument("count")
            p95 = self.get_argument("p95")
            p90 = self.get_argument("p90")
            p85 = self.get_argument("p85")
            avg = self.get_argument("avg")
            d_time = date_time.split("|")
            print d_time
            db_time = "%s %s" %(d_time[0], d_time[1])

            print db_time, name, count, p95, p90, p85, avg
            db = php_analysis()
            db.avg = avg
            db.name = name
            db.count = count
            db.p85 = p85
            db.p90 = p90
            db.p95 = p95
            db.date_time = db_time
            db.save()
            print "save ok"
            return self.write(json.dumps({"status": 200, "result": "OK"}, indent=4))

        except:
            print "save error"
            return self.write(json.dumps({"status": 403, "result": "OK"}, indent=4))