import inspect
import sys
import time
import datetime
import _ctypes
import pyautogui
import pywinauto
from evenbet_app_test_pywinauto.constants import *
from pywinauto import Desktop
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
import re

from evenbet_app_test_pywinauto.pages.PokerTablePage import PokerTablePage
from evenbet_app_test_pywinauto.pages.locators import WindowsLocators, find_element_or_none


def get_rect_center(rect):
    h_center = int((rect.left + rect.right)/2)
    v_center = int((rect.top + rect.bottom) / 2)
    return (h_center, v_center)

def is_inside_window(elem_rect, win_rect):
    if elem_rect.left < win_rect.left:
        return False
    if elem_rect.top < win_rect.top:
        return False
    if elem_rect.right > win_rect.right:
        return False
    if elem_rect.bottom > win_rect.bottom:
        return False
    return True


def dnd_scroll(dist):
    pyautogui.mouseDown(button='left')
    pyautogui.move(0, dist)
    pyautogui.mouseUp(button='left')


def ensure_element_disappears(element, timeout=0):
    time_start = time.time()
    while time.time() - time_start <= timeout:
        try:
            print(element.rectangle())
        except _ctypes.COMError as e:
            print(repr(e))
            return True
    print(time.time() - time_start)
    return False

def whoami():
    frame = inspect.currentframe()
    return inspect.getframeinfo(inspect.currentframe()).function

def some_func():
    print("hello")
    print(inspect.getframeinfo(inspect.currentframe()).function)
    print(sys._getframe(0).f_code.co_name)

application = pywinauto.Application(backend='uia').start(APP_PATH).\
                        connect(class_name_re=MAIN_WINDOW_CLASS_NAME_RE, timeout=30)

app_win = application.window(class_name_re=MAIN_WINDOW_CLASS_NAME_RE)
time_start = time.time()
print(app_win.child_window(class_name="QQuickPopupItem").children(control_type="MenuItem"))
print(time.time() - time_start)