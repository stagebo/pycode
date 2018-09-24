import requests

'''
__target__ = 金山每日一句
'''

url = "http://open.iciba.com/dsapi/"
r = requests.get(url)
print(r.json())
