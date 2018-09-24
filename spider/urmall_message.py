import requests,json,sys,os,traceback
session = requests.session()


if __name__ == "__main__":
    while True:
        idx = 0
        success = 0
        url = 'http://pxy.urmyall.xyz'
        ret = requests.get(url).json()
        print(ret)
        for ips in ret:
            try:
                ip = ips[0]
                port = ips[1]
                print(ip,port)
                # url = "http://www.cnblogs.com/wyongbo/p/jnaTest.html"
                # url = 'http://urmyall.xyz:9003/admin/ip_test'
                url = "https://www.douyu.com/search/?kw=1963337"
                data = {

                }
                proxies = {
                    'http': 'http://%s:%s' % (ip, port),
                    'https': 'http://%s:%s' % (ip, port)
                }
                try:
                    rets = session.post(url, proxies=proxies,data=data, timeout=5)
                    ret_text = rets.content.decode('gbk')
                    print(rets.status_code,ret_text)
                    url = "https://www.douyu.com/1963337"
                    rets = session.post(url, proxies=proxies, data=data, timeout=5,)
                    ret_text = rets.content.decode('gbk')
                    print(rets.status_code, ret_text)
                    print("**************************成功%s"%success)
                except:
                    print("----------------------------------------------%s"%idx)
                idx += 1

            except:
                traceback.print_exc()
