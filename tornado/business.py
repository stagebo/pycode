#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         business
# Purpose:      接口文件
# Author:       wyb
# Description:  接口服务
# Created:      2018-2-2 9:15:00
#----------------------------------------------------------------------------
import psycopg2
import datetime
from tornado import gen
import tornado
import logging



class apis:
    # 功能函数列表，首字母大写，命名规则：
    # Query：查询       Update: 更新
    # Check: 检查合法性 Insert: 插入(新建)
    # Delete: 删除

    _apis = []



def log(strs):
    logging.info("time:%s "% datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +str(strs))




def printf(*args, sep=' ', end='\n',):
    print(*args,sep=sep,end=end)
    pass


class functions(apis):
    """ 业务需求类函数.
        前端调用::

             参见每一个函数的注释.
    """

    def __init__(self, dbhelper):
        self.dbhelper = dbhelper
        # 初始化函数列表
        methods = dir(self)
        for m in methods:
            me = m.lower()
            if me.startswith('query_') or me.startswith('update_') or me.startswith('insert_') or me.startswith(
                    'delete_') or me.startswith('check_'):
                if m not in self._apis:
                    self._apis.append(m)
    def _errmsg(self,str):
        return {
            "result":"-1",
            "msg":str,
        }


    @tornado.gen.coroutine
    def _execute(self,sql):
        refdata = []
        try:
            cursor = yield self.dbhelper.db.execute(sql)
            refdata = [dict((cursor.description[i][0], str(value)) for i, value in enumerate(row)) for row in cursor.fetchall()]
        except psycopg2.Error as e:
            #打印错误，会打印到日志中。
            #抛出异常，系统管理员可得到通知
            raise
            return None

        return refdata

    @tornado.gen.coroutine
    def select_all(self,handler,tablename):
        right = self._right(handler.operatorid)
        if right is False:
            return [], False

        refdata  = yield self._execute("select * from %s" % tablename)
        return  refdata,True

        # 1

    # 1
    @tornado.gen.coroutine
    def Query_xq_list(self, handler):
        """
             - 功能:    #1  查询所有小区信息
             - URL:     /版本号/query_xq_list
             - HTTP:    GET

             - 返回值:
                        * 正确返回:{"result":"0","msg":"","payload":{"layers":[]}}
                        * 错误:{"result":"-1","msg":"错误消息内容"}
             - 结果说明： layers：图层信息列表
        """
        sql = 'select * from fhyc_business.t_xq'
        ret = yield self._execute(sql)
        if ret == None:
            return self._errmsg("查询失败"),True

        return {"result": "0", "msg": "", "payload": ret}, True
