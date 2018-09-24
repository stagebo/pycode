#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
__author__ = 'wyb'
def create(brithday,number,area_code = [5,2,0,1,1,2]):
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
    num = area_code
    bri = [int(i) for i in brithday.strftime("%Y%m%d")]
    num += bri
    ns = [int(i) for i in number]
    num += ns
    suml = [num[i] * weight[i] for i in range(len(weight))]
    mod = sum(suml) % 11

    num.append(mod_keys[mod])
    return num
if __name__ == "__main__":
    idn = create(datetime.datetime(1994,12,27,0,0,0),108)
    print(idn)
    print("main")