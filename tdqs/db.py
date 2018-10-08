#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     pdb
    Author:        wyb
    Date:          2018/9/24 0024
    Description:   连接postgresql数据库
"""

import psycopg2
import configparser
import read_conf
cf = configparser.ConfigParser()
cf.read("../application.conf")
rt = read_conf.read_config(cf)

dbhost = rt['host']
port = rt['port']
dbname = rt['dbname']
user=rt['user']
pwd = rt['pwd']
conn = psycopg2.connect(database=dbname, user=user, password=pwd, host=dbhost, port=port)
def open(dbname):
    global conn
    conn = psycopg2.connect(database=dbname, user=user, password=pwd, host=dbhost, port=port)




def execute(sql,*args, **kwargs):
    cur = conn.cursor()
    cur.execute(sql,args)
    # print("Table created successfully")
    conn.commit()
    return cur

def query_dict(sql,*args, **kwargs):
    print(args,kwargs)
    refdata = []
    try:
        cursor = conn.cursor()
        # print(dir(cursor))
        cursor.execute(sql,args,)
        refdata = [dict((cursor.description[i][0], str(value)) for i, value in enumerate(row)) for row in cursor.fetchall()]
    except psycopg2.Error as e:
        conn.rollback()
        print(e)
        return None
    finally:
        pass
    return refdata

def query(sql,*args, **kwargs):
    cur = conn.cursor()
    cur.execute(sql,*args, **kwargs)
    ret = []
    for row in cur:
        ret.append(row)
    conn.commit()

    return ret

if __name__ == "__main__":
    # print(query_dict("select * from system.t_grid_info where f_area_id = %s",[3]))
    print(query_dict("select * from system.t_grid_info where f_area_id = %s and f_grid_id = %s",[3,"S_6501020000000000000003003"]))
