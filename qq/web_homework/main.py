#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     main
    Author:        wyb
    Date:          2018/10/23 0023
    Description:   web 启动页面
"""
import udb
import json

from flask import Flask, url_for,request,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/delete/user/<int:post_id>')
@app.route('/user/delete/<username>',methods=['GET'])
def delete_user(username):
    # show the post with the given id, the id is an integer
    return "success" if(udb.delete_user(username)) else "error"

@app.route('/user/add',methods=['POST'])
def add_user():
    username, password = request.form['username'], request.form['password']
    return "success" if(udb.add_user(username,password)) else "error"

@app.route('/user/update',methods=['POST'])
def update_password():
    password = request.form['password']
    return "success" if(udb.update_password(password)) else "error"

@app.route('/user/get/<username>',methods=['GET'])
def get_user(username):
    return json.dumps(udb.get_user(username))


@app.route('/user/list',methods=['GET'])
def get_users():
    return json.dumps(udb.get_user_list())

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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=6001,debug=True)

    with app.test_request_context():
        print(url_for('post/123'))
    ...
