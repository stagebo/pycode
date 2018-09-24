import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

'''
__target__ = 分布型拟合
'''

N = 10
xdata = [10**0.1*i for i in range(N)]
ydata = [10**(0.2*i+0.4) for i in range(N)]
print("xdata:",xdata)
print("ydata:",ydata)

xd = [np.log(i) if(i>0)else np.log(1) for i in xdata]
yd = [np.log(i) for i in ydata]
print("xd:",xd)
print("yd:",yd)
# xd = xdata
# yd = ydata
x = np.array(xd)
y = np.array(yd)

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

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend(loc=1)# 图例 指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')

plt.show()
plt.savefig('p2.png')


