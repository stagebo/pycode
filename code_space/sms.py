#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     sms
    Author:        wyb
    Date:          2018/9/29 0029
    Description:   发送短信
"""

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import configparser

cf = configparser.ConfigParser()
cf.read("../application.conf",encoding='utf-8')

# 短信应用SDK AppID
appid = cf.getint("sms", "appid")  # SDK AppID是1400开头

# 短信应用SDK AppKey
appkey = cf.get("sms", "appkey")

# 短信模板ID，需要在短信应用中申请
template_id =  cf.getint("sms", "template_id")  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请

# 签名
sms_sign = "眼若秋波"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`

def send_msg(phone_num,msg):
    sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
    ssender = SmsSingleSender(appid, appkey)
    try:
        result = ssender.send(sms_type, 86, phone_num,
            f"您的登陆验证码为：{msg}，请在2分钟内填写。", extend="", ext="")
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

    print(result)

if __name__ == "__main__":

    # 需要发送短信的手机号码
    phone_numbers = [cf.getint("sms", "phone_numbers")]
    send_msg(phone_numbers[0],'hahh')
    print("main")