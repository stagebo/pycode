#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/7/5'
__target__ 读取shape文件
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
import shapefile
def read_shape(fn):
    sf = shapefile.Reader(fn)
    shapes = sf.shapes()
    for shp in shapes:
        print(shp.bbox)
if __name__ == "__main__":
    print("main")
    fn = 'D:\\TDQS\\新疆\\聂桂春\\乌鲁木齐-高新区2018-7-4\\乌鲁木齐-高新区\\乌鲁木齐-高新区\\Line.shp'
    read_shape(fn)