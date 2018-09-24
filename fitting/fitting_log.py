import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

'''
__target__ = 分布型拟合
'''
# 获取直方图信息
def get_data(y,n):
    '''
    获取直方图信息
    :param y:  源数据
    :param n:  组数
    :return:   返回直方图中点处坐标
    '''
    maxd = max(y)
    mind = min(y)
    dy = maxd - mind
    dx = dy/n
    yd = [0] * n
    xd = []
    idx = 0
    while True:
        xd.append(mind+idx*dx+dx/2)
        for yi in y:
            if yi>=mind+idx*dx and yi < mind+(idx+1)*dx\
                    or yi == maxd:
                yd[idx] += 1
        idx += 1
        if mind+idx*dx>=maxd:
            break
    return xd,yd


data = [2.4,11.9808,1.5,2.3,59.8,20.12,57.98,38.7,28,63,1.7,1.848,0.9,44.8,1.4,1.76,2.016,
        1.3188,2.3296,3.4342,1.2224,1.4652,1.2,2.3392,0.55,2.15,0.56,7.28,2.1888,150,2.87,2.82]
# data = [5.72,4.24,31.48,2.19,7.28,1.04,0.89,1.76,0.75,2.34,1.47,1.22,3.43,2.75,1.32,1.76]
dx = 1.8
idx = 0
xd = []
yd = []
while True:
    if idx > max(data):
        break
    sum = 0
    xidx = idx + dx/2
    for i in data:
        if i>=idx and i < idx + dx:
            sum += 1
    if sum > 0:
        xd.append(xidx)
        yd.append(sum)
    idx += dx
print(xd)
print(yd)
xdata = [np.log10(i) for i in xd]
ydata = [np.log10(i) for i in yd]
print("xdata:",xdata)
print("ydata:",ydata)
x = [1575.6, 263.47, 520.0, 1458.0, 1111.0, 176.4, 609.5, 682.0, 278.0, 1165.0, 2596.1, 960.4, 1909.8, 266.5, 1593.9, 776.2, 1105.6, 562.7, 779.0, 861.0, 469.88, 952.4, 557.0, 1629.18, 553.3, 1103.6, 723.0, 623.3, 944.38, 899.55, 375.0, 745.0, 790.0]
y = [2.164, 0.327, 0.373, 1.709, 1.511, 0.21, 0.817, 0.521, 0.31, 1.08, 3.609, 1.294, 2.452, 0.338, 2.062, 0.632, 1.135, 0.755, 0.783, 1.172, 0.593, 1.244, 0.378, 2.199, 0.747, 1.515, 0.967, 0.828, 1.29, 1.226, 0.394, 0.594, 1.001]

x = np.array(x)
y = np.array(y)

# 指定函数型
def func(x,a,b):

    return a*x + b
# 获取拟合结果
popt, pcov = curve_fit(func, x, y)

# 打印拟合 参数
print(popt)

a=popt[0]#popt里面是拟合系数，读者可以自己help其用法
b=popt[1]


yvals=func(x,a,b)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')

plt.xlabel('Fobs')
plt.ylabel('Z')

plt.legend(loc=1)# 图例 指定legend的位置,读者可以自己help它的用法
plt.title('')

plt.show()
plt.savefig('p2.png')


