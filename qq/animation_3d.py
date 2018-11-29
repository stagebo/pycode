#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     animation_3d
    Author:        WYB
    Date:          2018/11/29 00:21:56
    Description:   
"""
import os, sys
import copy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib import cm
fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1, projection='3d')  # 指定三维空间做图

# 训练数据集
training_set = [[(1, 0, 0), 1],
                [(1, 1, 0), 1],
                [(1, 0, 1), 1],
                [(0, 1, 1), -1],
                [(1, 1, 1), -1],
                [(0, 0, 1), -1],
                ]

w = [0, 0, 0]  # 参数初始化
b = 0
# 超平面方程： w[0]*X + w[1]*Y + w[2] *Z + b =1
history = []  # 用来记录每次更新过后的w,b


def update(item):
    """
    随机梯度下降更新参数
    :param item: 参数是分类错误的点
    :return: nothing 无返回值
    """
    global w, b, history  # 把w, b, history声明为全局变量
    w[0] += 0.1 * item[1] * item[0][0]  # 根据误分类点更新参数,这里学习效率设为1
    w[1] += 0.1 * item[1] * item[0][1]
    w[2] += 0.1 * item[1] * item[0][2]
    b += 1 * item[1]
    history.append([copy.copy(w), b])  # 将每次更新过后的w,b记录在history数组中


def cal(item):
    """
    计算item到超平面的距离,输出yi(w*xi+b)
    zi(w1*xi+w2*yi+b)
    （我们要根据这个结果来判断一个点是否被分类错了。如果yi(w*xi+b)>0,则分类错了）
    :param item:
    :return:
    """
    # item = ((1,2),1)
    res = 0
    for i in range(len(item[0])):  # 迭代item的每个坐标，对于本文数据则有两个坐标x1和x2
        res += item[0][i] * w[i]
    res += b
    res *= item[1]  # 这里是乘以公式中的yi
    return res


def check():
    """
    检查超平面是否已将样本正确分类
    :return: true如果已正确分类则返回True
    """
    flag = False
    for item in training_set:
        if cal(item) <= 0:  # 如果有分类错误的
            flag = True  # 将flag设为True
            update(item)  # 用误分类点更新参数
    print("中途: w: " + str(w) + "b: " + str(b))
    if not flag:  # 如果没有分类错误的点了
        print("最终结果: w: " + str(w) + "b: " + str(b))  # 输出达到正确结果时参数的值
    return flag  # 如果已正确分类则返回True,否则返回False

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

# history = [[[0.1, 0.0, 0.0], 1], [[0.1, -0.1, -0.1], 0], [[0.2, 0.0, -0.1], 1], [[0.2, -0.1, -0.2], 0], [[0.30000000000000004, -0.1, -0.1], 1], [[0.30000000000000004, -0.2, -0.2], 0]]


surf = None
def init():
    global training_set,surf
    for t in training_set:
        p = t[0]
        lx = 'ro' if (t[1] == 1) else 'rx'
        ax.plot([p[0]], [p[1]], [p[2]], lx, label='p')

    w, b = [1.3, -1.3, -1.0999999999999999], 1
    w, b = [0, 0, -1], 1
    X = np.arange(-1,2, 0.1)
    Y = np.arange(-1,2, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = -(w[0] * X + w[1] * Y + b) / w[2]
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)

def animate(i):
    global  surf
    if i >= len(history):
        return
    w, b = history[i]
    X = np.arange(-1,2, 0.1)
    Y = np.arange(-1,2, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = -(w[0] * X + w[1] * Y + b) / w[2]
    # surf.update()
    if "remove" in dir(surf):
        surf.remove()
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)


if __name__ == "__main__":
    for i in range(100000):  # 迭代1000遍
        if not check(): break  # 如果已正确分类，则结束迭代

ani = animation.FuncAnimation(fig=fig,
                              init_func=init,
                              func=animate,
                              frames=len(history),
                              interval=1000,
                              repeat=False,
                              blit=False)

plt.show()
    