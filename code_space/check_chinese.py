#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     check_chinese
    Author:        wyb
    Date:          2018/7/17
    Description:   判断字符串中是否有中文
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

patten = '中文、英文、数字包括下划线：^[\u4E00-\u9FA5A-Za-z0-9_]+$'
def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

if __name__ == "__main__":
    print(check_contain_chinese('中国'))
    print(check_contain_chinese('xxx'))
    print(check_contain_chinese('xx中国'))
