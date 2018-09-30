#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     img2hw
    Author:        wyb
    Date:          2018/9/30 0030
    Description:   图片转手绘
"""
from PIL import Image
import numpy as np
import sys, getopt
def img2hand_write(input,output):
    a = np.asarray(Image.open(input).convert('L')).astype('float')

    depth = 10.                     # (0-100)
    grad = np.gradient(a)            #取图像灰度的梯度值
    grad_x, grad_y = grad              #分别取横纵图像梯度值
    grad_x = grad_x*depth/100.
    grad_y = grad_y*depth/100.
    A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
    uni_x = grad_x/A
    uni_y = grad_y/A
    uni_z = 1./A

    vec_el = np.pi/2.2                  # 光源的俯视角度，弧度值
    vec_az = np.pi/4.                   # 光源的方位角度，弧度值
    dx = np.cos(vec_el)*np.cos(vec_az)  #光源对x 轴的影响
    dy = np.cos(vec_el)*np.sin(vec_az)  #光源对y 轴的影响
    dz = np.sin(vec_el)             #光源对z 轴的影响

    b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)    #光源归一化
    b = b.clip(0,255)

    im = Image.fromarray(b.astype('uint8')) #重构图像
    im.save(output)

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    input_file = None
    output_file = None
    for op, value in opts:
        if op == "-i":
            input_file = value
        elif op == "-o":
            output_file = value
    if not input_file or not output_file:
        print('''
                   -i input image file
                   -o output image file
                   ''')
        sys.exit(1)
    img2hand_write(input_file,output_file)
    print("main")