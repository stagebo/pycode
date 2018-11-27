#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     exam_test
    Author:        wyb
    Date:          2018/11/17 0024
    Description:   examsystem 测试脚本
"""
import json
import requests
import sys,io

url = 'http://exam.urmyall.xyz:9701/{}'.format

url = 'http://localhost:9701/{}'.format
def token(func):
    def wapper(*args, **kwargs):
        if args[0].token is None:
            args[0].login()
        return func(*args, **kwargs)
    return wapper


class Test:

    def __init__(self):
        self.token = None

    def login(self):
        u = url('api/log/login')
        print('login',u)
        tk = requests.post(u,data={'username': "admin", 'password': '123'})
        print(tk,tk.status_code,tk.text)
        self.token = json.loads(tk.text)["data"]['token']

    # @token
    def get(self, api, **kw):
        print(url(api))
        ret = requests.get(url(api), params=kw, headers={"Session-Token": self.token})
        text = ret.text
        try:
            text = json.load(ret.text)
        except:
            pass
        return text, ret.status_code

    # @token
    def post(self, api, data={}):
        print(url(api))
        ret = requests.post(url(api), data=data, headers={"Session-Token": self.token})
        text = ret.text
        try:
            text = json.load(ret.text)
        except:
            pass
        return text, ret.status_code

    def post_file(self,api,data, files={}):
        print('url:  %s    ===================================================================================' % url)
        session = requests.session()
        result = session.request('post', url(api),
                                 params=None, data=data, headers=None, cookies=None, files=files,
                                 auth=None, timeout=5, allow_redirects=True, proxies=None,
                                 hooks=None, stream=None, verify=None, cert=None, json=None)

        try:
            text = json.load(result.text)
        except:
            pass
        return result.text, result.status_code

if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='GBK')
    # print(Test().get('query_t')) # ERROR ID
    T = Test()
    T.login()
    # print(T.get('api/log/islogin'))
    # print(T.post('api/log/logout'))
    print(T.post("api/sms/send",data={"examid":"dca520c4-64d7-427b-af3b-adb385174362"}))
    # print(T.post('api/exam/bindfile',data={"examid":"4091b56e-01b6-490f-9c57-f30720f5667c","fileid":"8d3bb348-3609-4bf1-93da-256e29d298a2"}))
    # print(T.get('api/exam/files',examid = "4091b56e-01b6-490f-9c57-f30720f5667c"))

    # files = {"file": open('F:\\Users\\WYB\\Desktop\\经济社会信息.xls', 'rb')}
    # print(T.post_file('api/common/upload', data={}, files=files))

    # print(T.get('api/log/islogin'))
    # print(T.post('api/sys/loginuser'))
    #
    # print(T.post('api/user/add',data={"username":"admin","truename":"系统管理员","password":"123","idnumber":123123,'role':1}))
    # print(T.post('api/role/add',data={'name':'主任1','num':'6'}))
    # print(T.post('api/campus/add',data={'name':'主校区','address':'津南区'}))
    # print(T.post('api/college/add',data={'name':'法学院1'}))
    # print(T.post('api/course/add',data={'name':'马克思主义哲学',"collegeid":"13c01153-6c48-4c16-a856-899d528a46f6","capacity":21}))
    # print(T.post('api/grade/add',data={'name':'2015级',"collegeid":"13c01153-6c48-4c16-a856-899d528a46f6"}))
    # print(T.post('api/room/add',data={'name':'23楼A304',"address":"23楼"}))
    # print(T.post('api/tclass/add',data={'name':'自动化二班',"gradeid":"9f3ecf03-980b-4202-9c36-7f0ad891b50f","collegeid":"79842b7a-788f-4845-8acb-b091e190adfa"}))
    # print(T.post('api/exam/add',data={'name':'自动化二班',"gradeid":"9f3ecf03-980b-4202-9c36-7f0ad891b50f","collegeid":"79842b7a-788f-4845-8acb-b091e190adfa"}))



    # print(T.post('api/user/modify',data={"id":"dffcdd9d-08c1-4665-a9f1-04997a53f3ba","username":"www","truename":"www1","password":"123","idnumber":"123123"}))
    # print(T.post('api/role/modify', data={"id":"557cd8c5-dc36-4f3b-8dec-bcb548148d75","name":"主任"}))
    # print(T.post('api/campus/modify', data={"id":"79d251ad-59e2-4636-9175-898f867c2eb8","name":"主校区1","address":"123123123"}))
    # print(T.post('api/college/modify', data={"id":"79842b7a-788f-4845-8acb-b091e190adfa","name":"理学院1"}))
    # print(T.post('api/course/modify', data={"id":"967b3d71-55db-41f5-bfe1-cc4944bf82ba","name":"激光原理","capacity":22}))
    # print(T.post('api/grade/modify', data={"id":"89f50cb3-9510-46b2-9bbe-c7af423f9f1d","collegeid":"13c01153-6c48-4c16-a856-899d528a46f6","name":"2019级"}))
    # print(T.post('api/room/modify', data={"id":"587b6100-3aa7-4d37-a694-06fd8cd7fb7d","address":"24楼"}))
    # print(T.post('api/tclass/modify', data={"id":"99536e78-f5b5-45c7-b50b-8109b910753a","gradeid":"9f3ecf03-980b-4202-9c36-7f0ad891b50f","collegeid":"79842b7a-788f-4845-8acb-b091e190adfa","name":"自动化二班"}))
    # print(T.post('api/exam/modify', data={"id":"d52f38c7-4d37-405c-8e1b-af6ad78bad1c", "gradeid":"9f3ecf03-980b-4202-9c36-7f0ad891b50f",  "collegeid":"79842b7a-788f-4845-8acb-b091e190adfa","name":"自动化二班", "time":"2020-12-23 12:23"}))

    # print(T.post('api/user/remove',data={"id":"7769d0a6-1fc9-45f9-9add-e68421d54436"}))
    # print(T.post('api/role/remove', data={"id": "1f560bb7-2e7e-46a7-80f4-f193465498f2"}))
    # print(T.post('api/campus/remove', data={"id": "3b446cae-1cd9-4c26-a4c2-2333ba85af80"}))
    # print(T.post('api/college/remove', data={"id": "e65ab1a5-d93c-4071-9f80-563073c325fa"}))
    # print(T.post('api/course/remove', data={"id": "5601b503-1420-45a6-b28e-adaa14bfec43"}))
    # print(T.post('api/grade/remove', data={"id": "5c00eec8-c39e-4098-903c-11b141396309"}))
    # print(T.post('api/room/remove', data={"id": "b73b5bc5-d19f-45cc-98c8-17d449c290a5"}))
    # print(T.post('api/tclass/remove', data={"id": "b73b5bc5-d19f-45cc-98c8-17d449c290a5"}))
    # print(T.post('api/exam/remove', data={"id": "b73b5bc5-d19f-45cc-98c8-17d449c290a5"}))


    #
    # print(T.get('api/user/get',id="dffcdd9d-08c1-4665-a9f1-04997a53f3ba"))
    # print(T.get('api/role/get', id="557cd8c5-dc36-4f3b-8dec-bcb548148d75"))
    # print(T.get('api/campus/get', id="79d251ad-59e2-4636-9175-898f867c2eb8"))
    # print(T.get('api/college/get', id="13c01153-6c48-4c16-a856-899d528a46f6"))
    # print(T.get('api/course/get', id="967b3d71-55db-41f5-bfe1-cc4944bf82ba"))
    # print(T.get('api/grade/get', id="43beb85d-4922-48fe-af47-958e842abc47"))
    # print(T.get('api/room/get', id="587b6100-3aa7-4d37-a694-06fd8cd7fb7d"))
    # print(T.get('api/tclass/get', id="9b00618c-ae72-4ce5-a772-94c6280b5fd2"))
    # print(T.get('api/exam/get', id="9b00618c-ae72-4ce5-a772-94c6280b5fd2"))
    #
    #
    #
    # print(T.get('api/user/count'))
    # print(T.get('api/role/count'))
    # print(T.get('api/user_role/count'))
    # print(T.get('api/exam/count'))
    # print(T.get('api/tclass/count'))
    # print(T.get('api/grade/count'))
    # print(T.get('api/campus/count'))
    # print(T.get('api/college/count'))
    #
    # print(T.get('api/user/list'))
    # print(T.get('api/role/list'))
    # print(T.get('api/user_role/list'))
    # print(T.get('api/exam/list'))
    # print(T.get('api/tclass/list'))
    # print(T.get('api/grade/list'))
    # print(T.get('api/campus/list'))
    # print(T.get('api/college/list'))