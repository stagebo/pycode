#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/7/9'
__target__ 清除数据库垃圾数据
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
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
import datetime
import os
now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
if not os.path.exists('../log'):
    os.mkdir('../log')
file = open("../log/%s.txt"%now,'w')
def log(*k,sp=' ',end='\n'):
    print(k)
    global  file
    for i in k:
        file.write(i+sp)
    file.write(end)

def clear_data():
    sl = "public,postgis,xzh_view,xzh_business,zhl_view,zhl_business,fhyc_view,fhyc_business".split(',')
    sql = """
           select * from system.t_grid_info
           """
    ret = db.query_dict(sql)
    slist = [i['f_grid_id'] for i in ret]
    for sc in sl:
        sql = "select tablename from pg_tables where schemaname = '%s'"%sc
        ret = db.query_dict(sql)
        tlist = [i['tablename'] for i in ret]
        for t in tlist:
            if t.endswith('_exp'):
                continue
            sql = """
            SELECT DISTINCT 
            a.attname AS field
            FROM pg_class c,
            pg_attribute a
            WHERE c.relname = '%s'
            and a.attnum > 0
            and a.attrelid = c.oid

            """%t
            expret = db.query_dict(sql)
            if not expret:
                expret = db.query_dict("select tablename from %s.%s_exp"%(sc,t))
            if not expret:
                log('table 【%s. %s】 does not has exp data'%(sc,t))
                # log(sql)
                continue
            gchid_name = None
            for r in expret:
                f_name = r['field'].lower()

                if f_name == 'f_sid' or f_name == 'f_subgchid' or f_name == 'sid':
                    gchid_name = f_name
            if not gchid_name:

                log('table 【%s.%s】 has no sid,continue!'%(sc,t))
                continue
            log(sc,t,gchid_name)
            sql = "delete from %s.%s where %s not in (%s)"%(sc,t,gchid_name,','.join(["'%s'"%i for i in slist]))
            try:
                ret = db.execute(sql)
                log('delete table 【%s.%s】,changed rows 【%s】'%(sc,t,ret))
            except:
                log('【error】 %s,%s'%(sc,t))

if __name__ == "__main__":
    print("main")
    clear_data()

    file.close()