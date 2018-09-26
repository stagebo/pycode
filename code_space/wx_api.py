#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
__target__ = 微信测试
'''
from wxpy import *
import requests
key = "81410c064db0455ca2debf20c5aa9972"
session = requests.session()

url = 'http://sandbox.api.simsimi.com/request.p'

data = {'key' : 'd6bbfd1b-7cb3-4cfe-87b1-261e4d210d19',
          'lc' : "ch",
          'ft' : '0.0',
	  'text' : "你好啊"}

ret = requests.get(url,data)
print(ret.content)

