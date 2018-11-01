#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     menu
    Author:        wyb
    Date:          2018/10/25 0025
    Description:   
"""
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

path = []
while True:
    m = menu
    for p in path:
        m = m[p]
    citys = m.keys()
    print('\n'.join(citys))
    choice = input("-->>").strip()
    if choice =='back':
        if path:path.pop()
    elif choice=='q': break
    elif choice in citys:path.append(choice)



