#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: urls.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014 14-2-23 上午12:40
#      History: 
#=============================================================================

import tornado.web
from index import MainHeandler,  ChatSocketHandler, Atk_Handler, MapHeandler, BarHeandler
from models.hacker_list import atk_list
from web_analysis.php_analysis import php_map

handlers = [
    (r"/", MainHeandler),
    (r"/hacker/atk", Atk_Handler),
    (r"/hacker/map", MapHeandler),
    (r"/hacker/bar", BarHeandler),
    (r"/hacker/list/$", atk_list),
    (r"/php_analysis/$", php_map),
    (r"/websocket", ChatSocketHandler),
]