#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__target__ = 获取平台信息
__mtime__ = '2018/7/2'
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
import platform

def TestPlatform():
    print ("----------Operation System--------------------------")
    #Windows will be : (32bit, WindowsPE)
    #Linux will be : (32bit, ELF)
    print(platform.architecture())

    #Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
    #Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final
    print(platform.platform())

    #Windows will be : Windows
    #Linux will be : Linux
    print(platform.system())

    print ("--------------Python Version-------------------------")
    #Windows and Linux will be : 3.1.1 or 3.1.3
    print(platform.python_version())

# def UsePlatform():
#   sysstr = platform.system()
#   if(sysstr =="Windows"):
#     print ("Call Windows tasks")
#   elif(sysstr == "Linux"):
#     print ("Call Linux tasks")
#   else:
#     print ("Other System tasks")

def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        return 1
    elif (sysstr == "Linux"):
        return 2
    else:
        return 0
def printf( *args, sep=' ', end='\n',):
    if UsePlatform() == 1:
        print(*args)

if __name__ == "__main__":
   printf(1,2,3,'sdf')