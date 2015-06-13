#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
#     FileName: data_fx.py
#         Desc: 2015-15/3/16:上午11:17
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      History: 
# =============================================================================
from mongoengine import *
connect("hacker_atk", host="127.0.0.1", port=27017)
from websocket import create_connection
import json
import pygeoip
import time

gi = pygeoip.GeoIP('GeoLiteCity.dat', pygeoip.MEMORY_CACHE)
ws = create_connection("ws://127.0.0.1:8001/websocket")

from data.models import hacker_data, php_analysis
db = hacker_data.objects.all()
for data in db:
    s = {'city': '江苏', 'dport': '80', 'countrycode': 'CN', 'country': 'bj11', 'latitude2': 39.93, 'longitude2': 116.39, 'latitude': '31.22', 'longitude': '121.47', 'svc': 'http', 'country2': 'CN', 'city2': '南宁机房', 'countrycode2': 'US',  'hostip': '123.125.2.2', 'zerg': '111111', 'type': data["atk_type"], 'md5': '210.78.137.6'}

    rst = gi.record_by_addr(data["atk_ip"])
    try:
        s["city"] = data["city"]
        s["countrycode"] = rst.get("country_code")
        s["country"] = rst["time_zone"]
        s["country2"] = "beijing"
        s["countrycode2"] = "CN"
        # s["city2"] = service_addr
        s["md5"] = data["atk_ip"]
        s["hostip"] = data["idc_server"]
        s["latitude"] = rst["latitude"]
        s["longitude"] = rst["longitude"]
        ws.send(json.dumps(s))
        ws.recv()
        time.sleep(0.1)
        print s
    except:
        pass
ws.close()
