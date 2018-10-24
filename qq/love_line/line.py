#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     main
    Author:        wyb
    Date:          2018/10/23 0023
    Description:   line 启动页面
"""
import linedb
import json
import datetime
import uuid
import platform


from flask import Flask, url_for,request,render_template
app = Flask(__name__)

VERSION = datetime.datetime.strftime("%Y%m%d%H%M%S")

@app.route('/get_data')
def get_data():
    return json.dumps(linedb.get_lines())

@app.route('/')
def get_lines():
    return render_template('index.html', lines=linedb.get_lines(),uuid=VERSION)

@app.route('/all')
def get_lines_all():
    return render_template('line_all.html', lines=linedb.get_lines_all(),uuid=VERSION)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


def is_linux():
    return True if ("Linux" in platform.system()) else False

if __name__ == '__main__':
    is_debug = False if(is_linux())else True
    app.run(host='0.0.0.0',port=9501,debug=is_debug)
