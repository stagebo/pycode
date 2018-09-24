'''
__target__ = 直方图分布
'''
import matplotlib.pyplot as plt
import numpy as np


data = [2.4,11.9808,1.5,2.3,59.8,20.12,57.98,38.7,28,63,1.7,1.848,0.9,44.8,1.4,1.76,2.016,
        1.3188,2.3296,3.4342,1.2224,1.4652,1.2,2.3392,0.55,2.15,0.56,7.28,2.1888,150,2.87,2.82]
# data = [5.72,4.24,31.48,2.19,7.28,1.04,0.89,1.76,0.75,2.34,1.47,1.22,3.43,2.75,1.32,1.76]

dx = 2
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

fig = plt.figure()
# fig.suptitle('bold figure suptitle', fontsize=6, fontweight='bold')
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('DeltF = %s'%dx)
ax.set_xlabel('Fobs(Jy ms)(10^x)')
ax.set_ylabel('△N (10^y)')
ax.plot(xdata,ydata, 'o')
plt.axis([-.5, 2, -.5, 1.5])

#
plist = [(xdata[i],ydata[i]) for i in range(len(xdata))]
print('point list:',plist)
for p in plist:
    delt = .1
    delt1 = .005
    xx,yy = p
    plt.annotate('', xy=(xx, yy - delt), xytext=(xx, yy + delt),
                 arrowprops=dict(facecolor='red', width=.1, headwidth=0),
                 )
    plt.annotate('', xy=(xx-delt, yy ), xytext=(xx+delt, yy),
                 arrowprops=dict(facecolor='red', width=.1, headwidth=0),
                 )

    # plt.annotate('', xy=(xx - delt1, yy - delt), xytext=(xx + delt1, yy - delt),
    #              arrowprops=dict(facecolor='red', width=.1, headwidth=0),
    #              )
    # plt.annotate('', xy=(xx - delt1, yy + delt), xytext=(xx + delt1, yy + delt),
    #              arrowprops=dict(facecolor='red', width=.1, headwidth=0),
    #              )
    # plt.annotate(r'', xy=(xx, yy - 0.1), xytext=(xx, yy + .1), xycoords='data',
    #   textcoords='offset points', fontsize=9,
    #  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

mlx = [xdata[0],xdata[9]]
mly = [ydata[0],ydata[9]]
plot2=plt.plot(mlx,mly, 'r',label='curve_fit values')

# index_ls = ['10^%s'%round(i,1) for i in xdata] # ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
# plt.xticks(xdata, index_ls)

plt.show()