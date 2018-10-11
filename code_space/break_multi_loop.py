#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     break_multi_loop
    Author:        wyb
    Date:          2018/10/11 0011
    Description:   跳出多层循环
"""

idx = 0
for i in range(5):
    for j in range(4):
        for k in range(6):
            if k == 3:
                break
            print(i,j,k)
            idx += 1
        # step = 60
        else:
            continue
        break
        # step = 15
    else:
        continue
    break
    # step = 3



print('sum step:',idx)
if __name__ == "__main__":
    print("main")