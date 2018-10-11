#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Description:   身份证构造器
"""
import datetime
import copy
__author__ = 'wyb'
def create(brithday,number,area_code = [5,2,0,1,1,2]):
    result = copy.copy(area_code)
    # 前17位所占比重
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 余数所对应校验码
    mod_keys = [1,0,'X',9,8,7,6,5,4,3,2]
    now = datetime.datetime.now()
    if brithday < now - datetime.timedelta(days=100*365):
        return None
    if brithday >= now:
        return None
    if not str(number).isdigit():
        return None
    number = int(number)
    if number < 0 or number > 999:
        return None

    # number = str(number).zfill(3)
    number= "%03d"%number
    num = result
    bri = [int(i) for i in brithday.strftime("%Y%m%d")]
    num += bri
    ns = [int(i) for i in number]
    num += ns
    suml = [num[i] * weight[i] for i in range(len(weight))]
    mod = sum(suml) % 11

    num.append(mod_keys[mod])
    return num
if __name__ == "__main__":
    idn = create(datetime.datetime(1994, 12, 27, 0, 0, 0), 108)
    print(''.join([str(i) for i in idn]))

    idn = create(datetime.datetime(1994, 12, 27, 0, 0, 0), 108)
    print(''.join([str(i) for i in idn]))
    print("main")
    bri = datetime.datetime(1994,12,27,0,0,0)
    lines = []
    for i in range(100):
        bri = bri + datetime.timedelta(days=1)
        idn,idm = create(bri,111),create(bri,102)
        idns,idms = ''.join([str(i) for i in idn]),''.join([str(i) for i in idm])
        line = "%s    %s \r"%(idns,idms)
        print(line,end='')
        lines.append(line)
    with open('idnumber.txt','w') as file:
        file.writelines(lines)