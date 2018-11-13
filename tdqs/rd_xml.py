#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     rd_xml
    Author:        WYB
    Date:          2018/11/12 09:41:31
    Description:   
"""
try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET
import base64
import json
def _create_excel(data, file_name, sheetname="sheet1"):
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
    style.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    # 创建sheet
    sheet = wb.add_sheet(sheetname, cell_overwrite_ok=True)

    # 记录列宽
    col_widths = [3 for i in range(0, max([len(j) for j in data]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            v = "" if (data[i][j] == None or str(data[i][j]).lower() == "none") else data[i][j]
            col_widths[j] = max(col_widths[j], len(str(data[i][j])))

            maxlen = 32766
            v = v if (len(str(v)) < maxlen) else v[0:maxlen]

            sheet.write(i, j, v, style)

    # 设置列宽
    # for i in range(len(col_widths)):
    #     wid = min(256 * (col_widths[i] + 1), 65535)
    #     sheet.col(i).width = wid


    wb.save(file_name)
    return True

import xlwt
import sys,os
tree = ET.parse("test.xml")
root = tree.getroot()
items = root.findall('item')
data = [["方法","接口","参数"]]
idx = 0
methods = []
for item in items:

    # print(item.find("path"))
    path = item.find("path").text
    m = "GET"
    req = item.find("request").text
    resp = item.find("response").text
    params = []
    pl = path.split("?")

    # print(req)
    # print(str(request))
    path_str = path
    if len(pl) > 1:
        path_str,ps = pl
        pms = ps.split("&")
        for pm in pms:
            params.append(pm.split("=")[0])

    if req:
        try:
            request = base64.b64decode(req.encode('utf-8')).decode('utf-8')
            headers = [i.replace('\r','') for i in request.split("\n") if i is not None]
            method,pth,http = headers[0].split(" ")

            params_header = headers[-1]
            m = method
            if "POST" in method:
                path_str = pth
            try:
                jd = eval(params_header)

                for k in jd.keys():
                    params.append(k)
            except:
                pass


        except:
            print('====================================')
            print(pl, req)
            print('====================================')
            # sys.exit(0)
    if resp:
        response = base64.b64decode(resp.encode('utf-8'))

    if len(path_str) > 3 and (path_str,m) not in methods and '/1.0.1/' in path_str and m != "OPTIONS":
        pmslist = [i for i in params if i != '_']
        methods.append((path_str,m))
        data.append((m,path_str,',&'.join(pmslist)))
        print(idx, path_str, pmslist)
        idx += 1

# data = list(set(data))

_create_excel(data, "interface.xls", sheetname="sheet1")
