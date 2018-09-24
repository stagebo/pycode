'''
__target__ =
'''
import sys
def run():
    p = sys.argv
    fs = open(p[0])
    print('begin to read script',end='')
    while 1:
        line = fs.readline()
        if not line:
            break
        print(line,end=' ')
    print('read script end')

if __name__ == "__main__":
    run()