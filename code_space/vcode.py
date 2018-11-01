#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     vcode
    Author:        wyb
    Date:          2018/10/27 0027
    Description:   生成验证码
"""

# 导入random模块
import random

# 导入Image,ImageDraw,ImageFont模块
from PIL import Image, ImageDraw, ImageFont
def get_str(l):
    s = [i for i in '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    result = ''
    for i in range(l):
        c = random.choice(s)
        result += c
    return result

def get_img(vcode):
    # 定义使用Image类实例化一个长为120px,宽为30px,基于RGB的(255,255,255)颜色的图片
    img1 = Image.new(mode="RGB", size=(120, 30), color=(255, 255, 255))

    # 实例化一支画笔
    draw1 = ImageDraw.Draw(img1, mode="RGB")

    # 定义要使用的字体
    # font1 = ImageFont.truetype("One Chance.ttf", 28)

    for i,char1 in enumerate(vcode):
        # char1 = random.choice([chr(random.randint(65, 90)), str(random.randint(0, 9))])

        # 每循环一次重新生成随机颜色
        color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # 把生成的字母或数字添加到图片上
        # 图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
        draw1.text([i * 24, 0], char1, color1)
    # 把生成的图片保存为"pic.png"格式
    # with open("pic.png", "wb") as f:
    #     img1.save(f, format="png")
    return img1

if __name__ == "__main__":
    print(get_str(4))
    get_img(get_str(4))
    print("main")