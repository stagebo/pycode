#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'wyb'
__mtime__ = '2018/7/5'
__target__ = '生成markdown文件，批量生成，通过读取文件内部的__target__ 行来填写内容'
"""
import os

idx = 1
def make_markdown(directory):
    global smd,idx
    with open(os.path.join(directory,'readme.md'),'w',encoding='utf-8') as md:
        md.write('%s目录代码列表\r\n=====\r\n\r\n'%directory)
        list = os.listdir(directory)  # 列出文件夹下所有的目录与文件
        for f in list:
            path = os.path.join(directory, f)
            if os.path.isfile(path) and f.endswith('.py'):
                md.write('## 文件：[%s](%s)\r' % (f, f))
                dr = directory[directory.find('/')+1:]
                smd.write('### %s 文件：[%s/%s](%s/%s)\r' % (idx, dr, f,dr, f))
                idx += 1
                print('## 文件：[%s](%s)\r'%(f,f))
                target = ''
                title = ''
                with open(path,'r',encoding='utf-8') as rd:
                    lines = rd.readlines()
                    for l in lines:
                        if '__target__' in l and target == '':
                            target = l.replace('__target__ = ', '').replace('__target__', '')
                        if 'Description' in l and target == '':
                            target = l.replace('Description=', '').replace('Description:', '')
                        if '__title__' in l and target == '':
                            title = l.replace('__title__', '')
                        if 'File Name' in l and target == '':
                            title = l.replace('File Name:', '')

                md.write('### 标题：%s\r' % title)
                md.write('> 内容：%s\r\n' % target)
                # smd.write('### 标题：%s\r' % title)
                smd.write('> 内容：%s\r\n' % target)
                print('> 内容：%s\r\n'%target)


smd = open('../readme.md','w',encoding='utf-8')
smd.write('pycode 代码说明\r')
smd.write('=====\r')
smd.write('##  日常代码收集整理\r')
if __name__ == "__main__":
    print("main")
    mds = ['../code_space','../code_test','../data','../douyu','../fitting','../spider','../ssh_code','../tdqs','../tornado','../qq']
    for d in mds:
        make_markdown(d)

