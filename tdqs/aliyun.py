import json
import requests


url = 'http://localhost:7003/1.0.0/{}'.format

def token(func):
    def wapper(*args, **kwargs):
        if args[0].token is None:
            args[0].login()
        return func(*args, **kwargs)
    return wapper


class Test:

    def __init__(self):
        self.token = None

    def login(self):
        print('login',url('login'))
        tk = requests.post(url('login'),
                           data=json.dumps({'username':
                                                "13163063175", 'password': 'a74f5b9d995be2c2633a64322ee61ecd','app':0}))
        print(tk,tk.status_code,tk.text)
        self.token = json.loads(
            tk.text
        )["sessionToken"]

    # @token
    def get(self, api, **kw):
        print(url(api))
        ret = requests.get(url(api), params=kw, headers={"Session-Token": self.token})
        return ret.text,ret.status_code

    # @token
    def post(self, api, data={}):
        print(url(api))
        ret = requests.post(url(api), data=json.dumps(data), headers={"Session-Token": self.token})
        return ret.text,ret.status_code


if __name__ == "__main__":
    # print(Test().get('query_t')) # ERROR ID
    T = Test()
    T.login()
    # cmd='ehco ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBiYtfaRP/WZl+t+wNxUqjzTqAGRJKfv/u5EvEEpFV//34d2wtIDxRslTyd1DsIrIVABjIokr4pgadH50eqkM+DQfhhjVaDG0tq80U5QLgEOtjJc+KVmvIyiIiiRhDSNrXqEWLG44H/a0DLgXw6tBG2FPQUVZG86ucuw21zn00z4oh+OOV3KP6itxAYeKGWYfCR/iQjIPAf2456P2pfekG+BRlaY6dCeqlCtThRuHxY4zoRxxI7Ovf+aCDimyo3SwYZWczlgZtkF46TDraUvmnSKva//BmmOt5cEZct1Sj00Vm5nWusJSH0PINDnyu7fmt0HxcldhI2hxPQaOeuEQP 571051761@qq.com >> /home/git/.ssh/authorized_keys'
    #cmd = 'chmod 700 /home/git/.ssh/authorized_keys'
    # cmd = 'cat /home/git/.ssh/authorized_keys'
    #cmd = "echo -e 123 > /home/git/t.sh"
    #cmd = "rm -f /home/git/t.sh"
    # print(T.get('query_business_test?c=%s'%cmd,))