#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     req
    Author:        wyb
    Date:          2018/9/23 0023
    Description:   获取金山每日一句
"""
import requests


url = "http://open.iciba.com/dsapi/"
r = requests.get(url)
print(r.json())
