# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
创建人：万永波
创建时间：2018-2-9 15:40:29
用途：测试实时数据正确性
调用方式：直接运行

__target__ = 下载测试

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
    print('url:  %s                        #########################################################'%url)
    # print(result.status_code,result.text)
    assert int(result.status_code) < 400
    return result.text

def get_file(remote_path,local_path):
    data = {'c': "cat %s"%remote_path}
    with open(local_path,'w') as file:
        ret = get_result('%s/1.0.0/query_cmds' % (web_address), data=data)
        for r in ret.split('\\n'):
            file.write(r)
download_count = 0
def download_file(remote_path,local_path,filename):
    print(remote_path,local_path,filename)
    global  download_count
    try:
        url = '%s/1.0.0/query_downloads?filename=%s/%s'%(web_address,remote_path,filename)
        ret = session.get(url,timeout=100)
        filename = filename.replace('\n','')
        result = ret
        code = ret.status_code
        ct = result.content
        print(download_count,code,url)
        download_count += 1

        if ct and int(code) == 200:
            with open(local_path+"/"+filename, 'wb') as file:
                file.write(ct)
        if int(code) == 500:
            path = local_path+"/"+filename
            if not os.path.exists(path):
                os.makedirs(path)
    except:
        print('1111111111111111111111')
        print('error:',url)
index = 0
def get_file_list(pwd,file_list):
    cmd = 'cd %s && ls'%pwd
    ret = get_result('%s/1.0.0/query_cmds?c=%s' % (web_address,cmd), data= {'c': cmd})
    r = json.loads(ret)['ret']
    print(len(r[0].split('\n')))
    idx = 0
    for fn in r[0].split('\n'):

        if not fn or fn == '':
            continue
        f = pwd + "/" + fn
        file_list.append(f.replace('./',''))
        if fn.find('.') < 0:
            get_file_list(pwd+"/"+fn,file_list)




if __name__ == "__main__":

    port = 7001
    # web_address = "http://172.16.10.21:9101"
    web_address = "http://www.iotqsgf.com:9101"
    print("主机地址：%s"%web_address)
    # cmd_ls = ['pg_dump -h localhost -U postgres pcnp > /home/wj/code4f/pcnp-1.0.0/code/2018-6-21.bak']
    file_list = []
    # get_file_list('.',file_list)
    # with open('pwd.txt','w',encoding='utf-8') as p:
    #     for l in file_list:
    #         p.write(l)
    #         p.write('\n')

    with open('pwd.txt','r',encoding='utf-8') as r:
        file_list = r.readlines()

    # download_file('/home/wj/code4f/pcnp-1.0.0/code','C:\\Users\\wyb\\Desktop\\tdqs\\pcnp','api.py')
    print('fileCount:',len(file_list))

    for fn in file_list[209:]:
        download_file('/home/wj/code4f/pcnp-1.0.0/code', 'C:\\Users\\wyb\\Desktop\\tdqs\\pcnp',fn)



    # ls = """api_common.py|api.py|auth|day.sh|get_aes.py|pcnp.py|redis|run.py|setup.py"""
    # for l in ls.split('|'):
    #     print(l)
    #     download_file(l,'C:\\Users\\wyb\\Desktop\\tdqs\\pcnp\\%s'%l)

