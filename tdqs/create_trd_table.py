#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description:   创建实时数据表格
"""
import db
import datetime
import os
import random
db.open('phems')

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
    sls = [ i['f_station_id'] for i in db.query_dict("select * from public.t_energy_station")]
    dtypes = [i['f_device_type_id'] for i in db.query_dict("select * from public.td_device_type")]
    sql = """
    drop table if exists %s;
    create table %s (
      f_write_time timestamp not null primary key,
      f_json_data jsonb
    )
    """
    for sid in sls:
        for did in dtypes:
            tablename = "trd_2018_%s_%s_m"%(sid,did)
            db.execute(sql%(tablename,tablename))

if __name__ == "__main__":
    print("main")
    create_data()

    file.close()