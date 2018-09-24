#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/6/30'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃       ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import db
import pandas as pd
class TranspositionTable():
    def __init__(self):
        pass

def _table_exists( schemename, tablename):
    sql = "select count(*) from pg_tables where schemaname = '%s' and tablename = '%s'" % (
    schemename.lower(), tablename.lower())
    ret = db.query_dict(sql)
    if int(ret[0]["count"]) < 1:
        return False
    return True
def deal_2_tae_gmjjlshqk():
    db.execute('drop table zhl_business.tae_gmjjlshqk_transposition')
    schemaname = "zhl_business"
    table_name = "tae_gmjjlshqk"
    tn_p = table_name+'_transposition'
    if not _table_exists(schemaname,tn_p):
        sql = """
        create table %s.%s (
        f_item varchar(128),
        f_2013 varchar(32),
        f_2014 varchar(32),
        f_2015 varchar(32),
        f_2016 varchar(32),
        f_2017 varchar(32)
        )
        """%(schemaname,tn_p)
        print(sql)
        db.execute(sql)
    exp = db.query_dict("select f_name,f_cname from %s.%s_exp order by f_order" % (schemaname, table_name))
    fields = [i.get("f_name").lower() for i in exp]
    cnames = [i.get("f_cname").lower() for i in exp]

    data = db.query("select %s from %s.%s"%(','.join(fields),schemaname,table_name))
    data_new = []
    fields_new = ['f_item','f_2013','f_2014','f_2015','f_2016','f_2017']

    for i in range(len(data[0])):
        item = []
        for j in range(len(data)):
            item.append(data[j][i])
        data_new.append(item)
    for i in range(len(fields)):

        data_new[i] =  [cnames[i]]+list(data_new[i])
    print('data new :')
    sql_i = """
           insert into %s.%s (%s) values (%s);
           """
    sql_list = []
    for i in data_new:
        print(i)
        sql_list.append(sql_i%(
            schemaname,tn_p,','.join(fields_new),','.join(["'%s'"%k for k in i])
        ))
    for s in sql_list:
        print(s)
    db.execute(''.join(sql_list))
if __name__ == "__main__":
    print("main")
    deal_2_tae_gmjjlshqk()