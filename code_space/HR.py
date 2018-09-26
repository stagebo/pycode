#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     req
    Author:        wyb
    Date:          2018/9/23 0023
    Description:   前端面试题
"""

import requests
# from bs4 import BeautifulSoup
import  uuid
ses = requests.session()
def get(url,header={},data={}):
    global ses
    header["User-Agent"]='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    header['Accept-Encoding'] = 'gzip, deflate, sdch'
    header['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
    header['Connection'] = 'keep-alive'
    response = ses.get(url,data=data,headers=header)
    print(url)
    print("Header===============================================================")
    for key in response.headers:
        print(key,":",response.headers[key])

    print("Data===============================================================")
    print(response.content)
    print()
    return response.content,response.headers

if __name__ == "__main__":
    url = 'http://118.24.120.229:3000/'
    get(url)

    url1 = 'http://118.24.120.229:3000/ADD7A65F-4EB6-4DAA-B543-B71EC7D95A59'
    get(url1)

    url2 = 'http://118.24.120.229:3000/DEFE2946-9C0C-40E5-8908-7151ED2AEE28'
    get(url2)

    url2 = 'http://118.24.120.229:3000/DD6FCD88-D456-426E-AE04-9BA7BDD44108'
    header = { 'referer':'DEFE2946-9C0C-40E5-8908-7151ED2AEE28'}
    get(url2,header=header,data=header)


    url2 = 'http://118.24.120.229:3000/3F220E04-A1B3-44AE-95A7-6E063BA4CFD5'
    ct,head = get(url2)
    keys = ''
    # keys = ''.join([div.contents[0] if(len(div.contents)==1) else '' for div in BeautifulSoup(ct.decode("utf8"),'lxml').find_all('div')])
    print('next page:',keys,'\r\n')


    url2 = 'http://118.24.120.229:3000/91C424FF-8826-4514-AAF9-F5A9DA07BD69'
    ct,head = get(url2)

# def get_content(content):
#     content = content.decode('utf8')
#     beautiful = BeautifulSoup(content,'lxml')
#     divs = beautiful.find_all('div')
#     contents_div = []
#     for div in divs:
#         cont = div.contents
#         if len(cont) == 1:
#             contents_div.append(cont[0])
#     result = ''
#     for cont in contents_div:
#         result += cont
#     return result





