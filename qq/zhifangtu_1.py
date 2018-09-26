#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     zhifangtu
    Author:        wyb
    Date:          2018/9/26 0024
    Description:   绘制直方图_1
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas

# example data
mu=100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)
x = [680,222,330,867,909,579,675,1071,521,1554,369,885,417,830,707,527,678,587,
1471,229,1749,922,2583,845,220,443,574,139,1066,1445,365,218,1530]

x = [1575.6,263.47,520,1458,1111,176.4,609.5,682,278,1165,2596.1,960.4,1909.8,266.5,1593.9,776.2,
     1105.6,562.7,779,861,469.88,952.4,557,1629.18,553.3,1103.6,723,623.3,944.38,899.55,375,745,790
]
x = [680,222,330,867,909,579,675,1071,521,1554,369,885,417,830,707,527,678,587,
1471,229,1749,922,2583,845,220,443,574,139,1066,1445,365,218,1530]
mu = np.mean(x)
sigma=np.std(x)
x = np.array(x)
num_bins = 9 # 组数 = 极差/组距
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins,facecolor='black',normed=1,alpha=1)
y = mlab.normpdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y
plt.plot(bins, y, 'r--') #绘制y的曲线


x1 = np.linspace(176.4, 2596.1, 1000)
#normal = mlab.normpdf(x1, x.mean(), x.std())
#line1, = plt.plot(x1,normal, 'r-', linewidth = 2)
# y = mlab.normpdf(bins, mu, sigma)#拟合一条最佳正态分布曲线y
#plt.plot(bins, y, 'r--') #绘制y的曲线
# add a 'best fit' line
# y = mlab.normpdf(bins, mu, sigma)
# plt.plot(bins, y, 'r--')
plt.xlabel('DM')
plt.ylabel('N')
plt.title('histogram')
#plt.legend('')

# Tweak spacing to prevent clipping of ylabel

plt.show()