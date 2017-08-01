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

# def test():
#     if wait('id','Notificatoin'):
#         driver.find_element_by_id('Notification').click()
#     else:
#         # driver.find_element_by_accessibility_id('Open drawer').click()
#         driver.find_element_by_accessibility_id('播放歌單').click()



# Menu
def menu():
    log('[menu][start]')
    driver.find_element_by_accessibility_id('Open drawer').click()
    log('[menu][end]')


# Menu -> Library
def menu_my_library():
    log('[menu_my_library][start]')
    driver.find_element_by_accessibility_id('My Library').click()
    log('[menu_my_library][end]')

# Menu -> Library -> All Songs
def menu_my_library_all():
    log('[menu_my_library_all][start]')
    driver.find_element_by_accessibility_id('ALL Songs').click()
    log('[menu_my_library_all][end]')

# Menu -> Library -> Offline Songs
def menu_my_library_offline():
    log('[menu_my_library_offline][start]')
    driver.find_element_by_accessibility_id('Offline Songs').click()
    log('[menu_my_library_offline][end]')

# Menu -> Library -> Play History
def menu_my_library_history():
    log('[menu_my_library_history][start]')
    driver.find_element_by_accessibility_id('Play History').click()
    log('[menu_my_library_history][end]')

# Menu -> Library -> Collected Songs
def menu_my_library_csong():
    log('[menu_my_library_csong][start]')
    driver.find_element_by_accessibility_id('Collected Songs').click()
    log('[menu_my_library_csong][end]')

# Menu -> Library -> Collected Albums
def menu_my_library_calbum():
    log('[menu_my_library_calbum][start]')
    driver.find_element_by_accessibility_id('Collected Albums').click()
    log('[menu_my_library_calbum][end]')
    
# Menu -> Library -> Collected Playlists
def menu_my_library_cplaylist():
    log('[menu_my_library_cplaylist][start]')
    driver.find_element_by_accessibility_id('Collected Playlists').click()
    log('[menu_my_library_cplaylist][end]')


# Menu -> Discover
def menu_discover():
    log('[menu_discover][start]')
    driver.find_element_by_accessibility_id('Discover').click()
    log('[menu_discover][end]')

# Menu -> Discover -> FEATURED
def menu_discover_featured():
    log('[menu_discover_featured][start]')
    driver.find_element_by_accessibility_id('FEATURED').click()
    log('[menu_discover_featured][end]')

# Menu -> Discover -> FEATURED -> Today Special
def featured_today_special():
    log('[featured_today_special][start]')
    driver.find_element_by_accessibility_id('播放歌單').click()
    log('[featured_today_special][end]')

# Menu -> Discover -> CHART
def menu_discover_chart():
    log('[menu_discover_chart][start]')
    driver.find_element_by_accessibility_id('CHART').click()
    log('[menu_discover_chart][end]')

# Menu -> Discover -> NEW
def menu_discover_new():
    log('[menu_discover_new][start]')
    driver.find_element_by_accessibility_id('NEW').click()
    log('[menu_discover_new][end]')

# Menu -> Discover -> GENRE&MOOD
def menu_discover_genre():
    log('[menu_discover_genre][start]')
    driver.find_element_by_accessibility_id('GENRE&MOOD').click()
    log('[menu_discover_genre][end]')


# Menu -> Radio
def menu_radio():
    log('[menu_radio][start]')
    driver.find_element_by_accessibility_id('Radio').click()
    log('[menu_radio][end]')


# Menu -> People
def menu_people():
    log('[menu_people][start]')
    driver.find_element_by_accessibility_id('People').click()
    log('[menu_people][end]')

# Menu -> People -> LOCAL
def menu_people_local():
    log('[menu_people_global][start]')
    driver.find_element_by_accessibility_id('LOCAL').click()
    log('[menu_people_global][end]')

# Menu -> People -> GLOBAL
def menu_people_global():
    log('[menu_people_global][start]')
    driver.find_element_by_accessibility_id('GLOBAL').click()
    log('[menu_people_global][end]')

def menu_people_global_more():
    log('[menu_people_global_more][start]')
    el = driver.find_elements_by_id('More')
    el[0].click()
    log('[menu_people_global_more][end]')


# Menu -> Setting
def menu_setting():
    log('[menu_setting][start]')
    driver.find_element_by_accessibility_id('Setting').click()
    log('[menu_setting][end]')

# Menu -> Notification
def menu_notification():
    log('[menu_notification][start]')
    driver.find_element_by_accessibility_id('Notification').click()
    log('[menu_notification][end]')



def skip_message():
    if wait('id','CONFIRM'):
        driver.find_element_by_accessibility_id('CONFIRM').click()

def scroll_down():
    driver.execute_script("mobile: scroll", {"direction": "down"})

def scroll_up():
    driver.execute_script("mobile: scroll", {"direction": "up"})

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

def delay(x=None):
    if x!=None:
        time.sleep(x)
    else:
        time.sleep(3)

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