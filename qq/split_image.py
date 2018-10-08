#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     split_image
    Author:        wyb
    Date:          2018/10/7 0007
    Description:   
"""
from PIL import Image
import uuid
def split_image(imgsrc):
    '''
    1   2   3
    4(0,1)   5   6
    7   8   9

    :return:
    '''
    im = Image.open(imgsrc)  # 读取和代码处于同一目录下的 lena.png
    w, h = im.size
    a = min(w, h)
    d = a // 3
    value_list = []
    uid_str = str(uuid.uuid1())
    filename = 'images/image_split_%s.png' % (uid_str)
    value_list.append("'" + filename + "'")
    im.save(filename)
    for key in range(9):
        filename = 'images/image_split_%s_%s_%s.png' % (key, uid_str, key)
        value_list.append("'" + filename + "'")
        j = key // 3
        i = key % 3
        region = im.crop((i * d, j * d, i * d + d, j * d + d))
        region.save(filename)


if __name__ == "__main__":
    imgsrc = "F:\\Users\\wyb\\Desktop\\123.jpg"
    split_image(imgsrc)
    print("main")