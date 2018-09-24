import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

'''
__target__ = 拟合函数
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

# 数据项
data = [1530.4,218.78,365,1445,1066,139.4,574.5,443.7,220.3,845.4,2583.1,922.4,1749.8
,229.6,1471.9,587.7,678.4,527.8,707.9,830,417.3,885.53,369,1554.91,521.48,1071.27
,675.54,579.78,909.61,867.86,330.42,222,680]

# 获取直方图图表信息
xd,yd = get_data(data,9)
print(xd,yd)
x = np.array(xd)
y = np.array(yd)

# 指定函数型
def func(x,a,b,c):
    # A = (x-b)**2
    # B = 2*c**2
    # C = -A/B
    # return a*np.exp(C)
    return a*np.exp(-(x-b)**2/c)
# 获取拟合结果
popt, pcov = curve_fit(func, x, y)

# 打印拟合 参数
print(popt)

a=popt[0]#popt里面是拟合系数，读者可以自己help其用法
b=popt[1]
c = popt[2]

yvals=func(x,a,b,c)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend(loc=1)# 图例 指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')

plt.show()
plt.savefig('p2.png')


