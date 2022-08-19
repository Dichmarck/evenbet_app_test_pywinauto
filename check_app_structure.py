import inspect
import sys
import time
import datetime
import _ctypes
import pyautogui
import pywinauto
from evenbet_app_test_pywinauto.constants import *
from evenbet_app_test_pywinauto.conftest import mouse_input
from pywinauto import Desktop
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
import re

from evenbet_app_test_pywinauto.pages.PokerPage import PokerPage
from evenbet_app_test_pywinauto.pages.PokerTablePage import PokerTablePage
from evenbet_app_test_pywinauto.pages.locators import WindowsLocators, find_element_or_none


def get_rect_center(rect):
    h_center = int((rect.left + rect.right)/2)
    v_center = int((rect.top + rect.bottom) / 2)
    return (h_center, v_center)


application = pywinauto.Application(backend='uia').start(APP_PATH).\
                        connect(class_name_re=MAIN_WINDOW_CLASS_NAME_RE, timeout=30)
app_win = application.window(class_name_re=MAIN_WINDOW_CLASS_NAME_RE)

time_start = time.time()


print(time.time() - time_start)






