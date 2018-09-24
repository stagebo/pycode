import datetime
import time
'''
__target__ = 时间
'''
while True:
    tar = datetime.datetime.strptime("2018-2-12 15:30:00","%Y-%m-%d %H:%M:%S")
    now = datetime.datetime.now()
    d = tar - now
    print(d)
    print("剩余天数：%s"%d.days)
    time.sleep(1)