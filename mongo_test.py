#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
#     FileName: mongo_test.py
#         Desc: 2015-15/3/12:下午4:00
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      History: 
# =============================================================================

from mongoengine import *
from data.models import hacker_data
import datetime
import time
from websocket import create_connection
import pygeoip
import json

connect("hacker_atk", host="192.168.115.205", port=27017)
start_time = ((datetime.datetime.now()-datetime.timedelta(days=3)))
stop_time = datetime.datetime.now()

gi = pygeoip.GeoIP('GeoLiteCity.dat', pygeoip.MEMORY_CACHE)

test = hacker_data.objects(datetime__gte=start_time, datetime__lt=stop_time)
ws = create_connection("ws://192.168.8.80:8001/websocket")
for i in test:
    # print i.ip
    """
    'latitude': '31.22', 'longitude': '121.47', 为攻击者的坐标
    country 攻击来源
    country2 攻击目标
    {"latitude":"51.00","longitude":"9.00","countrycode":"DE","country":"DE","city":"","org":"Hetzner Online AG - Virtualisierung","latitude2":"47.61","longitude2":"-122.33","countrycode2":"US","country2":"US","city2":"Seattle","type":"ipviking.honey","md5":"78.47.106.229","dport":"50509","svc":"50509","zerg":""}
    """
    s = {'city': '江苏', 'dport': '80', 'countrycode': 'CN', 'country': 'bj11', 'latitude2': 39.93, 'longitude2': 116.39, 'Target': '123.125.20.1', 'latitude': '31.22', 'longitude': '121.47', 'svc': 'http', 'country2': 'CN', 'city2': '南宁机房', 'countrycode2': 'US',  'hostip': '123.125.2.2', 'zerg': '111111', 'type': i["atk_type"], 'md5': '210.78.137.6'}

    rst = gi.record_by_addr(i.atk_ip)
    service_addr = gi.record_by_addr(i["idc_server"])

    try:
        s["city"] = i["city"]
        s["countrycode"] = rst.get("country_code")
        s["country"] = rst["time_zone"]
        s["country2"] = "beijing"
        s["countrycode2"] = "CN"
        s["city2"] = service_addr["city"]
        s["md5"] = i["atk_ip"]
        s["hostip"] = i["idc_server"]
        s["latitude"] = rst["latitude"]
        s["longitude"] = rst["longitude"]
        ws.send(json.dumps(s))
        result = ws.recv()
    except:
        print i["atk_ip"]
        pass
    time.sleep(0.1)
ws.close()