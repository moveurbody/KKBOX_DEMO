# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 下午9:48
# @Author  : Yuhsuan
# @File    : desired_capabilities.py
# @Software: PyCharm Community Edition
import os
import datetime

directory = '%s/' % os.getcwd()

desired_caps = {
    'deviceName': 'emulator-5554',
    'platformName': 'Android',
    'platformVersion': '6.0',
    'appPackage': 'com.skysoft.kkbox.android',
    'noRest':True,
    'app': '/Users/yuhsuan/Desktop/Deepblu/KKBOX/com.skysoft.kkbox.android.apk'
}

acc = '0937394494'
pwd = '1qaz2WSX3edc'

# appium --session-override --command-timeout 72000000 --no-reset