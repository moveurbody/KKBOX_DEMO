# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 下午9:55
# @Author  : Yuhsuan
# @File    : action.py
# @Software: PyCharm Community Edition

import datetime
import time
import os

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from log_module import log
from desired_capabilities import desired_caps

driver = None
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 初始化appium driver, 以便可以做物件抓取
def driver_init():
    global driver
    log('[driver_init] start')
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    log('[driver_init] end')

def test():
    if wait('id','Notificatoin'):
        driver.find_element_by_id('Notification').click()
    else:
        # driver.find_element_by_accessibility_id('Open drawer').click()
        driver.find_element_by_accessibility_id('播放歌單').click()

def featured_today_special():
    driver.find_element_by_accessibility_id('播放歌單').click()


def skip_message():
    if wait('id','CONFIRM'):
        driver.find_element_by_id('CONFIRM').click()

def screen_shot():
    directory = '%s/' % os.getcwd()
    directory = directory+"result/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = now+'.png'
    path = directory+file_name
    print(path)
    driver.save_screenshot(path)

def home_screen():
    back()
    home()
    home()
    back()

def home():
    driver.press_keycode(3)

def back():
    driver.press_keycode(4)

def enter():
    driver.press_keycode(66)

def sleep(x):
    time.sleep(x)

def wait(type=None,el=None,time=None):
    if type == 'id':
        type = By.ID
    elif type == 'class':
        type = By.CLASS_NAME
    elif type == 'name':
        type = By.NAME
    elif type == 'tag':
        type = By.TAG_NAME
    elif type == 'xpath':
        type = By.XPATH
    else:
        type = By.ID

    if time == None:
        time = 5

    try:
        waite_element = WebDriverWait(driver,time).until(EC.presence_of_element_located((type,el)))
        return True
    except Exception as e:
        screen_shot()
        print("[Error] The element: %s can't be found." % (el),e)
        return False

# com.skysoft.kkbox.android: id / drawerItem_layout
# My Library
# Discover
# Radio
# People
# Setting
# Notification