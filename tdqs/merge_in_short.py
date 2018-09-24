#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/7/6'
__target__  合并单元格的合并信息
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
def get_key(ele):
    return ele[0]
def merge_mg(merge_info):
    merge_info.sort(key=get_key)
    for m in merge_info:
        print(m)

def _get_header_merge_info(header_data):
    rg = []
    hd = header_data
    for i in range(1, len(hd)):
        for j in range(0, len(hd[0])):
            if hd[i][j] == hd[i - 1][j]:
                rg.append((i - 1, i + 1, j, j + 1))
    for i in range(0, len(hd)):
        for j in range(1, len(hd[0])):
            if hd[i][j] == hd[i][j - 1]:
                rg.append((i, i + 1, j - 1, j + 1))
    return rg

def _get_header_merge_info1(hd):
    return []
if __name__ == "__main__":
    # print("main")
    hd = [['类目', '实绩值', '实绩值', '实绩值', '实绩值', '实绩值', '实绩值', '预测值', '预测值'],
          ['类目', '2013', '2014', '2015', '2016', '2017', '年均增长率(%)', '2025', '年均增长率(%)']]
    # mginfo = _get_header_merge_info(hd)
    # print('old =======================')
    # for m in mginfo:
    #     print(m)
    #
    # mginfo = _get_header_merge_info1(hd)
    # print('old =======================')
    # for m in mginfo:
    #     print(m)
    rg = []

    for i in range(0,len(hd)):
        d = hd[i]
        dic = {}
        for j in range(1,len(d)):
            if d[j] not in dic.keys():
                dic[d[j]] = []
            dic[d[j]].append(j)
        rgs = []
        for key in dic.keys():
            for idx in dic[key]:
                if idx-1 not in dic[key] or idx+1 not in dic[key]:
                    rgs.append(idx)
        ix = 0
        while ix < len(rgs):
            if rgs[ix+1]-1 != rgs[ix]:
                rg.append((i,i+1, rgs[ix],rgs[ix+1]))
            ix += 2
    print(rg)
