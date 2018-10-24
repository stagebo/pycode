#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     md5_rsa
    Author:        wyb
    Date:          2018/10/23 0023
    Description:   md5+rsa 混合加密
"""


import rsa
import hashlib

publicKey,privateKey = rsa.newkeys(1024)#生成随机秘钥

print('public key:',publicKey)
print('private key:',privateKey)

message ='Test123456'
print('plain test:',message)

message = message.encode()
message = hashlib.md5(message).hexdigest()
print('Before encrypted:',message)

message = message.encode()
cryptedMessage = rsa.encrypt(message, publicKey)
print('After encrypted:\n',cryptedMessage)


message = rsa.decrypt(cryptedMessage, privateKey)
message = message.decode()
print('After decrypted:',message)

# 私钥签名
signature = rsa.sign(message.encode(), privateKey, 'SHA-1')

# 公钥验证
rsa.verify(message.encode(), signature, publicKey)

if __name__ == "__main__":
    print("main")