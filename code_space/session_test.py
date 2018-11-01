#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     session_test
    Author:        wyb
    Date:          2018/10/26 0026
    Description:   测试Session实现
"""

import json
from flask import Flask, url_for,request,render_template,make_response,send_file,session
import uuid
import qrcode
from datetime import *
from io import BytesIO
import os
import vcode
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。


@app.route('/get_vcode')
def get_vcode():
    v = vcode.get_str(4)
    img = vcode.get_img(v)

    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)

    session["vcode"] = v
    return send_file(byte_io, mimetype='image/png')

@app.route('/validate_vcode')
def validate_vcode():
    vs = request.args.get("vcode",None)
    vd = session.get("vcode",None)
    print(vs,vd)
    if not vd or str(vd).lower() != str(vs).lower():
        return "False"
    del session['vcode']
    return "True"

@app.route('/get_qrcode')
def get_qrcode():
    qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=1)
    qr.add_data("17684117493")
    img = qr.make_image()

    byte_io = BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png')

@app.route('/')
def hello_world():
    session_id = request.cookies.get("SessionID",None)
    if session_id:
        msg = "大爷您是老顾客"
    else:
        msg = "大爷您第一次"
    print(msg,session_id)
    response = make_response(msg);
    response.set_cookie('SessionID', str(uuid.uuid1()))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6001,debug=True)

