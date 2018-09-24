# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Description: 测试脚本

'''
import json
import requests

web_address = "http://localhost:8888"
session = requests.Session()



def get_result(url,data={}):
    print('url:  %s                        #########################################################'%url)
    result = session.get(url,data=data)
    print(result.status_code,result.text)
    assert int(result.status_code) < 400
    return result.text

def post_result(url,data):
    print('url:  %s                        #########################################################' % url)
    result = session.post(url,data)
    print(result.status_code, result.text)
    assert int(result.status_code) < 400
    return result.text

def post_file(url,data,files={}):
    print('url:  %s                        #########################################################' % url)
    result = session.request('get', url,
            params=None, data=data, headers=None, cookies=None, files=files,
            auth=None, timeout=50, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None)
    print(result.status_code, result.text)
    assert int(result.status_code) < 400
    return result.text

if __name__ == "__main__":
    port = 7001
    print("主机地址：%s"%web_address)

    # 1
    get_result('%s/1.0.0/query_xq_list' % web_address)
