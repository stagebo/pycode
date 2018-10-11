#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/7/11'
__target__ 读取配置文件
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
import configparser
def read_config(cf):
    host = cf.get("dbconf", "host")
    port = cf.getint("dbconf", "port")
    dbname = cf.get("dbconf", "dbname")
    user = cf.get("dbconf", "user")
    pwd = cf.get("dbconf", "pwd")
    result = {
        "host":host,
        "port":port,
        "dbname":dbname,
        "user":user,
        "pwd":pwd,

    }
    return result

if __name__ == "__main__":

    cf = configparser.ConfigParser()
    cf.read("../app.conf",encoding='utf-8')
    rt = read_config(cf)
    print(rt)
    print("main")