# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: d3_data.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-28
#      History: 
#=============================================================================

import websocket
import time
import json
from websocket import create_connection
# from settings import engine, DB_Session
# from jm_waf.models import Hack

import pygeoip
gi = pygeoip.GeoIP('GeoLiteCity.dat', pygeoip.MEMORY_CACHE)

# test = DB_Session.query(Hack).all()
ws = create_connection("ws://127.0.0.1:8001/websocket")
# for i in test:
#     # print i.ip
#     atk_data = {'city': 'Changsha', 'dport': '80', 'countrycode': 'CN', 'country': 'CN', 'latitude2': 35.86,
#                 'longitude2': 104.1, 'longitude': '10.08', 'svc': 'http', 'country2': 'US', 'city2': 'Miami',
#                 'countrycode2': 'US', 'latitude': '34.63', 'org': 'http hacker', 'zerg': '', 'type': 'web atk',
#                 'md5': ''}
#     rst = gi.record_by_addr(i.ip)
#     time.sleep(0.1)
#     try:
#         # atk_data["city"] = rst.get("city", None)
#         # atk_data["countrycode"] = rst["country_code"]
#         # atk_data["country"] = rst["country_code3"]
#         # atk_data["country2"] = "CN"
#         # atk_data["countrycode2"] = "CN"
#         # atk_data["city2"] = "Beijing"
#         # atk_data["md5"] = i.ip
#         # atk_data["latitude"] = rst["latitude"]
#         # atk_data["longitude"] = rst["longitude"]
#         # print atk_data
#         s = {'city': str(rst["city"]), 'countrycode': 'MO', 'latitude': rst["latitude"], 'country': 'MAC', 'latitude2': 35.86, 'longitude2': 104.1, 'longitude': rst["longitude"], 'svc': 'http', 'country2': 'CN', 'city2': 'Beijing', 'org': 'Hurricane Electric', 'dport': '80', 'countrycode2': 'CN', 'zerg': '', 'type': 'ipviking.honey', 'md5': str(i.ip)}
#         print s
#         s = "%s" %(s)
#         ws.send(s)
#         result = ws.recv()
#     except Exception, e:
#         pass
# ws.close()



#
json_file = open("./data/d3_test.txt", "r")
# atk_data = {'city': 'Changsha', 'dport': '80', 'countrycode': 'CN', 'country': 'CN', 'latitude2': 35.86, 'longitude2': 104.1, 'longitude': '10.08', 'svc': 'http', 'country2': 'US', 'city2': 'Miami', 'countrycode2': 'US', 'latitude': '34.63', 'org': 'http hacker', 'zerg': '', 'type': 'ipviking.honey', 'md5': '210.78.137.6'}
json_data = json_file.readlines()
# # for i in json_data:
# #     s = json.loads(i)
# #     s["latitude2"] = 35.86
# #     s["longitude2"] = 104.1
# #     print s
# # while True:
# for i in json_data:
#
#     s = "%s" % (i)
#     print s
#     ws.send(s)
#     result = ws.recv()
#     time.sleep(1)
"""
'latitude': '31.22', 'longitude': '121.47', 为攻击者的坐标
country 攻击来源
country2 攻击目标
{"latitude":"51.00","longitude":"9.00","countrycode":"DE","country":"DE","city":"","org":"Hetzner Online AG - Virtualisierung","latitude2":"47.61","longitude2":"-122.33","countrycode2":"US","country2":"US","city2":"Seattle","type":"ipviking.honey","md5":"78.47.106.229","dport":"50509","svc":"50509","zerg":""}
"""
s = {'city': '江苏', 'dport': '80', 'countrycode': 'CN', 'country': 'CN', 'latitude2': 39.93, 'longitude2': 116.39, 'Target': '123.125.20.1', 'latitude': '31.22', 'longitude': '121.47', 'svc': 'http', 'country2': 'CN', 'city2': '南宁机房', 'countrycode2': 'US',  'hostip': '123.125.2.2', 'zerg': '111111', 'type': 'SQL注入', 'md5': '210.78.137.6'}
# print type(s)
ws.send(json.dumps(s))
# ws.send(json.dumps(s))
# result = ws.recv()
# print result
ws.close()


