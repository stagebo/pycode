#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     decorator_test
    Author:        WYB
    Date:          2018/11/12 13:16:41
    Description:   装饰器测试
"""
import json
import inspect
import psycopg2
import traceback
import psycopg2.extras
from functools import wraps
from enum import Enum, unique
from tornado.gen import coroutine
from jsonschema import validate, FormatChecker

def after1(func):
    def wrapper(something):  # 指定一毛一样的参数
        ret = func(something)
        print("[after]: after1 {}()".format(func.__name__))
        return ret
    return wrapper  # 返回包装过函数
def after2(func):
    def wrapper(something):  # 指定一毛一样的参数
        ret = func(something)
        print("[after]: after2 {}()".format(func.__name__))
        return ret
    return wrapper  # 返回包装过函数


def before(func):
    @after1
    @after2
    def wrapper(something):  # 指定一毛一样的参数
        print("[before]: enter {}()".format(func.__name__))
        return func(something)
    return wrapper  # 返回包装过函数

@before
def say(something):
    print("this is method body.")
    return "hello {}!".format(something)


if __name__ == "__main__":
    print(say(123))

