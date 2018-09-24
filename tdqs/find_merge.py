#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/7/11'
__target__ 提取合并单元格信息
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
def get_merge(lst):
    ret = []
    if len(lst) < 2:
        return []
    if lst[0] == lst[1]:
        ret.append(0)
    idx = 1
    while idx < len(lst)-1:
        if (lst[idx] == lst[idx - 1] and lst[idx] != lst[idx + 1]) or (lst[idx] == lst[idx + 1] and lst[idx] != lst[idx - 1]):
                ret.append(idx)
        idx += 1

    if lst[-1] == lst[-2]:
        ret.append(len(lst)-1)
    return ret

if __name__ == "__main__":
    lst = ['a','a','b','b']
    ret = get_merge(lst)
    print(ret)
    print("main")