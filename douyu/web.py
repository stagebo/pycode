import os
import tornado.ioloop
import pyrestful.rest
import logging
import pymysql
import configparser
import sys
import datetime
import json
import platform
import re
import traceback
from pyrestful import mediatypes
from pyrestful.rest import get, post, put, delete
from tornado.log import access_log, app_log, gen_log
from tornado.options import define,options
sys.path.append("..")


from tornado import ioloop, gen
from tornado_mysql import pools





class Application(pyrestful.rest.RestService):
    def __init__(self):
        self.cf = configparser.ConfigParser()



        logging.info("tornado is tring to init...")
        settings= dict(
            #cookie_secret="SBwKSjz3SCWo04t68f/FOY7fPKZI20JYje1IYPBrxaM=",
            template_path=os.path.join(os.path.dirname(__file__), "html"),

        )
        handlers=[
            MainHadler,

        ]
        super(Application, self).__init__(handlers, **settings)

        logging.info("tornado is inited.")


#
class MainHadler(pyrestful.rest.RestHandler):
    @get(_path="/")
    def index(self):
        self.render("base.html")

    @get(_path="/main")
    def main_page(self):
        self.render("main.html")

    @get(_path="/doc")
    def main_doc(self):
        self.render("doc/html/index.html")

    @get(_path="/about")
    def about_page(self):
        self.finish("123")



    @get(_path="/love/hastime" ,_produces=mediatypes.APPLICATION_JSON)
    def get_sum_time(self):
        now = datetime.datetime.now()
        tar = datetime.datetime(2017,6,6,21,0,0)
        d = now - tar
        return {
            "days": d.days,
            "seconds": d.seconds
        }

    @get(_path="/admin/redis", _produces=mediatypes.APPLICATION_JSON)
    def redis_test(self):
        try:
            rd = self.application.redis
            rd.set("time",datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            d = rd.get("time")

            return {
                'time':d
            }
        except:
            traceback.print_exc()



def main():

    try:
        print("Start the service")
        app = Application()
        app.listen(8888)
        print("access port %s" % 8888)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop the service")

if __name__ == '__main__':
    main()
