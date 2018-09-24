#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     req
    Author:        Administrator
    Date:          2018/7/20
    Description:   
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
__author__ = 'Administrator'
import requests
session = requests.session()

def get_result(url,data={},header={}):
    result = session.get(url,data=data,headers=header)
    print('url:  %s    ===================================================================================' % url)
    # print(result.status_code,result.text)
   # assert int(result.status_code) < 400
    return result.text,result.status_code

def post_result(url,data={}):
    result = session.post(url,data)
    print('url:  %s    ===================================================================================' % url)
    print(result.status_code, result.text)
    # assert int(result.status_code) < 400
    return result.text

def post_file(url,data,files={}):
    print('url:  %s    ===================================================================================' % url)
    result = session.request('post', url,
            params=None, data=data, headers=None, cookies=None, files=files,
            auth=None, timeout=5, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None)
    print(result.status_code, result.text)
    # assert int(result.status_code) < 400
    return result.text

def get_download(url,data,fn):
    if not fn:
        print("文件名不能为空")
    print('url:  %s    ===================================================================================' % url)
    result = session.get(url,data=data)
    print(result.status_code,'download file %s succeed!')
    if int(result.status_code) < 400:
        ct = result.content
        with open(fn,'wb') as file:
            file.write(ct)

if __name__ == "__main__":
    ret,code = get_result('http://www.360doc.com/content/13/0722/22/998704_301833252.shtml')
    # print(ret)
    txt = ret[ret.find('旧历的'):ret.find('二月七日')+4]
    with open('../data/祥林嫂.txt','w',encoding='utf8') as tx:
        tx.write(txt)