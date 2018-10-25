#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     height_light
    Author:        wyb
    Date:          2018/10/25 0025
    Description:   打印各种颜色的样式
"""
# 红色字体
print('\033[1;31m')
print('*'*10)
print('hello world！')
print('*'*10)
print('\033[0m')
# 绿色字体
print('\033[1;32m' + 'green' + '\033[0m')
 
# 蓝色字体
print('\033[1;34m' + 'blue' + '\033[0m')
 
# 黄字下划线
print('\033[4;33m' + 'yellow' + '\033[0m')
 
# 红底黑字
print('\033[1;30;41m' + 'black' + '\033[0m')
 
# 白底黑字
print('\033[1;30;47m' + 'white' + '\033[0m')
 
print('normal')

if __name__ == "__main__":
    print("main")