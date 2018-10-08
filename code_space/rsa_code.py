#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     rsa_code
    Author:        wyb
    Date:          2018/10/8 0008
    Description:   RSA 加密模拟
"""

def is_prime(n):
    for i in range(2,n-1):
        if n%i == 0:
            return True
    return False

def is_each_prime(a,b):
    return False if ([ True for i in range(2,min(a,b))if a%i == 0 and b%i == 0]) else True

def get_big_prime(start=100000):
    while is_prime(start):start += 1
    return start

def get_key(p=-1,q=-1):
    if p == -1:
        p = get_big_prime(10**10)
    if q == -1:
        q = get_big_prime(10**12)
    N = p*q
    FN = (p-1)*(q-1)
    e = 3
    while not is_each_prime(e,FN):
        e += 1
        # print(e,FN)
    d = -1
    idx = 1
    sum = 1
    while idx < FN:
        sum += FN
        if sum % e == 0:
            d = sum / e
            break
        idx += 1
    assert d > 0
    d = int(d)
    return N,e,d


def _rsa(base,key,msg): return msg**key%base if(base >=1 and key >=1)else 0

if __name__ == "__main__":
    # print(123)
    # print(get_key(137,191))
    base = 26167
    keyE = 3
    keyD = 17227
    msg = 333
    emsg = _rsa(base,keyE,msg)
    dmsg = _rsa(base,keyD,emsg)
    print('before encode:',msg)
    print('after encode:',emsg)
    print('after decode:',dmsg)
    print("main")