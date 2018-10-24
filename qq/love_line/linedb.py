#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     udb
    Author:        wyb
    Date:          2018/10/23 0023
    Description:   模拟数据库
"""
import datetime

# 最大密码错误次数
MAX_ERROR_TIME = 3


users = {
    'qq':{
        'username':'qq',
        'pwd':'123',
        'err_count':0,
        'last_login_time':None
    }
}

def user_exist(username):
    return True if(username in users.keys())else False

def get_user(username):
    return users[username] if(username in users.keys())else False

def get_user_list():
    return [users[k] for k in users.keys()]

def check_password(username,password):
    if username not in users.keys():
        return -1
    if users[username]['err_count'] >= MAX_ERROR_TIME:
        return -3
    if str(password) !=  users[username]['pwd']:
        users[username]['err_count'] += 1
        return -2
    users[username]['err_count'] = 0
    users[username]['last_login_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return 0

def add_user(username,password):
    if username in users.keys():
        return False
    users[username] = {'username': username, 'pwd': password, 'err_count': 0, 'last_login_time': None    }
    return True

def delete_user(username):
    if username in users.keys():
        del users[username]
        return True
    return False

def update_password(username,password):
    if username not in users.keys():
        return False
    users[username]['pwd'] = password
    return True

lines = [
    {
        'title':'大连飞天津',
        'content':'秋秋来天津旅游',
        'href':'#',
        'date':'2017-5-28'
    },{
        'title':'天津飞大连',
        'content':'波波去大连接秋秋毕业',
        'href':'#',
        'date':'2017-6-22'
    },{
        'title':'大连飞天津',
        'content':'一起飞天津，一起毕业',
        'href':'#',
        'date':'2017-6-27'
    }
]

lines = sorted(lines, key=lambda line: line['date'])

def get_lines():
    return lines

if __name__ == "__main__":
    print(check_password('qq', '123'))
    print("main")