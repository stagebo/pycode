#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     animation_3d
    Author:        WYB
    Date:          2018/11/29 00:21:56
    Description:   
"""
import os, sys

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib import cm
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1, projection='3d')  # 指定三维空间做图

t = np.linspace(0, 4, 200)  # 在0到4之间，均匀产生200点的数组
theta = t * 2 * np.pi  # 角度

# 生成曲线数组
z = t
x = np.sin(theta)
y = np.cos(theta)

# 运动的点
# point, = ax.plot([x[0]], [y[0]], [z[0]], 'ro', label='p')
training_set = [[(1, 0, 0), 1],
                [(0, 1, 1), 0],
                [(1, 1, 0), 1],
                [(1, 1, 1), 0],
                [(0, 0, 1), 0],
                [(1, 0, 1), 1]]
ppx,ppy,pnx,pny = [],[],[],[]
for t in training_set:
    p = t[0]
    lx = 'ro' if (t[1]==1) else 'rx'
    ax.plot([p[0]],[p[1]],[p[2]],lx,label='p')
# plt.plot(x, y, 'bo', x_, y_, 'rx')
# 曲线
line, = ax.plot([x[0]], [y[0]], [z[0]], label='line')

# 设置显示的范围和描述
x_min = 0
y_min = 0
z_min = 0
x_max = 1
y_max = 1
z_max = 1
margin = 1
ax.set_xlim(x_min - margin, x_max + margin)
ax.set_ylim(y_min - margin, y_max + margin)
ax.set_zlim(z_min - margin, z_max + margin)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# 标题
ax.set_title('3D animate')
ax.view_init(30, 35)
# 设置标签在右下角
ax.legend(loc='lower right')

history = [[[0.1, 0.0, 0.0], 1], [[0.1, -0.1, -0.1], 0], [[0.2, 0.0, -0.1], 1], [[0.2, -0.1, -0.2], 0], [[0.30000000000000004, -0.1, -0.1], 1], [[0.30000000000000004, -0.2, -0.2], 0]]


w, b = [1.3, -1.3, -1.0999999999999999], 1
X = np.arange(0, 1, 0.1)
Y = np.arange(0, 1, 0.1)
X, Y = np.meshgrid(X, Y)
Z = -(w[0] * X + w[1] * Y + b) / w[2]
# plain = ax.plot(X,Y,Z,label='plain')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
print('\n'.join(dir(surf)))
def animate(i):
    global  surf
    # line.set_xdata(x[:i + 1])
    # line.set_ydata(y[:i + 1])
    # line.set_3d_properties(z[:i + 1])
    # point.set_xdata(x[i])
    # point.set_ydata(y[i])
    # point.set_3d_properties(z[i])
    if i >= len(history):
        return
    w, b = history[i]
    X = np.arange(-1,2, 0.1)
    Y = np.arange(-1,2, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = -(w[0] * X + w[1] * Y + b) / w[2]
    # surf.update()
    surf.remove()
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)


ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=len(history),
                              interval=1000,
                              repeat=False,
                              blit=False)

plt.show()
    