#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     timer_test
    Author:        wyb
    Date:          2018/9/25 0025
    Description:   
"""
import threading
import time

def hello(name):
    print ("hello %s" % name)

    global timer
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()

if __name__ == "__main__":
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()
    print(123)