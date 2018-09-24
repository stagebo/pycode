import requests
import json

session = requests.session()

if __name__ == "__main__":
    url = "https://ucp.douyucdn.cn/ucp.do"
    multi = [{"d":"","i":0,"rid":0,"u":"/member/login","ru":"","ac":"click_login_code","rpc":"page_home","pc":"","pt":1526260546820,"oct":1526260547210,"dur":0,"pro":"host_site","ct":"web","e":{"step":2,"fac":"","type":1,"rac":"show_login"},"av":"","up":""}]
    ret = session.post(url,data={"multi":json.dumps(multi),"v":"1.5"})
    print(ret.text)

    loginNew = "https://passport.douyu.com/iframe/loginNew"
    form_data = {
        "areaCode": "0086",
        "phoneNum":"17684117493",
        "password": "202cb962ac59075b964b07152d234b70",
        "geetest_challenge": "2f899832b06399c40295df5718dc4be5ce",
        "geetest_validate":"d8b963305e2a75ce59caace02fa0b4be",
        "geetest_seccode": "https://passport.douyu.com/member/login?",
        "client_id": "1",
        "sm_did": "WHJMrwNw1k/G7TO8IGojaeqUaf2cYW+t5rw/gTKBtW7xCBNJ/3h0c+qiHlL1lxUpbfTVx53/Xrf+4p1ZDeEDGD8bs/L4jlsZiyFQgNjqfW9f0EGCXmL17fg/GllaqVP3BzvTkg+lu6hW32SUWBGfzv/SMyd+w2X70yXN2jBARg2ym9tT3t6hyZNftG9Hf6lzVOldHq9BrL1c4jOYkjAH8HEvxLotb8xpELQnhfBPKWyr+PgElv2QRsGWKOIGULr211+sn3yjf99EMRRJ7n/5I4g==1487582755342",
        "did":"",
        "lang":"cn"
    }
    ret = session.post(loginNew,data=form_data)
    print(ret.json())


