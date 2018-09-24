#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     word_cloud
    Author:        Administrator
    Date:          2018/7/23
    Description:   生成简易的词云图片
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃       ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃  永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
__author__ = 'Administrator'
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print('main')
    file = open('../data/祥林嫂.txt','r',encoding='utf8')
    ret = file.read()
    txt = ' '.join(jieba.cut(ret))
    wl = WordCloud(
        font_path='simsun.ttf',
        width=800,
        height=500
    ).generate(txt)
    png = '../data/wc.png'
    wl.to_file(png)
    # print(wl)
    plt.imshow(wl,interpolation='bilinear')
    plt.axis('off')
    print(txt)