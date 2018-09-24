#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     reg_test
    Author:        wyb
    Date:          2018/7/20
    Description:   正则表达式测试
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


import re
# def test():
#     url = '23.00'
#     pattern = re.compile(r'\.[0-9]+$')
#     print (pattern.findall(url))
#     out = re.sub(pattern, '', url)
#     print (out)

# if __name__ == "__main__":
    # st = '123.00'
    # ptn = re.compile(r'\.[0]+')

    # ret = re.sub(ptn,'$1',st)
    # print(st,ret)
    #
    # print(re.match(ptn, st))  # 在起始位置匹配
    # print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
    #
    # line = "Cats are smarter than dogs"
    #
    # matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
    #
    # if matchObj:
    #     print("matchObj.group() : ", matchObj.group())
    #     print("matchObj.group(1) : ", matchObj.group(1))
    #     print("matchObj.group(2) : ", matchObj.group(2))
    # else:
    #     print("No match!!")
    # v = '123.0010100'
    # mo = re.match(r'([\d]+)\.([\d]{0,}[1-9]){0,}([0]+)',v,re.M|re.I)
    # if mo:
    #     print(mo.group(1))
    #     print(mo.group(2))
    #     print(mo.group(3))
    #     print(v.replace(mo.group(3),''))


# 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)

#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))
#
# print(re.findall(r'[\d]+','adbdf212df512df'))
# print(re.findall(r'<div(\.)+</div>]', "<div class=123>this is content</div>"))
print(re.match(r'<div(\.)+</div>]', "<div class=123>this is content</div>",re.M|re.I))