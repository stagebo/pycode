#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description:Tornado实现web程序异步访问
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
import traceback
import json
import  db
import business

class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(  )

        handlers=[
            (r"/1.0.0/(\w+)", CommonHandler),
        ]
        super(Application, self).__init__(handlers,**settings)

class CommonHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, word):
        print('get request')
        yield self.deal(self, word)

    @tornado.gen.coroutine
    def post(self, word):
        print('post request')
        yield self.deal(self,word)

    @tornado.gen.coroutine
    def deal(sf,self,word):
        if 'apis' not in dir(self):
            self. apis = [business.functions(self.application.db)
                        ]
        try:
            word = word[0].upper() + word[1:].lower()
            methods = []
            for api in self.apis:
                if word in api._apis:
                    methods.append( getattr(api, word))
            if len(methods) < 1:
                self.write("接口不存在err或未定义到apis中")
                return
            if len(methods) > 1:
                self.write("接口名重复！")
                return
            response = yield tornado.gen.Task(methods[0], self)
            if not response[1]:
                print(response)

            self.write(json.dumps(response[0],ensure_ascii=False))
        except AttributeError as e:
            traceback.print_exc()
            self.write("服务器异常！")
            # sys.exit(0)
        finally:
            self.finish()

if __name__ == "__main__":

    dbhost = '172.16.10.21'
    dbname = 'pcnp'
    dbuname = 'postgres'
    dbport = 5432
    dbpwd = 'tdq$abc123'

    tornado.options.parse_command_line()
    app = Application()
    ioloop = tornado.ioloop.IOLoop.instance()

    app.db = db.DbHelper()
    app.db.open(ioloop=ioloop, dbname=dbname, dbusername=dbuname, dbpasswd=dbpwd, dbhost=dbhost, dbport=dbport)

    print("数据库地址：", dbhost, dbname, dbpwd, dbport)
    future = app.db.db.connect()
    ioloop.add_future(future, lambda f: ioloop.stop())
    ioloop.start()

    http_server = tornado.httpserver.HTTPServer(app)
    port = 8888
    host = 'localhost'
    http_server.listen(port)
    print('主机地址：http://%s:%s'%(host,port))
    ioloop.start()