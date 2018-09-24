#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     happy_glass
    Author:        wyb
    Date:          2018/9/1 0001
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
import time
import os,sys
if __name__ == "__main__":
    print("main")
    idx = 0
    while 1:
        idx += 1
        x = 552
        cmd = 'adb shell input swipe %s 1000 %s 550'%(x,x)
        if idx%4==0:
            cmd =  'adb shell input swipe 552 1000 555 550'
        print(idx,cmd)
        os.system(cmd)
        time.sleep(1.5)