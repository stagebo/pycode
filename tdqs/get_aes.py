# coding=utf-8
import sys
from Crypto.Cipher import AES
from Crypto import Random
import binascii

key = 'tdqsgf8888!@#$%^' #注意，此处必须是16个字符
iv = Random.new().read(16)


def encrypt(text):
     cipher1 = AES.new(key,AES.MODE_CFB,iv)
     encrypt_msg =  iv + cipher1.encrypt(text)
     return binascii.b2a_hex(encrypt_msg).decode()

def decrypt(text):
     msg = binascii.a2b_hex(text)
     iv =  msg[0:16]
     cipher2 = AES.new(key,AES.MODE_CFB,iv)
     decrypt_msg = cipher2.decrypt(msg[16:])
     return decrypt_msg.decode('utf-8')

def encrypt2(text):
     PADDING='\0'
     pad_it = lambda s: s+(16 - len(s)%16)*PADDING
     key ='1234567890000000'
     iv =  key
     cipher1 = AES.new(key,AES.MODE_CBC,iv)
     encrypt_msg = cipher1.encrypt(pad_it(text))
     return binascii.b2a_hex(encrypt_msg).decode()

def decrypt2(text):
     key ='1234567890000000'
     iv =  key
     msg = binascii.a2b_hex(text)
     cipher2 = AES.new(key,AES.MODE_CBC,iv)
     decrypt_msg = cipher2.decrypt(msg)
     return decrypt_msg.decode('utf-8')


if __name__ == '__main__':
    if len(sys.argv)<2:
            print("get_aes -e(-ee)[-d(-dd)] text")
            sys.exit(-1)

    cmd  = sys.argv[1]
    text = sys.argv[2]

    if cmd == '-e' and text !='':
         msg = encrypt(text)
         print('加密后的值为：',msg)
         sys.exit(0)

    if cmd == '-d' and text !='':
         msg = decrypt(text)
         print('解密后的值为：',msg)
         sys.exit(0)

    if cmd == '-ee' and text !='':
         msg = encrypt2(text)
         print('加密后的值为：',msg)
         sys.exit(0)

    if cmd == '-dd' and text !='':
         msg = decrypt2(text)
         print('解密后的值为：',msg)
         sys.exit(0)
