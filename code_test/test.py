#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/6/29'
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
def test():return 123

class T():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def pt(self):
        print(self.a,self.b)
if __name__ == "__main__":
    t1 = T(1,2)
    t1.pt()

    # t2 = T()
    # t2.pt()
    print(test())
    print("main")
    s = """
    a
    b
    c
    """
    print(s)
    a = s.replace('\n','').replace('\r','').replace('\r\n','').replace(' ','')
    print(a)

    import enum

    print(enum)
