#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     except_test
    Author:        Administrator
    Date:          2018/7/24
    Description:   异常测试
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
__author__ = 'Administrator'

def except_test():
    try:
        print(123)
        x = 1/0
        return 'correct'
    except Exception as e:
        print(e)
        return e
        
if __name__ == "__main__":
    print('main')
    ex = except_test()
    print(ex)