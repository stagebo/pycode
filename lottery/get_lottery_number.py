#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     get_lottery_number
    Author:        wyb
    Date:          2018/8/29 0029
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
import requests
import re
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import lottery_2018
def get_ln(num):
    url = "http://kaijiang.500.com/shtml/ssq/18%s.shtml"%num
    ret = requests.get(url)
    # print(ret.text)

    pattern = re.compile(r'<li class="(ball_red){0,}(ball_blue){0,}">(\d+)</li>',re.M|re.I)   # 查找数字
    result1 = pattern.findall(ret.text)
    # print(result1)
    result = [int(i[2]) for i in result1]
    return result
def get_all():
    ret = []
    for i in range(1,101):
        num = str(i).zfill(3)
        ln = get_ln(num)
        print(i,ln)
        ret.append((i,ln))
    return ret
def show(x,y,title='title',xname='xname',yname='yname'):
    x = np.array(x)
    y = np.array(y)
    plot1 = plt.plot(x, y, '*', label=title)

    plt.xlabel(xname)
    plt.ylabel(yname)

    plt.legend(loc=1)  # 图例 指定legend的位置,读者可以自己help它的用法
    plt.title('curve_fit')

    plt.show()
    plt.savefig('p2.png')
if __name__ == "__main__":
    print("main")
    ret = lottery_2018.data # get_all()
    # blue_ball = [i[6] for i in ret]
    y = [0 for i in range(16)]
    for i in ret:
        y[i[1][6]-1] += 1

    x = [i+1 for i in range(len(y))]
    print(x,y)
    show(x,y,title='blue_num_count')

    y1 = [sum(i[1]) for i in ret]
    x1 = [i+1 for i in range(len(y1))]
    show(x1,y1,title='sum')
    # print(ret)