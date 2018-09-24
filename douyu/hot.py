import requests,json,sys,os,traceback
import config
session = requests.session()


if __name__ == "__main__":

    print(123123)
    while True:
        idx = 0
        success = 0
        url = 'http://pxy.urmyall.xyz'
        ret = requests.get(url).json()
        print(ret)
        for ips in ret:

            ip = ips[0]
            port = ips[1]
            # print(ip,port)
            # url = "http://www.cnblogs.com/wyongbo/p/jnaTest.html"
            # url = 'http://urmyall.xyz:9003/admin/ip_test'
            url = "https://www.douyu.com/search/?kw=1963337"
            data = {

            }
            proxies = {
                'http': 'http://%s:%s' % (ip, port),
                'https': 'http://%s:%s' % (ip, port)
            }
            header = config.get_header()
            header["Referer"] = "https://www.douyu.com/search/?kw=1963337"
            try:
                rets = session.request('get',url, proxies=proxies,data=data, timeout=5)
                ret_text = rets.content
                print(rets.status_code)
                url = "https://www.douyu.com/1963337"
                rets = session.request('get', proxies=proxies, data=data, timeout=5)
                ret_text = rets.content
                print(rets.status_code)
                print("**************************成功%s"%success)
                success += 1
            except:
                # traceback.print_exc()
                print("----------------------------------------------%s"%idx)
                idx += 1
                # session.request( method, url,
                #         params=None, data=None, headers=None, cookies=None, files=None,
                #         auth=None, timeout=None, allow_redirects=True, proxies=None,
                #         hooks=None, stream=None, verify=None, cert=None, json=None):
#{"error":0,"servers":[{"ip":"wsproxy.douyu.com","port":"6671"},{"ip":"wsproxy.douyu.com","port":"6672"},{"ip":"wsproxy.douyu.com","port":"6673"},{"ip":"wsproxy.douyu.com","port":"6674"},{"ip":"wsproxy.douyu.com","port":"6675"}],"h5_wsproxy":[{"domain":"dy2.douyu.com","port":"6671"}]}