import requests,json
header = {
    "User-Agent":""

}
#  https://github.com/xiaosimao/IP_POOL
if __name__ == "__main__":
    ip = '124.207.178.174'
    port = 9090
    proxies = {
        'http': 'http://%s:%s'%(ip,port),
        'https': 'http://%s:%s'%(ip,port)
    }
    url = "https://www.douyu.com/search/?kw=1963337"
    ret = requests.get("http://urmyall.xyz:9003/admin/ip_test",proxies=proxies,timeout=0.2)
    # ret = requests.get(url,proxies=proxies,headers=header)
    print(ret.text)