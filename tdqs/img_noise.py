#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     img_noise
    Author:        WYB
    Date:          2018/11/15 10:31:27
    Description:   
"""
import os, sys

# coding:utf-8
import sys, os
from PIL import Image, ImageDraw
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('veid.png')

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()
