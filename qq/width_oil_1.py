#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     width_oil_1
    Author:        wyb
    Date:          2018/10/5 0005
    Description:   广度优先搜索
"""
import os

initial_oil_state = [10,0,0] # 油瓶的初始状态
oil_volume = [10,7,3] # 每个油瓶的对应容积
from collections import deque # 导入collections标准库中的队列对象和方法 # 利用python的deque队列记录状态转移情况，初始化时加入油瓶初始状态。deque是可以从头尾插入和删除的队列
record = deque()
record.append(initial_oil_state)
# 删除文件，因为文件以追加模式打开
answer = '../data/oil_half_width_answer.txt'
if os.path.exists(answer):
    os.remove(answer)


def NextStateLegal(current_state,oil_volume):
    next_action = [
        (from_,to_)
        # 列表推导
        # 例如[x*x for x in range(10) if x % 3 == 0]得出10以内能被3整除的数的平方构成的列表
        for from_ in range(3) for to_ in range(3)
        if from_ != to_ and current_state[from_] > 0
           and current_state[to_] < oil_volume[to_]
    ]
    # 通过列表推导式获得下一动作的二元组构成的列表，由（倒出油瓶编号，倒入油瓶编号）组成。
    # 二重循环得到下一步的所有可能动作，然后通过
    # 1.倒入倒出不能为同一个2.倒出的油瓶中必须有油3.已经满了的油瓶不能再倒入 的条件判断是否合法
    for from_, to_ in next_action:
        # next_state = current_state ,浅复制造成错误,不该这样,或者可以导入copy使用deepcopy方法
        next_state = list(current_state)
        if current_state[from_] + current_state[to_] >oil_volume[to_]:
            next_state[from_] -= (oil_volume[to_]-current_state[to_])
            next_state[to_] = oil_volume[to_]
        else:
            next_state[from_] = 0
            next_state[to_] = current_state[to_] + current_state[from_]
        yield next_state

# 再由所有可能的合法动作得出所有的下一个状态，通过yield产生供其它函数调用

# 记录调试的变量：num表示总共实现方法数，record_list记录所有实现路径
num = 0
record_list = []

def searchResult(record, oil_volume=[10,7,3], final_state=[5,5,0]):
    global num, record_list
    # 由record的末尾元素得到当前油瓶状态
    current_state = record[-1]
    # 得到关于当前状态的下一状态的可迭代生成器，供下一步循环使用
    next_state = NextStateLegal(current_state, oil_volume)
    # 遍历所有可能的下一个状态
    for state in next_state:
        # 保证当前状态没在之前出现过。如果状态已经出现还进行搜索就会形成状态环路，陷入死循环。
        if state not in record:
            # 添加到新的状态到列表中
            record.append(state)
            # 判断是否达到最终状态
            if state == final_state:
                #记录当前是第几种方案
                numm = num + 1
                s_numm = str(numm)
                str_record = ''
                #将队列转换为相对美观的字符串
                for i in record:
                    str_record += str(i)
                    if i != [5, 5, 0]:
                        str_record += '->'
                # console打印可执行方案
                print(str_record)
                # 连接字符串以便保存
                queue_ = '第'+ s_numm + '种方案' + str_record + '\n\n'
                # 文件存入方案，a表示文件以追加模式打开
                with open(answer, 'a', encoding='utf-8') as f:
                    f.write(queue_)
                #record_list.append(record)这样使用错误，导致加入列表的是record的引用
                #应该使用下面的式子来进行深复制，得到一个新的队列再加入列表。
                record_list.append(deque(record))
                num += 1
            else:
                # 如不是最终状态则递归搜索
                searchResult(record, oil_volume, final_state)
            # 去除当前循环中添加的状态，进入下一个循环，关键步！
            record.pop()

if __name__ == '__main__':
    # 开始
    searchResult(record)
    # print(record_list)
    # print([len(i) for i in record_list])
    # 保存方案数以及最短路径输出字符串
    number = "用广度优先搜索共有%d种方案。" % num
    shortest = "路径最短的方案中状态总数为%d。" % min([len(i) for i in record_list]) # 数字转换字符串，为了方便保存在文件中
    s_num = str(num)
    s_min = str(min([len(i) for i in record_list]))
    # 找到最短路径所在下标
    s_min_index = [j for j in [len(i) for i in record_list] if j == int(s_min)][0]
    s_min_record = "最短路径为：%s"%'-->'.join([str(i) for i in record_list[s_min_index]])

    # 保存需要存放的字符串，将用于write函数中
    ss_num = "用广度优先搜索共有" + s_num + "种方案。\n"
    ss_min = "路径最短的方案中状态总数为" + s_min + "。\n"
    # 文件存入方案数以及最短路径
    with open(answer, 'a',encoding='utf-8') as f:
        f.write(ss_num)
        f.write(ss_min)
        f.write(s_min_record)

    # console打印所有方案的数量和最短路径
    print(number)
    print(shortest)
    print(s_min_record)

