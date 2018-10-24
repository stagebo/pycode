#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     restart
    Author:        wyb
    Date:          2018/10/24 0024
    Description:   
"""
import os
def restart():
    os.system('git checkout .')
    os.system('git pull')
    os.system('python3 line.py')
    pass
if __name__ == "__main__":
    restart()
    print("main")