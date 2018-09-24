# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
#     File Name:     qq_bot
#     Author:        wyb
#     Date:          2018/8/3 0003
#     Description:
# """
# __author__ = 'wyb'
#
# from qqbot import QQBot
#
#
# class MyQQBot(QQBot):
#     def onQQMessage(bot, contact, member, content):
#         if content == '-hello':
#             bot.SendTo(contact, '你好，我是QQ机器人')
#         elif content == '-stop':
#             bot.SendTo(contact, 'QQ机器人已关闭')
#             bot.Stop()
#
#
# myqqbot = MyQQBot()
# myqqbot.Login()
# myqqbot.PollForever()
# if __name__ == "__main__":
#     print("main")


from qqbot import _bot as bot
bot.Login(['-q', '1234'])