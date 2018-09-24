import requests,json,sys,os

if __name__ == "__main__":
    url = 'http://pxy.urmyall.xyz'
    ret = requests.get(url).json()
    print(ret)
    for ips in ret:
        ip = ips[0]
        port = ips[1]

        url = "http://www.cnblogs.com/wyongbo/p/jnaTest.html"
        # url = 'http://urmyall.xyz:9003/admin/ip_test'
        proxies = {
            'http': 'http://%s:%s' % (ip, port),
            'https': 'http://%s:%s' % (ip, port)
        }
        rets = requests.get(url, proxies=proxies)
        print(rets.status_code)