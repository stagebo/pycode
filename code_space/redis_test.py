'''
__target__ = Redis 测试文件
'''
import redis

rd = redis.Redis(host='www.iotqsgf.com',port=6379,db=0,socket_timeout=10)
print('start...')
rd.set('t','abc123')
print(rd.get('t'))