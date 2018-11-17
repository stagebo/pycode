#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     ybs
    Author:        WYB
    Date:          2018/11/16 08:19:00
    Description:   
"""
import os, sys
import requests,json,hashlib
import xlwt
from datetime import *
import traceback

url = 'http://www.iotqsgf.com:9102/1.0.1/{}'.format
# url = 'http://172.16.72.53:9102/1.0.1/{}'.format

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
    # wb = xlwt.Workbook(encoding='utf-8')
    wb = xlwt.Workbook()
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
                print(i,j,data[i])
                v = data[i][j] # "" if (data[i][j] == None or str(data[i][j]).lower() == "none") else data[i][j]
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



class YBS():

    def login(self, username,password):
        login_url = "https://apicloud.yiboshi.com/api-study/v1/users/login"
        login_url = "http://api.yiboshi.com/api/study/student/login"
        data = {
            "username": username,
            "password": self.md5(password)  # ""e10adc3949ba59abbe56e057f20f883e"
        }
        ret = requests.post(login_url, data = data)
        print(ret.text)
        ret_data = json.loads(ret.text)
        self.user_data = ret_data['data']
        return  ret.status_code,ret.text

    def list_trainning(self,userId,excludeExpire="true",trainingWay=1):
        url = "http://api.yiboshi.com/api/study/student/listStudentTraining?userId=%s&excludeExpire=%s&trainingWay=%s"%(userId,excludeExpire,trainingWay)
        ret = self.get(url)
        return json.loads(ret.text)


    def list_course(self,uid,tid):

        url = f"http://api.yiboshi.com/api/study/student/listStudentProjCourseInfoAndStatus?userId={uid}&trainingId={tid}&courseState=&compulsory=&keyword=";#获取课程列表
        ret = self.get(url)
        print(uid,tid)
        print(ret.status_code)
        return json.loads(ret.text)


    def pass_exam(self,uid,tid,pid,cid):
        url = f"http://api.yiboshi.com/api/WebApp/commitCoursePracticeScore?trainingId={tid}&projectId={pid}&userId={uid}&courseId={cid}&score=100&versionId=3.1"
        ret = self.get(url)
        print(ret.text)
        return json.loads(ret.text)


    def get_answer(self,cid):
        url = f"http://examapi.yiboshi.com/course/practices/{cid}?callback=P"
        ret = self.get(url)
        return ret.text

    def get(self, url,data={}):
        ret = requests.get(url, data=data)
        return ret


    def post(self, url,data={}):
        ret = requests.post(url, data=data)
        return  ret


    def md5(self, str):
        m1 = hashlib.md5()
        m1.update(str.encode("utf-8"))
        token = m1.hexdigest()
        return token

if __name__ == "__main__":
    # sys.setdefaultencoding('utf-8')

    file = open("ybs_%s.log"%datetime.now().strftime("%Y%m%d%H%M%S"),'w',encoding='utf8')
    username = "15085927614"
    # username = "520112196902182110"
    password = "123456" # e10adc3949ba59abbe56e057f20f883e
    # 邓立菊 520112196902182110，密室123456。
    ybs = YBS()
    ybs.login(username,password)
    uid = ybs.user_data['studentInfo']['id']
    train_list = ybs.list_trainning(uid)
    print(train_list)

    tid_list = [i['id'] for i in train_list['data']['list']]
    print(tid_list)
    idx = 1
    ans_data = [['题目','答案',"A","B","C","D","E"]]
    for train in train_list['data']['list']:
    # for tid in tid_list:
        tid = train['id']
        tname = train['name']
        course_info_list = ybs.list_course(uid,tid)
        for project in course_info_list['data']['list']:
            pid = project['id']
            pname = project['projectName']
            for course in project['courseList']:
                try:
                    cid = course['id']
                    cname = course['name']
                    cfid = course['courseFieldID']
                    # print(course)

                    # ret = ybs.pass_exam(uid,tid,pid,cid)

                    # msg = "%s||%s||%s||%s\r\n"%(tname,pname,cname,str(ret))
                    # print(msg)
                    # file.write(msg)

                    ans_ret = ybs.get_answer(cfid)
                    ans_ret = ans_ret[:-2]
                    ans_ret = ans_ret[ans_ret.find("(")+1:]
                    ans_ret = json.loads(ans_ret)
                    for question in ans_ret['data']:
                        ana = question['ana']
                        stem = question['stem']
                        ans = question['ans']
                        opts = question['opts']
                        qs_str = "%s||%s||%s\r\n"%(ana,ans,'$$'.join(["##".join([i['opt'],i['ctnt']]) for i in opts]))
                        d = [ana,ans] + [i['ctnt'] for i in opts]
                        ans_data.append(d)
                        file.write("%s、【%s】%s\n"%(idx,ans,stem))
                        for opt in opts:
                            file.write("    %s、%s\n"%(opt['opt'],opt['ctnt']))
                        file.write("解释：【%s】\n\n"%ana)
                        idx += 1
                        # file.write(qs_str)
                    print(ans_ret)
                except:
                    traceback.print_exc()
                    print("=============================")
    # create_excel([ans_data],"ans.xls",["答案"])
    file.flush()
    file.close()