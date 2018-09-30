#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     divi_oil
    Author:
    Date:          2018/9/30 0030
    Description:   广度优先搜索分油解
"""

import  os
initial_oil_state=[10,0,0]
oil_volume=[10,7,3]
from collections import deque

record = deque()

record.append(initial_oil_state)

if os.path.exists('oil_half_width_answer.txt'):
    os.remove('oil_half_width_answer.txt')

def NextStateLegal(current_state,oil_volume):
    next_action =[(from_,to_)
                  for from_ in range(3) for to_ in range(3)
                  if from_ !=to_ and current_state[from_] >0
                  and current_state[to_] < oil_volume[to_]
                  ]

    for from_,to_ in next_action:
          next_state = list(current_state)
          if current_state[from_] + current_state[to_]>oil_volume[to_]:
              next_state[from_] -= (oil_volume[to_]-current_state[to_])
              next_state[to_] = oil_volume[to_]
          else:
              next_state[from_] =0
          next_state[to_]=current_state[to_]+current_state[from_]
          yield next_state
          num = 0
          record_list =[]

def searchResult(record,oil_volume=[10,7,3],final_state=[5,5,0]):
    global num,record_list
    current_state =record[-1]
    next_state =NextStateLegal(current_state,oil_volume)
    for state in next_state:
        if state not in record:
            record.append(state)
        if state == final_state:
           num  =num+1
           s_num =str(num)
           str_record=''
    for i in record:
        str_record+=str(i)
        if i!=[5,5,0]:
            str_record +='->'
            print(str_record)
            queue_='第'+s_num+'种方案'+str_record+'\n\n'
            f=open('oil_half_width_answer.txt','a')
            f.write(queue_)
            f.close()
            record_list.append(deque(record))
            num += 1
        else:
            searchResult(record,oil_volume,final_state)
            record.pop


if __name__=='__main__':
    searchResult(record)
    number = "广度优先搜索共有%d种方案"%num
    shortest="路径最短的方案中状态总数为%d"% min([len(i)for i in record_list])
    s_num =str(num)
    s_min=str(min([len(i) for i in record_list]))
    ss_num="用广度优先搜索共有"+s_num + "种方案。\n"
    ss_min="路径最短的方案中状态总数为"+s_min+"。\n"
    f=open('oil_half_width_answer.txt','a')
    f.write(ss_num)
    f.write(ss_min)
    f.close()
    print(number)
    print(shortest)


