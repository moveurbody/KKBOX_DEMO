# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 下午10:07
# @Author  : Yuhsuan
# @File    : main.py
# @Software: PyCharm Community Edition

from action import *
from log_module import log

driver_init()

delay()
# play
featured_today_special()

# open setting
menu()
delay()
menu_setting()
scroll_down()
scroll_up()
delay()
back()

# open Notification
menu()
delay()
menu_notification()
delay()
back()