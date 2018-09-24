#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/7/5'
__target__ = '生成markdown文件，批量生成，通过读取文件内部的__target__ 行来填写内容'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import os

def make_markdown(directory):
    with open(os.path.join(directory,'readme.md'),'w',encoding='utf-8') as md:
        md.write('%s目录代码列表\r\n=====\r\n\r\n'%directory)
        list = os.listdir(directory)  # 列出文件夹下所有的目录与文件
        for f in list:
            path = os.path.join(directory, f)
            if os.path.isfile(path) and f.endswith('.py'):
                md.write('## 文件：[%s](%s)\r\n'%(f,f))
                print('## 文件：[%s](%s)\r\n'%(f,f))
                target = ''
                title = ''
                with open(path,'r',encoding='utf-8') as rd:
                    lines = rd.readlines()
                    for l in lines:
                        if '__target__' in l and target == '':
                            target = l.replace('__target__', '')
                        if 'Description' in l and target == '':
                            target = l.replace('Description:', '')
                        if '__title__' in l and target == '':
                            title = l.replace('__title__', '')
                        if 'File Name' in l and target == '':
                            title = l.replace('File Name:', '')

                md.write('### 标题：%s\r\n' % title)
                md.write('> 内容：%s\r\n'%target)
                print('> 内容：%s\r\n'%target)



if __name__ == "__main__":
    print("main")
    make_markdown('.')
    # make_markdown('../code_space')
    make_markdown('../code_test')
    make_markdown('../data')
    make_markdown('../douyu')
    make_markdown('../fitting')
    make_markdown('../spider')
    make_markdown('../ssh_code')
    make_markdown('../tdqs')
    make_markdown('../tornado')
    make_markdown('../qq')
