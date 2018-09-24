#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__target__ =  生成GEOMJSON文件
__mtime__ = '2018/6/30'
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
import json
import traceback
# print(db.query_dict("select wkb_geometry from xzh_view.大区"))

if __name__ == "__main__":
    sc = "xzh_view"
    sql = "select tablename from pg_tables where schemaname = '%s'"%sc
    ret = db.query_dict(sql)

    for r in ret:

        try:
            tablename = r['tablename']
            sql = "select * from %s.%s"%(sc,tablename)
            data = db.query_dict(sql)

            features = []
            for d in data:
                geom = d['wkb_geometry']
                del d['wkb_geometry']
                fea = {
                    "type":"Feature",
                    "properties":d,
                    "geometry":geom
                }
                features.append(fea)
            print(tablename + "  success")
        except:
            traceback.print_exc()
            print(tablename+"  error")
        jd = {"type": "FeatureCollection", "features": features}
        filename = "geomjson/%s.json"%tablename
        with open(filename, 'w') as fl:
            fl.write('{')
            fl.write(json.dumps(jd))
            fl.write('{')