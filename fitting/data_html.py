#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     data_html
    Author:        wyb
    Date:          2018/8/31 0031
    Description:   爬去网站天文台计算数据
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
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit




# def show(x,y,title='Z-Fobs',xname='xname',yname='yname'):
#     # x = np.array(x)
#     # y = np.array(y)
#     plot1 = plt.plot(x, y, '*', label=title)
#
#     plt.xlabel('Fobs')
#     plt.ylabel('Z')
#     plt.grid(True)
#     plt.legend(loc=1)  # 图例 指定legend的位置,读者可以自己help它的用法
#     plt.title('')
#
#     plt.show()
#     plt.savefig('p2.png')
data = """337.3	-43.7	1575.6
10.9	-45.4	263.47
204.4	-6.4	520
332.2	6.24	1458
45.1	-38.7	1111
303.2	-51.7	176.4
266	51.4	609.5
254.11	-9.54	682
220.36	27.19	278
246.05	-0.99	1165
18.9	-60.8	2596.1
239	34.8	960.4
32.6	-8.5	1909.8
333.892	-53.5959	266.5
278	16.5	1593.9
232.665	-3.2348	776.2
24.6628	5.28092	1105.6
50.8413	-54.612	562.7
260.55	-21.9253	779
324.788	54.7446	861
225.955	30.6556	469.88
7.45003	27.4203	952.4
174.95	-0.225138	557
308.22	-26.2647	1629.18
49.2871	-66.2037	553.3
80.9978	-59.0191	1103.6
355.862	-41.7522	723
56.12	-37.82	623.3
50.829	-54.7663	944.38
226.444	-60.0303	899.55
300.653	-41.8051	375
25.434	-4.00381	745
356.641	-20.0206	790"""
dl = data.split('\n')
dls = [d.split('\t') for d in dl]

import requests
import re

def get_z(glo,gla,dm,dm_host):
    url = 'http://www.atnf.csiro.au/research/pulsar/ymw16/index.php?mode=IGM&gl=%s&gb=%s&dm=%s&DM_Host=%s&ndir=1' % (
    glo, gla, dm,dm_host)
    print(url)
    page = requests.get(url)
    pattern = re.compile(r'DM_IGM(.+)Dist:  ', re.M | re.I)  # 查找数字
    r = pattern.findall(page.text)
    print(r)
    if r:
        lt = r[0].split(':')
        zd = float(lt[len(lt) - 1])
        return zd

xd = []
yd1,yd2,yd3 = [],[],[]
dh1, dh2, dh3 = (0, 50, 100)
for dd in dls:
    # print(dd)
    glo,gla,dm = dd
    z1 = get_z(glo,gla,dm,dh1)
    z2 = get_z(glo,gla,dm,dh2)
    z3 = get_z(glo,gla,dm,dh3)
    yd1.append(z1)
    yd2.append(z2)
    yd3.append(z3)
    xd.append(float(dm))
    # break
print('x=',xd)
print('y1=',yd1)
print('y2=',yd2)
print('y3=',yd3)
