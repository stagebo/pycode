#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     tornado_file_access
    Author:        WYB
    Date:          2018/11/14 16:39:13
    Description:   静态文件访问
"""
#!/usr/bin/env python
# ! coding: utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web


class Hello(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/dist/index.html")


class Front(tornado.web.StaticFileHandler):
    '''
    静态文件访问
    '''
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")


app = tornado.web.Application([
    (r"/", Hello),
    (r"/dist/(.*)", Front, {"path": "dist/"})
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()