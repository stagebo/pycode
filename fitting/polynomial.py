import matplotlib.pyplot as plt
import numpy as np
'''
__target__ = 多项式拟合
'''
x = np.arange(-17, 17, 0.001)
y = np.array([(item**3+3*item**2+4*item+5) for item in x])

print(len(x),len(y),x,y)
z1 = np.polyfit(x, y, 3)#用3次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title('polyfitting')
plt.show()
plt.savefig('p1.png')
for x in range(16):
    print(x**3+3*x**2+4*x+5,p1(x))

print(1e+15)