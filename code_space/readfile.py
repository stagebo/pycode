'''
__target__ = 读取文件
'''
import os


def run():
    fn = 'C:/Users/wyb/Desktop/秋秋/yqq.txt'
    fs = open(fn)
    while 1:
        line = fs.readline()
        if not line:
            break
        print(line)

if __name__ == '__main__':
    run()