#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     draw_3d
    Author:        WYB
    Date:          2018/11/28 20:29:39
    Description:   
"""
import os, sys

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm


def draw_3d_point(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    n = 100

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    # for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    #     xs = randrange(n, 23, 32)
    #     ys = randrange(n, 0, 100)
    #     zs = randrange(n, zlow, zhigh)
    #     ax.scatter(xs, ys, zs, c=c, marker=m)
    #     print(xs,ys,zs,c,m)
    for point in points:
        xs,ys,zs = point[0]
        color = 'g' if(point[1]==0)else 'r'
        ax.scatter(xs, ys, zs,edgecolor=color)
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    # 绘制平面
    # [1.3, -1.3, -1.0999999999999999]b: 1
    # 1.3*x -1.3*y -1.09*z + 1 =0
    # z = (w1*x + w2*y + b)/w3
    w,b = [1.3, -1.3, -1.0999999999999999],1
    X = np.arange(0,1,0.1)
    Y = np.arange(0,1,0.1)
    X,Y = np.meshgrid(X,Y)
    Z = -(w[0]*X + w[1]*Y + b)/w[2]
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)

    ax.set_xlabel("x-label", color='r')
    ax.set_ylabel("y-label", color='g')
    ax.set_zlabel("z-label", color='b')
    fig.colorbar(surf, shrink=0.5, aspect=5)  # 图例
    plt.show()

def d3_plane():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection='3d')  # 一行一列第一个
    X = np.arange(1, 10, 1)
    Y = np.arange(1, 10, 1)
    X,Y = np.meshgrid(X, Y)  # 将坐标向量变为坐标矩阵，列为x的长度，行为y的长度
    Z = 3*X + 2*Y + 30

    # 构建平面
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)

    ax.set_xlabel("x-label", color='r')
    ax.set_ylabel("y-label", color='g')
    ax.set_zlabel("z-label", color='b')

    ax.set_zlim3d(0, 100) # 设置z坐标轴
    fig.colorbar(surf, shrink=0.5, aspect=5) # 图例

    plt.savefig("d3_plane.png")
    plt.show()
if __name__ == "__main__":
    training_set = [[(1, 0, 0), 1],
                    [(0, 1, 1), 0],
                    [(1, 1, 0), 1],
                    [(1, 1, 1), 0],
                    [(0, 0, 1), 0],
                    [(1, 0, 1), 1]]
    draw_3d_point(training_set)