# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 下午10:07
# @Author  : Yuhsuan
# @File    : main.py
# @Software: PyCharm Community Edition

from action import *
from log_module import log
import unittest

class kkbox(unittest.TestCase):
    def setUp(self):
        driver_init()

    def tearDown(self):
        pass

    def test_open_setting(self):
        # open setting
        menu()
        delay()
        menu_setting()
        scroll_down()
        scroll_up()
        delay()
        back()

    def test_open_notification(self):
        # open Notification
        menu()
        delay()
        menu_notification()
        delay()
        back()

    def test_play_music(self):
        featured_today_special()

    def test_search(self):
        # search
        log('search start')
        delay(1)
        menu()
        delay(1)
        menu_discover()
        delay(1)
        menu_discover_search()
        delay(1)
        menu_discover_search_input('Linkin Park')
        delay(1)
        enter()
        delay(1)
        press('com.skysoft.kkbox.android:id/layout_view')
        delay(1)
        press('com.skysoft.kkbox.android:id/layout_round_control_bar')
        delay(1)
        play_pause('play')
        screen_shot()
        delay(10)
        play_pause('stop')
        screen_shot()
        delay(5)

    def test_play(self):
        delay(3)
        play_pause('play')
        delay(3)
        play_pause('stop')
        delay(3)
        play_pause('stop')
        delay(3)
        play_pause('play')

if __name__ == '__main__':
    unittest.main()