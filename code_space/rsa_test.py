#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     rsa_test
    Author:        wyb
    Date:          2018/10/8 0008
    Description:   
"""
import rsa

key = rsa.newkeys(30000)#生成随机秘钥
privateKey = key[1]#私钥
publicKey = key[0]#公钥
print(key)
print('public key:',publicKey)
print('private key:',privateKey)

message ='sanxi Now is better than never.'
print('Before encrypted:',message)
message = message.encode()

cryptedMessage = rsa.encrypt(message, publicKey)
print('After encrypted:\n',cryptedMessage)

message = rsa.decrypt(cryptedMessage, privateKey)
message = message.decode()
print('After decrypted:',message)

if __name__ == "__main__":
    print("main")