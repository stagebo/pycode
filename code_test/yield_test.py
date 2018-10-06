#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     yield_test
    Author:        wyb
    Date:          2018/10/6 0006
    Description:   yield 使用测试
"""

def fab(max_n):
    n,a,b = 0,0,1
    while b < max_n:
        m = yield a
        print(m)
        a,b,n = b,a+b,n+1
if __name__ == "__main__":
    x = fab(10)
    print(dir(x))
    print(x.__next__())
    # print(x.send(8))
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())