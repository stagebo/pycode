#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description:   创建电量实时数据
"""
import db
import datetime
import os
import random
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
    tablename = 'trd_2018_2_1_m'
    tablename = 'trd_2018_1_1_m'
    data_temp = '''
   {"data": [{"id": 30, "1001": 84888.0, "1004": 84888.0, "1005": %s, "1006": 0.0, "1007": 0.0, "1008": 26.0, "1009": 235.7, "1010": 235.7, "1011": 232.9, "1012": 0.0, "1013": 0.0, "1014": 0.0, "1015": 0.0, "1017": 50.0, "1018": 0.0, "1019": 0.0, "1020": 0.0, "fault": 0},{"id": 31, "1001": 39766.0, "1004": 39766.0, "1005": %s, "1006": 0.4, "1007": 0.0, "1008": 348.0, "1009": 235.5, "1010": 235.6, "1011": 232.8, "1012": 3.2, "1013": 3.2, "1014": 0.0, "1015": 0.0, "1017": 50.01, "1018": 0.0, "1019": 0.0, "1020": 0.0, "fault": 0}, {"id": 32, "1001": 211592.0, "1004": 211592.0, "1005":%s, "1006": 74.4, "1007": 40.4, "1008": 25632.0, "1009": 234.8, "1010": 234.7, "1011": 231.8, "1012": 120.4, "1013": 128.8, "1014": 116.8, "1015": 0.877, "1017": 50.0, "1018": 23.6, "1019": 26.4, "1020": 24.0, "fault": 0}], "time": "%s"}
    '''
    data_temp = """
    {"data": [{"id": 34, "1001": 84888.0, "1004": 84888.0, "1005": %s, "1006": 0.0, "1007": 0.0, "1008": 26.0, "1009": 235.7, "1010": 235.7, "1011": 232.9, "1012": 0.0, "1013": 0.0, "1014": 0.0, "1015": 0.0, "1017": 50.0, "1018": 0.0, "1019": 0.0, "1020": 0.0, "fault": 0},{"id": 35, "1001": 39766.0, "1004": 39766.0, "1005": %s, "1006": 0.4, "1007": 0.0, "1008": 348.0, "1009": 235.5, "1010": 235.6, "1011": 232.8, "1012": 3.2, "1013": 3.2, "1014": 0.0, "1015": 0.0, "1017": 50.01, "1018": 0.0, "1019": 0.0, "1020": 0.0, "fault": 0}], "time": "%s"}
    """
    now = datetime.datetime.now()
    ny,nm,nd = now.year,now.month,now.day
    for i in range(0,30):
        start = datetime.datetime(ny,nm,nd,0,0,0) - datetime.timedelta(days=i)
        e1,e2,e3 = 0,0,0
        st = 50
        en = 100
        if i%7==2:
            st = 80
        for j in range(24*12):
            e1 += random.randint(st,en)
            e2 += random.randint(st,en)
            e3 += random.randint(st,en)
            if j == 0:
                e1,e2,e3 = 0,0,0
            tk = start + datetime.timedelta(minutes=j*5)
            # jd = data_temp%(e1,e2,e3,tk)
            jd = data_temp%(e1,e2,tk)
            sql = "delete from %s where f_write_time = '%s';insert into %s (f_write_time,f_json_data) values('%s','%s')"%(tablename,tk,tablename,tk,jd)
            print(tk)
            db.execute(sql,())

if __name__ == "__main__":
    print("main")
    db.execute("delete from %s where f_write_time > %s"%("trd_2018_1_1_m",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),())
    # create_data()

    file.close()