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

from flask import Flask, url_for,request,render_template
app = Flask(__name__)

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
    return render_template('index.html', lines=linedb.get_lines())

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=9501,debug=True)

    with app.test_request_context():
        print(url_for('post/123'))
    ...
