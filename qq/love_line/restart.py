#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     restart.py
    Author:        wyb
    Date:          2018/10/23 0023
    Description:   重启 line web服务。
"""
import os

#lines connect to popen_file's read
def kill_line():
    lines = os.popen('ps -ef')
    for line in lines:
        if line.find("python3") == -1 and line.find("java") == -1:
            continue
        vars = line.split()
        pid = vars[1]  # get pid
        proc = ' '.join(vars[7:])  # get proc description
        if "line.py" in proc and "python" in proc:
            print("kill %s is starting"%pid)
            os.system("kill %s"%pid)
        elif "tale" in proc and "java" in proc:
            print(proc, pid)
if __name__ == "__main__":
    kill_line()
    os.system("chmod 777 start.sh")
    os.system("bash start.sh")
