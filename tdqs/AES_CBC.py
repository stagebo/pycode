#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     AES_CBC
    Author:        WYB
    Date:          2018/11/27 11:46:39
    Description:   
"""
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

def encode(text, key = bytes("tdqsgf8888!@#$%^", encoding='utf8'),iv=bytes("tdqsgf8888!@#$%^", encoding='utf8')):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    PADDING = '\0'
    pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
    AES_code = bytes(pad_it(text),encoding='utf8')
    code = cipher.encrypt(AES_code)
    base64_text = str((base64.encodebytes(code)).decode()).replace('\n','')
    return base64_text


def decode(text, key = bytes("tdqsgf8888!@#$%^", encoding='utf8'),iv=bytes("tdqsgf8888!@#$%^", encoding='utf8')):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    textb = base64.b64decode(text.encode('utf-8'))
    decrypted_text = cipher.decrypt(textb).decode('utf-8')
    decrypted_code = decrypted_text.rstrip('\0')
    return decrypted_code


key = bytes("tdqsgf8888!@#$%^",encoding='utf8')
iv = bytes("tdqsgf8888!@#$%^",encoding='utf8')
en = encode("123456",key,iv)
print(en)
print(decode(en,key,iv))