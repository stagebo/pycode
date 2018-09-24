#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File Name:     ssh_cmd
    Author:        wyb
    Date:          2018/7/12
    Description:   服务器密码，这个好玩，参考目录下sec.txt 和 users.txt 文件
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

cmd_ls = [
    'newusers users.txt'
]
cmd_ls = ['/usr/sbin/pwunconv',
          'chpasswd < sec.txt',
          'pwconv'
          ]
cmd_ls = [
            # 'newusers users.txt',
            # '/usr/sbin/pwunconv',
            # 'chpasswd < sec.txt',
            # 'pwconv',
            # 'cat /etc/passwd'
              ]