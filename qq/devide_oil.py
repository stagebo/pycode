#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     devide_oil
    Author:        wyb
    Date:          2018/9/28 0028
    Description:   小孩分油问题，容量分别为10 7 3 的三只油桶分出两桶5的油来
"""
import os
initial_oil_state = [10,0,0]
oil_volume = [10,7,3]

from collections import deque
record = deque()


if __name__ == "__main__":
    print("main")