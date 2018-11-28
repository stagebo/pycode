#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     right_check
    Author:        WYB
    Date:          2018/11/13 15:41:34
    Description:  权限测试脚本
"""

import requests
import json
from datetime import *
import xlwt
from PIL import Image
import pytesseract
import hashlib
from Crypto.PublicKey import RSA
import base64
import traceback
import cv2
from matplotlib import pyplot as plt
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import sys,os
from Crypto.Cipher import AES


class RightCheck():

    def __init__(
            self,
            url='http://www.iotqsgf.com:9102/1.0.1/{}'.format,
            usr_pwd=[
                ("aqsmg", "Test123456", "系统管理员"),
                ("aqsj", "Test123456", "审计管理员"),
                ("aqpzy", "Test123456", "业务配置员"),
                ("aqczy", "Test123456", "业务操作员")
            ],
            aeskey="tdqsgf8888!@#$%^",
            aesiv="tdqsgf8888!@#$%^" ,
            rsapkfile = 'ghost-public.pem',
            veid="9989",
            vecode="9989",
            needvecode = False
    ):
        self.aeskey = aeskey
        self.aesiv = aesiv
        self.rsapkfile = rsapkfile
        self.url = url
        self.usr_pwd = usr_pwd
        self.users = [i[2] for i in usr_pwd]
        self.tokens = ["" for i in usr_pwd]
        self.veid = veid
        self.vecode = vecode
        self.needvecode = needvecode
        self.sysmg = [
            ("get_users", "GET"),
            ("get_lock_users", "GET"),
            ("insert_user", "POST"),
            ("insert_user_auth", "POST"),
            ("checkpassword", "POST"),
            ("update_user", "POST"),
            ("get_user_role", "GET"),
            ("get_user_auth", "GET"),
            ("update_user_auth", "POST"),
            # ("update__state","POST"),
            ("update_user_lock", "POST"),
            ("update_user_password", "POST"),
            ("get_department", "GET"),
            ("get_default_options", "GET"),
            ("set_default_options", "POST"),
            ("event_front", "POST")
        ]
        self.logmg = [
            ("get_users", "GET"),
            ("get_user_auth", "GET"),
            ("get_event_sys", "GET"),
            ("get_event_type", "GET"),
            ("get_department", "GET"),
            ("get_event_alert", "GET"),
            ("get_event_detail_unread", "GET"),
            ("get_event_biz", "GET"),
            ("get_event_type", "GET"),
            ("get_department", "GET"),
            ("get_event_detail_unread", "GET"),
            ("get_event_count_by_user", "GET"),
            ("get_event_report_by_time", "GET"),
            ("get_event_report_by_type", "GET"),
            ("get_event_report_by_user", "GET"),
            ("update_user_password", "POST"),
            ("event_front", "POST"),
            ("event_update_isread", "POST"),
            ("checkpassword", "POST"),
            ("event_update_isread","POST")

        ]
        self.pzy = [
            ("set_file_ext", "POST"),
            ("get_file_ext", "GET"),
            ("get_users", "GET"),
            ("get_user_auth", "GET"),
            ("update_user_password", "POST"),
            ("event_front", "POST"),
            ("checkpassword", "POST"),
        ]
        self.czy = [
            ("update_user_password", "POST"),
            ("query_all_grid_list", "GET"),
            ("query_element_enum", "GET"),
            ("query_map_config_json_by_sid", "GET"),
            ("query_layers_info_by_sid", "GET"),
            ("query_style_info_by_sid", "GET"),
            ("query_layers_data_by_layers_info", "POST"),
            ("query_report_meta_by_tablename", "POST"),
            ("query_platform_report_data", "POST"),
            ("query_report_data_page", "POST"),
            ("query_element_by_elementname", "POST"),
            ("query_element_info_by_seid", "POST"),
            ("query_files_by_area_module", "POST"),
            ("uploads", "POST"),
            ("downloads", "POST"),
            ("delete_file_common", "POST"),
            ("get_user_auth", "GET"),
            ("get_users", "GET"),
            ("event_front", "POST"),
            ("checkpassword", "POST"),
        ]
        self.ls = [set(self.sysmg), set(self.logmg), set(self.pzy), set(self.czy)]

    @staticmethod
    def check_contain_chinese(check_str):
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    @staticmethod
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

    @staticmethod
    def md5(str):
        m1 = hashlib.md5()
        m1.update(str.encode("utf-8"))
        token = m1.hexdigest()
        return token

    @staticmethod
    def rsa_decode(text, prk):
        cipher = Cipher_pkcs1_v1_5.new(prk)
        return cipher.decrypt(base64.b64decode(text), '')

    @staticmethod
    def rsa_encode(msg, rsapkfile):
        # md = RightCheck.md5(msg)
        with open(rsapkfile) as f:
            key = f.read()
            rsa_key = RSA.importKey(key)
            cipher = Cipher_pkcs1_v1_5.new(rsa_key)
            cipher_text = base64.b64encode(cipher.encrypt(msg.encode('utf8')))
            return cipher_text

    @staticmethod
    def aes_encode(text, key,iv):
        key = bytes(key,encoding='utf8')
        iv = bytes(iv,encoding='utf8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        PADDING = '\0'
        pad_it = lambda s: s + (16 - len(s) % 16) * PADDING
        AES_code = bytes(pad_it(text), encoding='utf8')
        code = cipher.encrypt(AES_code)
        base64_text = str((base64.encodebytes(code)).decode()).replace('\n', '')
        return base64_text

    @staticmethod
    def aes_decode(text,  key,iv):
        key = bytes(key, encoding='utf8')
        iv = bytes(iv, encoding='utf8')
        cipher = AES.new(key, AES.MODE_CBC, iv)
        textb = base64.b64decode(text.encode('utf-8'))
        decrypted_text = cipher.decrypt(textb).decode('utf-8')
        decrypted_code = decrypted_text.rstrip('\0')
        return decrypted_code

    @staticmethod
    def get_file(file, url):
        html = requests.get(url,verify=False)
        with open(file, 'wb') as file:
            file.write(html.content)

    @staticmethod
    def img2string(file):
        # 验证码图片识别
        # pytesseract.pytesseract.tesseract_cmd = 'E:\\Program Files\\tesseract-ocr\\tesseract-3.0.2\\Tesseract-OCR\\tesseract.exe'
        # # pytesseract.pytesseract.tesseract_cmd = 'E:\\Program Files\\tesseract-ocr\\tesseract-4.0\\Tesseract-OCR\\tesseract.exe'
        # text = pytesseract.image_to_string(Image.open(file), lang='eng')
        # print("result:", text)
        # return text

        while True:
            img = cv2.imread(file)
            dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
            plt.imshow(dst)
            plt.show()
            text = input("请输入验证码：")
            plt.close()
            if os.path.isfile(file):
                os.remove(file)
            if text != "n":
                return text

    def get(self, api, token):
        ret = requests.get(self.url(api),  headers={"Session-Token": token},verify=False)
        return ret.status_code

    def post(self, api,token):
        ret = requests.post(self.url(api), headers={"Session-Token": token},verify=False)
        return  ret.status_code

    def http(self, api, token, method):
        return self.get(api,token) if(method=="GET") else self.post(api,token)

    def get_img_ret(self, url):
        fn = "veid.png"
        self.get_file(fn,url)
        return self.img2string(fn)

    def check(self):
        data_dic = {"问题接口": []}
        data = []
        for i, ups in enumerate(self.ls):
            for j, token in enumerate(self.tokens):
                for u, method in ups:
                    ret = self.http(u, token, method)
                    print(u, self.users[i], self.users[j], ret)
                    if ret not in data_dic.keys():
                        data_dic[ret] = []
                    data_dic[ret].append([u, self.users[i], self.users[j], ret])
                    data.append([u, self.users[i], self.users[j], ret])
                    # 以下为问题接口
                    # k = [i[0] for i in ls[j]]
                    # print(u,u in k,k,)
                    if ret == 500 or \
                            (ret == 200 and i != j and u not in [i[0] for i in self.ls[j]]) or \
                            (ret not in [200, 500, 401]):
                        data_dic['问题接口'].append([u, self.users[i], self.users[j], ret])
        datas = [data]
        sheets = ['汇总']
        for key in data_dic.keys():
            datas.append(data_dic[key])
            sheets.append('详情-%s' % key)

        for d in datas:
            d.insert(0, ['接口名称', "接口所有者", '接口调用者', '响应状态码'])
        now = datetime.now()
        file_name = "权限测试%s.xls" % (now.strftime("%Y-%m%d-%H%M%S"))
        self.create_excel(datas, file_name, sheets=sheets)

    def login(self,users):
        '''
        登录数据：
            密码用MD5加密再用RSA加密
            请求数据用AES/CBC/ZeroPadding 加密
            返回数据AES/CBC/ZeroPadding 解密
        :param users:
        :return:
        '''
        veid = self.veid # random.randint(9999)+100000 # 904963
        veur = self.url("get_vecode?veid=%s" % veid)
        for i, u in enumerate(users):
            while True:
                # 获取图形验证码
                if self.needvecode:
                    vcode = self.get_img_ret(veur)
                else:
                    vcode = self.vecode
                data = {
                    "username": u[0],
                    "vecode": vcode,  # vcode,
                    "veid": veid,
                    "password": self.rsa_encode(self.md5(u[1]),self.rsapkfile).decode(),
                    "app": "0"
                }

                data = json.dumps(data)
                print("登陆前加密前：", data)
                endata = self.aes_encode(data,self.aeskey,self.aesiv)
                print("登陆前加密后：", endata)
                logindata = json.dumps({"data":endata})
                print("登录数据：",logindata)

                http_ret = requests.post(self.url("login"), data=logindata, verify=False)
                ret = http_ret.status_code,http_ret.text
                if ret[0] != 200:
                    print(ret)
                    print("请求失败")
                    return
                try:
                    d = json.loads(ret[1])
                    print("登录返回值:", d)
                    data = d['result_m']
                    dd = self.aes_decode(data, self.aeskey,self.aesiv)
                    print("返回值解密后-TEXT：", dd)
                    ret_data = eval(dd)
                    print("返回值解密后-JSON:", ret_data)
                    if "sessionToken" in ret_data.keys():
                        self.tokens[i] = ret_data["sessionToken"]
                        break
                except:
                    traceback.print_exc()
                    print("ERROR", ret)
                    return

    def run(self):
        self.login(self.usr_pwd)
        print("登录结果：",self.tokens)
        self.check()


if __name__ == "__main__":
    usr_pwd = [
            ("aqsmg", "Test123456","系统管理员"),
            ("aqsj", "Test123456","审计管理员"),
            ("aqpzy", "Test123456","业务配置员"),
            ("aqczy", "Test123456","业务操作员")
        ]
    # usr_pwd = [
    #         ("sysmg", "Admin123456","系统管理员"),
    #         ("wlogmg", "Test1234","审计管理员"),
    #         ("aqpzy", "Test1234","业务配置员"),
    #         ("loadrunner_19", "Admin123456","业务操作员")
    #     ]
    right = RightCheck(
        url='https://192.168.91.140/1.0.1/{}'.format,
        # url='http://www.iotqsgf.com:9102/1.0.1/{}'.format,
        usr_pwd=usr_pwd,
        aeskey="tdqsgf8888!@#$%^",
        aesiv="tdqsgf8888!@#$%^",
        rsapkfile='ghost-public.pem',
        veid="9989",
        vecode="9989",
        needvecode = False
    )
    right.run()













