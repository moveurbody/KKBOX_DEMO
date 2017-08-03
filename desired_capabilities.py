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
    # 'deviceName': 'QV707EXL0B',
    'platformName': 'Android',
    'platformVersion': '6.0',
    # 'platformVersion': '7.1.1',
    'appPackage': 'com.skysoft.kkbox.android',
    'noRest':True,
    'app': '/Users/yuhsuan/Desktop/Deepblu/KKBOX/com.skysoft.kkbox.android.apk',
    'unicodeKeyboard':True,
    'resetKeyboard':True,
    'language':'zh_TW',
    'locale': 'TW',
}

# appium --session-override --command-timeout 72000000 --no-reset
# /Users/yuhsuan/Library/Android/sdk/tools/emulator -netdelay none -netspeed full -avd Nexus_5_API_23
# . ~/Library/Android/sdk/export/tools/uiautomatorviewer