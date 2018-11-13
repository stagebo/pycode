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
cf.read("../application.conf",encoding='utf-8')
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


def execute(sql,args, **kwargs):
    cur = conn.cursor()
    cur.execute(sql,args)
    conn.commit()
    return cur

def query_dict(sql,args=()):
    try:
        cursor = conn.cursor()
        cursor.execute(sql, args)
        refdata = [dict((cursor.description[i][0], str(value)) for i, value in enumerate(row)) for row in
                   cursor.fetchall()]
    except psycopg2.Error as e:
        conn.rollback()
        return None
    return refdata

def fetchall(sql,args=()):
    cur = conn.cursor()
    cur.execute(sql,args)
    return cur.fetchall()

def fetchone(sql,args=()):
    cur = conn.cursor()
    cur.execute(sql,args)
    return cur.fetchone()

def fetchmaney(sql,args=()):
    cur = conn.cursor()
    cur.execute(sql,args)
    return cur.fetchmany()

def query(sql,args):
    cur = conn.cursor()
    cur.execute(sql,args)
    ret = []
    for row in cur:
        ret.append(row)
    conn.commit()
    return ret
def get_sql(sql="", args=()):
    cur = conn.cursor()
    return cur.mogrify(sql, args)


if __name__ == "__main__":
    cur = conn.cursor()
    print('\n'.join(dir(cur)))
    # print(query_dict("select * from system.t_grid_info where f_area_id = %s",[3]))
    print(query_dict("select * from system.t_grid_info "))
    print(query_dict("select * from system.t_grid_info where f_grid_id = 'S_6501020000000000000003003' or f_grid_id = %s",("S0001_201809050842131000001",)))
    print(query_dict("select * from system.t_grid_info where  f_grid_id = 'S_6501020000000000000003003' or f_grid_id = %s",("S0001_201809050842131000001'",)))
    print(get_sql("select * from system.t_grid_info where  f_grid_id = 'S_6501020000000000000003003' or f_grid_id = %s",("S0001_201809050842131000001'",)))
