#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     annotation
    Author:        wyb
    Date:          2018/8/28 0028
    Description:   
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
                ┃  永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
__author__ = 'wyb'

def ids(func):
    def wapper(*args, **kwargs):
        print(args)
        print(kwargs)
        if args[0].ids is None:
            args[0].login()
        return func(*args, **kwargs)
    return wapper

class Test():
    def __init__(self):
        self.ids = None

    def login(self):
        print('login')
        self.ids = 1

    @ids
    def access(self):
        print('access',self.ids)
# if __name__ == "__main__":
#     t = Test()
#     t.access()
#     print("main")

def attrs(**kwds):
    def decorate(f):
        # print(f)
        # print(dir(f))
        for k in kwds:
            setattr(f, k, kwds[k])
        return f

    return decorate

class C():
    def __init__(self):
        self.id = 123
    @attrs(versionadded="2.2",
           author="Guido van Rossum")
    def mymethod(self,f):
        print(getattr(self.mymethod,'versionadded',0))
        print(getattr(self.mymethod,'author',0))
        print(f)
#
# if __name__ == "__main__":
#    c = C()
#    c.mymethod(2)
#

def accepts(*types):
    def check_accepts(f):
        def new_f(*args, **kwds):
            print(types,args,kwds)
            assert len(types) == (len(args) + len(kwds)), \
                "args cnt %d does not match %d" % (len(args) + len(kwds), len(types))
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                    "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)

        # update_wrapper(new_f, f)
        return new_f

    return check_accepts


def returns(rtype):
    def check_returns(f):
        def new_f(*args, **kwds):
            print('ret:',rtype, args, kwds)
            result = f(*args, **kwds)
            assert isinstance(result, rtype), \
                "return value %r does not match %s" % (result, rtype)
            return result

        # update_wrapper(new_f, f)
        return new_f

    return check_returns


@accepts(int, (int, float))
@returns((int, float))
def func(arg1, arg2):
    return arg1 + arg2

if __name__ == "__main__":
  a = func(1, 1)
  print(a)