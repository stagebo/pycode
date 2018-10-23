#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     main
    Author:        wyb
    Date:          2018/10/23 0023
    Description:   web 启动页面
"""
import udb

from flask import Flask, url_for,request,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username,password = request.form['username'], request.form['password']
        ucheck = udb.check_password(username,password)
        if ucheck == 0:
            return 'login successfully！'
        elif ucheck == -1 or ucheck == -2:
            error = 'Invalid username/password'
        elif ucheck == -3:
            error = 'max_err number!'
        else:
            error = 'ERROR'
    return render_template('login.html', error=error)

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=6001,debug=True)

    with app.test_request_context():
        print(url_for('post/123'))
    ...
