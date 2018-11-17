#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     right_check
    Author:        WYB
    Date:          2018/11/13 15:41:34
    Description:
"""

import requests
import json
from datetime import *
import xlwt
from PIL import Image
import pytesseract
import random
import hashlib
from Crypto.PublicKey import RSA
import base64
import sys

import cv2
from matplotlib import pyplot as plt
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5


def check_contain_chinese(check_str):
    '''
    判断是否包含中文
    :param check_str:
    :return:
    '''
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def create_excel(datas, file_name, sheets=[]):
    """
    写入数据到Excel，并合并单元格
    xlwt缺点：
        版本
        只能处理Excel97-2003或Excel 97之前版本的xls格式
        存储数据过大
        存储数据过大时，会报错Exception: String longer than 32767 characters
    :param data:
    :param merge_info:
    :param file_name:
    :param hdc:
    :param sheetname:
    :return:
    """
    wb = xlwt.Workbook(encoding='utf-8')
    # 设置单元格样式
    # height 300,
    style = xlwt.easyxf(
        '''
        font:
            height 280,
            name 宋体,
            colour_index black,
            bold off,
            italic off;
        align:
            wrap off,
            vert centre,
            horiz centre;
        borders:
            left 1,
            right 1,
            top 1,
            bottom 1;
        alignment:
            horz center,
            vert center;
        ''')
    # style.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    # style.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    if len(datas) != len(sheets):
        sheets = ["sheet%s"%(i+1) for i in range( len(datas))]
    for sheetidx,data in enumerate(datas) :
        # 创建sheet
        sheetname = sheets[sheetidx]
        sheet = wb.add_sheet(sheetname, cell_overwrite_ok=True)

        # 记录列宽
        col_widths = [3 for i in range(0, max([len(j) for j in data]))]
        for i in range(len(data)):
            for j in range(len(data[0])):
                v = "" if (data[i][j] == None or str(data[i][j]).lower() == "none") else data[i][j]
                len_dataij = 0
                for s in str(data[i][j]):
                    if u'\u4e00' <= s <= u'\u9fff': # 判断是否有中文
                        len_dataij += 2.9
                    else:
                        len_dataij += 1.3
                col_widths[j] = max(col_widths[j], int(len_dataij))
                # print(data[i])
                # pattern = xlwt.Pattern()
                # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
                # status = int(data[i][-1])
                # if  status == 403:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['yellow']  # 设置单元格背景色为黄色
                # elif status == 401 or status == 200:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['green']
                # elif status == 500:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
                # else:
                #     pattern.pattern_fore_colour = xlwt.Style.colour_map['purple_ega']  # 设置单元格背景色为黄色
                # style.pattern = pattern
                maxlen = 32766
                v = v if (len(str(v)) < maxlen) else v[0:maxlen]

                sheet.write(i, j, v, style)

        # 设置列宽
        for i in range(len(col_widths)):
            wid = min(300 * (col_widths[i] + 1), 65535)
            sheet.col(i).width = wid


    wb.save(file_name)
    return True


# url = 'http://www.iotqsgf.com:9102/1.0.1/{}'.format
# url = 'http://172.16.72.53:9102/1.0.1/{}'.format
url = "https://172.16.72.166/1.0.1/{}".format

def login(data):
    ret = requests.post(url("login"), data = data,verify=False)
    return  ret.status_code,ret.text


def get(api,token):
    ret = requests.get(url(api),  headers={"Session-Token": token},verify=False)
    return ret.status_code


def post(api,token):
    ret = requests.post(url(api), headers={"Session-Token": token},verify=False)
    return  ret.status_code


def http(api,token,method):
    return get(api,token) if(method=="GET") else post(api,token)

def check():
    data_dic = {"问题接口":[]}
    data = []
    for i,ups in enumerate(ls):
        for j,token in enumerate(tokens):
            for u,method in ups:
                ret = http(u,token,method)
                print(u,users[i],users[j], ret)
                if ret not in data_dic.keys():
                    data_dic[ret] = []
                data_dic[ret].append([u,users[i],users[j],ret])
                data.append([u,users[i],users[j],ret])
                # 以下为问题接口
                # k = [i[0] for i in ls[j]]
                # print(u,u in k,k,)
                if ret == 500 or \
                        (ret == 200 and i!=j and u not in [i[0] for i in ls[j]]) or \
                        (ret not in [200,500,401]):
                    data_dic['问题接口'].append([u,users[i],users[j],ret])
    datas = [data]
    sheets = ['汇总']
    for key in data_dic.keys():
        datas.append(data_dic[key])
        sheets.append('详情-%s'%key)

    for d in datas:
        d.insert(0,['接口名称',"接口所有者",'接口调用者','响应状态码'])
    now = datetime.now()
    file_name = "权限测试%s.xls"%(now.strftime("%Y-%m%d-%H%M%S"))
    create_excel(datas, file_name, sheets=sheets)


def get_img(file,url):
    html = requests.get(url,verify=False)
    with open(file, 'wb') as file:
        file.write(html.content)


def img2string(file):

    # pytesseract.pytesseract.tesseract_cmd = 'E:\\Program Files\\tesseract-ocr\\tesseract-3.0.2\\Tesseract-OCR\\tesseract.exe'
    # # pytesseract.pytesseract.tesseract_cmd = 'E:\\Program Files\\tesseract-ocr\\tesseract-4.0\\Tesseract-OCR\\tesseract.exe'
    # text = pytesseract.image_to_string(Image.open(file), lang='eng')
    # print("result:", text)
    # return text

    while True:
        sys.path.append("../code_space")
        img = cv2.imread(file)
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

        # plt.subplot(121), plt.imshow(img)
        # plt.subplot(122)
        plt.imshow(dst)
        plt.show()
        text = input("请输入验证码：")
        if text != "n":
            return text

def get_img_ret(url):
    fn = "veid.png"
    get_img(fn,url)
    return img2string(fn)

def md5(str):
    m1 = hashlib.md5()
    m1.update(str.encode("utf-8"))
    token = m1.hexdigest()
    return token


# RSA 加密
def encrypt_rsa(msg):
    md = md5(msg)
    with open('ghost-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(md.encode('utf8')))
        return cipher_text


# rsa解密
def decrypt(self,rsakey, encrypt_text):
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    return cipher.decrypt(base64.b64decode(encrypt_text), '')





sysmg = [
    ("get_users","GET"),
    ("get_lock_users","GET"),
    ("insert_user","POST"),
    ("insert_user_auth","POST"),
    ("checkpassword","POST"),
    ("update_user","POST"),
    ("get_user_role","GET"),
    ("get_user_auth","GET"),
    ("update_user_auth","POST"),
    ("update__state","POST"),
    ("update_user_lock","POST"),
    ("update_user_password","POST"),
    ("get_department","GET"),
    ("get_default_options","GET"),
    ("set_default_options","POST"),
    ("event_front","POST")
]

logmg = [
    ("get_users","GET"),
    ("get_user_auth","GET"),
    ("get_event_sys","GET"),
    ("get_event_type","GET"),
    ("get_department","GET"),
    ("get_event_alert","GET"),
    ("get_event_detail_unread","GET"),
    ("get_event_biz","GET"),
    ("get_event_type","GET"),
    ("get_department","GET"),
    ("get_event_detail_unread","GET"),
    ("get_event_count_by_user","GET"),
    ("get_event_report_by_time","GET"),
    ("get_event_report_by_type","GET"),
    ("get_event_report_by_user","GET"),
    ("update_user_password","POST"),
    ("event_front","POST")
]

pzy = [
    ("set_file_ext","POST"),
    ("get_file_ext","GET"),
    ("get_users","GET"),
    ("get_user_auth","GET"),
    ("update_user_password","POST"),
    ("event_front","POST")

]

czy = [
    ("update_user_password","POST"),
    ("query_all_grid_list","GET"),
    ("query_element_enum","GET"),
    ("query_map_config_json_by_sid","GET"),
    ("query_layers_info_by_sid","GET"),
    ("query_style_info_by_sid","GET"),
    ("query_layers_data_by_layers_info","POST"),
    ("query_report_meta_by_tablename","POST"),
    ("query_platform_report_data","POST"),
    ("query_report_data_page","POST"),
    ("query_element_by_elementname","POST"),
    ("query_element_info_by_seid","POST"),
    ("query_files_by_area_module","POST"),
    ("uploads","POST"),
    ("downloads","POST"),
    ("delete_file_common","POST"),
    ("get_user_auth","GET"),
    ("get_users","GET"),
    ("event_front","POST")
]

ls = [set(sysmg),set(logmg),set(pzy),set(czy)]

users = ["系统管理员","审计管理员","业务配置员","业务操作员"]

tokens = ['','','','']

# print(post("update__state","K6WidUPW+Fqprbv+6LeJ095nH6Wftt7L+q94RmOahwQ="))
if __name__ == "__main__":
    veid = "9989" #random.randint(9999)+100000 # 904963
    ur = url("get_vecode?veid=%s"%veid)
    us = [
        ("wsmg","Test1234"),
        ("wlogmg","Test1234"),
        ("wpzy","Test1234"),
        ("wczy","Test1234")
    ]
    for i,u in enumerate(us):
        while True:
            # vcode = get_img_ret(ur)
            data = {
                "username": u[0],
                "vecode": "9989",#vcode,
                "veid": veid,
                "password": encrypt_rsa(u[1]).decode(),
                "app": "0"
            }
            ret = login(json.dumps(data))
            print(u,ret)
            try:
                d = json.loads(ret[1])
                if "sessionToken" in d.keys():
                    tokens[i] = d["sessionToken"]
                    break
            except:
                print(ret)
                # sys.exit(1)
    print(tokens)
    check()













