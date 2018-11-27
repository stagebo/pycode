#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     aestest
    Author:        WYB
    Date:          2018/11/26 15:52:13
    Description:  AES 加解密，AES/CBC/ZeroPadding
"""

import sys
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex

# BS = AES.block_size
# pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
# unpad = lambda s: s[0:-ord(s[-1])]


def encrypt_aes(text, key = bytes("tdqsgf8888!@#$%^", encoding='utf8'),iv=bytes("tdqsgf8888!@#$%^", encoding='utf8')):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    PADDING = '\0'
    pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
    AES_code = bytes(pad_it(text),encoding='utf8')
    code = cipher.encrypt(AES_code)
    # print(code)
    # return code
    base64_text = str((base64.encodebytes(code)).decode()).replace('\n','')

    return base64_text


def decode_aes(text,key = bytes("tdqsgf8888!@#$%^", encoding='utf8'),iv=bytes("tdqsgf8888!@#$%^", encoding='utf8')):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    textb = base64.b64decode(text.encode('utf-8'))
    decrypted_text = cipher.decrypt(textb).decode('utf-8')
    decrypted_code = decrypted_text.rstrip('\0')

    return decrypted_code
key = bytes("tdqsgf8888!@#$%^",encoding='utf8')
iv = bytes("tdqsgf8888!@#$%^",encoding='utf8')
en = encrypt_aes("123456",key,iv)
print(en)
print(decode_aes(en,key,iv))