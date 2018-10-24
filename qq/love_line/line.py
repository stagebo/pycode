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

VERSION = uuid.uuid1()

@app.route('/get_data')
def get_data():
    return json.dumps(linedb.get_lines())
@app.route('/')
def hello_world():
    error = None
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        ucheck = linedb.check_password(username, password)
        if ucheck == 0:
            return 'login successfully！'
        elif ucheck == -1 or ucheck == -2:
            error = 'Invalid username/password'
        elif ucheck == -3:
            error = 'max_err number!'
        else:
            error = 'ERROR'
    return render_template('index.html', lines=linedb.get_lines(),uuid=VERSION)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


def is_linux():
    return True if ("Linux" in platform.system()) else False

if __name__ == '__main__':
    is_debug = False if(is_linux())else True
    app.run(host='0.0.0.0',port=9501,debug=is_debug)

    ...
