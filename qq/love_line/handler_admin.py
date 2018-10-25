#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     handler_admin
    Author:        wyb
    Date:          2018/10/23 0023
    Description:   管理员后台
"""

from flask import Flask, url_for,request,render_template
import line
@line.app.route('/abc')
def abc():
    return "abc"