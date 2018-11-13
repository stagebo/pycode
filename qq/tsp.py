#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     tsp
    Author:        WYB
    Date:          2018/11/04 12:34:43
    Description:   暴力求解tsp 问题
"""

# 求两点之间的距离 i=(index,x,y)
def distance(i,j):
    # i = (idex,x1,y1)
    # j = (idx2,x2,y2)
    #i,j = (idx1,x1,y1,idx2,x2,y2)
    m,x,y = i
    n,xx,yy = j
    return ((x-xx)**2 + (y-yy)**2)**0.5

# 求全排列
def perm(l):
    if(len(l)<=1):
        return [l]
    r=[]
    for i in range(len(l)):
        s=l[:i]+l[i+1:]
        p=perm(s)
        for x in p:
            r.append(l[i:i+1]+x)
    return r

# 原始数据
data = []
# 读取原始数据
with open('city.txt','r') as file:
    lines = file.readlines()
    for l in lines:
        row = []
        for j in l.replace('\n','').split(" "):
            row.append(int(j))
        data.append(row)
print('原始数据：',data)
# 距离邻接矩阵
dist = [[0 for i in data] for j in data]

# 计算距离
for row in range(len(data)):
    for col in range(len(data)):
        if row == col:
            dis = 0
        else:
            dis = distance(data[row],data[col])
        dist[row][col] = dis
print('======距离邻接矩阵=======')
for row in dist:
    for j in row:
        print('{:10f}'.format(j),end='  ')
    print()
print('======距离邻接矩阵=======')

# 得到全排列
paths = perm([i for i in range(len(data))])
# 去重
paths_set = []
for p in paths:
    while p[0] != 0:
        # 旋转
        # p = ABCD
        p = p[1:]+[p[0]]
        # P = BCDA
    p.append(0)
    paths_set.append(tuple(p))
paths = set(paths_set)
print('======可用路径=======')
for i in paths:
    print('->'.join([str(j) for j in i]))
print('======可用路径=======')
# 计算每一个排列的距离
total = []
for path in paths:
    dis_total = 0
    for i in range(1,len(path)):
        dis_total += distance(data[path[i-1]],data[path[i]])
    total.append((dis_total,path))
# 找出距离最小值
print(total)
min_dis = min(i[0] for i in total)
min_paths = [p for p in total if p[0] == min_dis]
print("======最短路径=======")
print('\n'.join([str(i) for i in min_paths]))
print("======最短路径=======")
