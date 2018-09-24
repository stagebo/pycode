# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
创建人：stagebo
创建时间：2018-2-9 15:40:29
用途：测试实时数据正确性
调用方式：直接运行

'''

'''
__target__ = 
'''
import json
import requests
import configparser
import sys
import datetime
import os

session = requests.Session()

web_address = "http://www.iotqsgf.com:9101"
def get_result(url,data={}):
    result = session.get(url,data=data,timeout=99999)
    # print('url:  %s                        #########################################################'%url)
    # print(result.status_code,result.text)
    assert int(result.status_code) < 400
    return result.text

index = 0
def get_file_list(pwd,file_list,file):
    cmd = 'cd %s && ls'%pwd
    ret = get_result('%s/1.0.0/query_cmds?c=%s' % (web_address,cmd), data= {'c': cmd})
    r = json.loads(ret)['ret']
    # print(len(r[0].split('\n')))
    idx = 0
    for fn in r[0].split('\n'):

        if not fn or fn == '':
            continue
        f = pwd + "/" + fn
        f = f.replace('//','/')
        file_list.append(f)
        print(f)
        file.write(f)
        file.write('\n')
        file.flush()
        if fn.find('.') < 0:
            get_file_list(pwd+"/"+fn,file_list,file)




if __name__ == "__main__":

    web_address = "http://www.iotqsgf.com:9101"
    print("主机地址：%s"%web_address)
    file_list = []

    with open('../data/pwd_data.txt','w',encoding='utf-8') as file:
        get_file_list('/',file_list,file)


