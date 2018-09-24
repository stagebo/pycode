#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         db.py
# Author:       wyb
# Created:      2018-7-16 15:30:41
# Description:  数据库访问
#----------------------------------------------------------------------------
from tornado import gen
import psycopg2
import momoko
from tornado.ioloop import IOLoop

class DbHelper:
    def __init__(self):
        pass

    def open(self,ioloop,dbname,dbusername,dbpasswd,dbhost,dbport):
        dsn = 'dbname=%s user=%s password=%s host=%s port=%s' % (
            dbname, dbusername, dbpasswd, dbhost, dbport)

        self.db = momoko.Pool(
            dsn=dsn,
            size=1,
            max_size=20,
            ioloop=ioloop,
            setsession=("SET TIME ZONE UTC",),
            raise_connect_errors=False,
        )

    def create(self):
        pass

    @gen.coroutine
    def execute(self, sql):

        if sql == "":
            return False

        try:
            cursor = yield self.db.execute(sql)

        except psycopg2.Error as e:
            raise
            return False
        return True

    @gen.coroutine
    def execute_commit(self, sql):

        if sql == "":
            return False
        try:
            cursor = yield self.db.execute(sql)
            cursor.commit()
        except psycopg2.Error as e:
            raise
            return False
        return True
    @gen.coroutine
    def select(self,tablename,fdata=None):
        be = self.exist_table(tablename)
        if  be == False:
            return False

        try:
            cursor = yield self.db.execute("select row_to_json("+ tablename +") from "+ tablename )
            refdata=cursor.fetchall()
        except psycopg2.Error as e:
            raise
        if refdata :
            return refdata
        else:
            return False





    def close(self):
        self.conn.close()




if __name__ == "__main__":
     pass
