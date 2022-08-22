import inspect
import sys
import time
import datetime
import _ctypes
import pyautogui
import pywinauto
from evenbet_app_test_pywinauto.constants import *
from evenbet_app_test_pywinauto.utils import mouse_input, timer
from pywinauto import Desktop
from evenbet_app_test_pywinauto.pages import locators
from evenbet_app_test_pywinauto.pages.MainPage import BasePage
import re
from evenbet_app_test_pywinauto.pages.PokerPage import PokerPage
from evenbet_app_test_pywinauto.pages.PokerTableWindow import PokerTableWindow
from evenbet_app_test_pywinauto.pages.locators import WindowsLocators, find_element_or_none


application = pywinauto.Application(backend='uia').start(APP_PATH).\
                        connect(class_name_re=MAIN_WINDOW_CLASS_NAME_RE, timeout=30)
app_win = application.window(class_name_re=MAIN_WINDOW_CLASS_NAME_RE)

login_btn = app_win.child_window(class_name_re="PLoginButton_QMLTYPE_*")
print(login_btn)

