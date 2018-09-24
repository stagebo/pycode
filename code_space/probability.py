#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     probability
    Author:        wyb
    Date:          2018/9/20 0020
    Description:   给定一个返回1和0的概率分别是p和1-p的函数，求实现一个返回0和1概率一样的函数
"""
__author__ = 'wyb'
import random


def sf(p=0.3):
    '''
    该函数返回0的概率为p，返回1的概率为1-p
    :return:
    '''
    rt = random.random()
    return 1 if(rt>p) else 0

def df():
    '''
    要求调用sf函数，并返回0和1的概率各位0.5
    :return:
    '''
    while True:
        ret = sf(),sf()
        if ret == (0,1):
            return 0
        elif ret == (1,0):
            return 1


if __name__ == "__main__":
    n0,n1 = 0,0
    for i in range(0,1000):
        r = sf()
        if r == 1:
            n1 += 1
        else :
            n0 += 1
        # print(r,end=' ')
    print()
    print(n0,n1)

    n0, n1 = 0, 0
    for i in range(0, 1000):
        r = df()
        if r == 1:
            n1 += 1
        else:
            n0 += 1
        # print(r, end=' ')
    print()
    print(n0, n1)