#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     req
    Author:        wyb
    Date:          2018/9/23 0023
    Description:
"""
from geetest import *


class PcGetCaptchaHandler(SessionBaseHandler):
    def get(self):
        user_id = 'test'
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        status = gt.pre_process(user_id, JSON_FORMAT=0, ip_address="127.0.0.1")
        if not status:
            status = 2
        self.session[gt.GT_STATUS_SESSION_KEY] = status
        self.session["user_id"] = user_id
        response_str = gt.get_response_str()
        self.write(response_str)