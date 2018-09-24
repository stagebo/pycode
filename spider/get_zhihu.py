#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     get_zhihu
    Author:        wyb
    Date:          2018/7/20
    Description:   
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃       ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃  永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
__author__ = 'wyb'
import req
import config
import re

if __name__ == "__main__":

    header = {
        'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }
    url = 'https://www.zhihu.com/question/265715946/answer/297480288'
    text,code = req.get_result(url,header=header)
    # print(text)
    # text = '<div 123>4546</div>'
    # ptn = re.compile(r'<div(.){0,}>(.){0,}<div>')
    #
    # ptn = re.compile(r'^[\u4E00-\u9FA5]+$')
    # sl = ptn.findall(text)
    # print(sl)
    #
    # text = '<div 123><div id="123s">skldjf</div></div>'
    # pattern = re.compile(r'<(div|span).{0,}>.{0,}</(div|span)>')
    # # pattern = re.compile(r'<div(.){0,}>(.){0,}<div>')
    # result2 = pattern.findall(text)
    # #
    # print(result2)


    it = re.finditer(r'<(div|span)[.]{0,}>.{0,}</(div|span)>',text)
    for match in it:
        print (match.group() )