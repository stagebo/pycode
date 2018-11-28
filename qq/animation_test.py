#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     animation_test
    Author:        WYB
    Date:          2018/11/28 23:57:58
    Description:   
"""
import os, sys

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata, zdata = [], [], []
ln, = ax.plot([], [], 'r-', animated=False)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    # ax.set_3d_properties(z[:i + 1])
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    zdata.append(np.sin(frame))
    ln.set_data(xdata, ydata, zdata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
    