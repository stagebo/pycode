#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     req
    Author:        wyb
    Date:          2018/9/23 0023
    Description:   模拟挖矿请求
"""
import requests
import  json
session = requests.session()

url = "http://localhost:5000/{}".format

def get(u,**kwargs):
    uri = url(u)
    print(uri)
    ret = requests.get(str(uri),kwargs)
    return ret.status_code,ret.json()

def post(u,data={},**kwargs):
    uri = url(u)
    print(uri)
    ret = requests.post(uri,data=data)
    return ret.status_code,ret.text

if __name__ == "__main__":
    # print(get('mine'))
    d = {
         "sender": "d4ee26eee15148ee92c6cd394edd974e",
         "recipient": "someone-other-address",
         "amount": 5
        }
    d = str(d)
    print(d)
    print(post('transactions/new',data=d))