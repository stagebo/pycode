import requests,json
#  https://github.com/xiaosimao/IP_POOL

def main(url,data):
    ret = requests.post(url, data=data)
    print(ret.text)
if __name__ == "__main__":
    url = 'http://172.16.15.37:8080/HelloWeb/login.jsp'
    main(url,data={"username":"admin","password":"123"})