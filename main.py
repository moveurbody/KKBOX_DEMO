# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 下午10:07
# @Author  : Yuhsuan
# @File    : main.py
# @Software: PyCharm Community Edition

from action import *
from log_module import log

driver_init()

sleep(5)

log('[featured_today_special][start]')
featured_today_special()
log('[featured_today_special][end]')