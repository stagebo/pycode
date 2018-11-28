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


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin) * np.random.rand(n) + vmin

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
        xs,ys,zs = point
        ax.scatter(xs, ys, zs)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

if __name__ == "__main__":
    training_set = [[(1, 0, 0), 1], [(0, 1, 1), 0], [(1, 1, 0), 1], [(1, 1, 1), 0], [(0, 0, 1), 0], [(1, 0, 1), 1]]
    draw_3d_point([i[0] for i in training_set])