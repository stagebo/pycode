#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description:   创建温度实时数据
"""
import db
import datetime
import os
import random
import json
db.open('pcems')

now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
if not os.path.exists('../log'):
    os.mkdir('../log')
file = open("../log/create_data_%s.txt"%now,'w')
def log(*k,sp=' ',end='\n'):
    print(k)
    global  file
    for i in k:
        file.write(i+sp)
    file.write(end)

def create_data():
    tablename = 'trd_2018_1_11_m'

    data_temp = {"data": [
        {"id": 36, "11001": 20.7, "11002": 18.1, "fault": 0},
        {"id": 37, "11001": 20.9, "11002": 16.3, "fault": 0},
        {"id": 38, "11001": 20.5, "11002": 11.7, "fault": 0},
        {"id": 39, "11001": 20.5, "11002": 11.7,"fault": 0},
        {"id": 40, "11001": 20.5, "11002": 11.7,"fault": 0},
        {"id": 41, "11001": 22.3, "11002": 34.7, "fault": 0},
        {"id": 42, "11001": 20.5, "11002": 11.7,"fault": 0},
        {"id": 43, "11001": 19.6, "11002": 11.1, "fault": 0},
        {"id": 44, "11001": 19.3, "11002": 10.7, "fault": 0},
        {"id": 45, "11001": 23.8, "11002": 12.4, "fault": 0},
        {"id": 46, "11001": 19.5, "11002": 10.8, "fault": 0},
        {"id": 47, "11001": 21.7, "11002": 14.7, "fault": 0},
        {"id": 48, "11001": 20.8, "11002": 10.6, "fault": 0},
        {"id": 49, "11001": 20.5, "11002": 11.7,"fault": 0},
        {"id": 50,"11001": 20.5, "11002": 11.7, "fault": 0},
        {"id": 51, "11001": 17.6, "11002": 12.7, "fault": 0},
        {"id": 52, "11001": 21.3, "11002": 10.1, "fault": 0},
        {"id": 53, "11001": 12.5, "11002": 13.4, "fault": 0}],
        "time": "2018-10-8 10:28:26"}

    now = datetime.datetime.now()
    ny,nm,nd = now.year,now.month,now.day
    for i in range(0,30):
        start = datetime.datetime(ny,nm,nd,0,0,0) - datetime.timedelta(days=i)
        e1,e2,e3 = 0,0,0
        st = 10
        en = 25
        for j in range(24*12):
            for idx in range(len(data_temp['data'])):
                e1 = random.randint(st,en)
                if j == 0:
                    e1, e2, e3 = 0, 0, 0
                data_temp['data'][idx]['11001'] = e1


            tk = start + datetime.timedelta(minutes=j*5)
            data_temp['time'] = str(tk)
            # jd = data_temp%(e1,e2,e3,tk)
            jd = json.dumps(data_temp)
            sql = "delete from %s where f_write_time = '%s';insert into %s (f_write_time,f_json_data) values('%s','%s')"%(tablename,tk,tablename,tk,jd)
            print(tk)
            print(sql)
            # db.execute(sql,())

if __name__ == "__main__":
    print("main")
    create_data()

    file.close()