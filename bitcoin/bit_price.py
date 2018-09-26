#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    File Name:     bit_price
    Author:        wyb
    Date:          2018/8/31 0031
    Description:   获取比特币价格
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃       ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃  永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
__author__ = 'wyb'
from databot.flow import Pipe, Timer
from databot.botframe import BotFrame
from databot.http.http import HttpLoader


def main():
    Pipe(
        Timer(delay=2),  # send timer data to pipe every 2 sen
        "http://api.coindesk.com/v1/bpi/currentprice.json",  # send url to pipe when timer trigger
        HttpLoader(),  # read url and load http response
        lambda r: r.json['bpi']['USD']['rate_float'],  # read http response and parese as json
        print,  # print out
    )

    BotFrame.render('simple_bitcoin_price')
    BotFrame.run()

if __name__ == "__main__":
    print("main")

    main()