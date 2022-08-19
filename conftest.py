import datetime
import io
import os
import sys
import time

import PIL.Image
import allure
import pyautogui
import pytest
import pywinauto
from allure_commons.types import AttachmentType

from evenbet_app_test_pywinauto.constants import *
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.LoginPage import LoginPage
from evenbet_app_test_pywinauto.pages.locators import *

#pytest -s -v --tb=short --alluredir=allure

@pytest.fixture(scope='module')
def app():
    """This fixture opens application, authorizing in it, makes window full-screen and closes app in the end."""

    with allure.step("Start app and connect to it."):
        application = pywinauto.Application(backend='uia').start(APP_PATH).\
            connect(class_name_re=MAIN_WINDOW_CLASS_NAME_RE, timeout=30)
        app_win = application.window(class_name_re=MAIN_WINDOW_CLASS_NAME_RE)
        page = LoginPage(app_win)

    with allure.step("Find or open login window."):
        login_window = page.wait_for_login_window(timeout=3)
        if not login_window:
            main_page_login_button = page.wait_for_main_page_login_button(timeout=1)
            assert main_page_login_button, "No Login button on main page."
            main_page_login_button.click_input()
            login_window = page.wait_for_login_window(timeout=5)
        assert login_window, "Login window didn't appear neither at start nor after clicking Login button on main page."

    with allure.step("Find username and password fields and type data into them."):
        username_field = page.find_login_username_field()
        assert username_field, "No Username field on Login page"
        page.print_username_in_login_username_field(username_field)
        password_field = page.find_login_password_field()
        assert password_field, "No Password field on Login page"
        page.print_password_in_login_username_field(password_field)

    with allure.step("Find and click 'Login' button in login form."):
        login_btn = page.find_login_button()
        assert login_btn, "No Login button on Login page"
        login_btn.click_input()

    with allure.step("Check 'Show User Balance' button on main page."):
        show_user_balance_button = page.wait_for_show_user_balance_button(timeout=5)
        assert show_user_balance_button, "Show User Balance button didn't appear on Main page after login."

    with allure.step("Make window fullscreen."):
        fullscreen_btn = page.find_fullscreen_button()
        assert fullscreen_btn, "Right top fullscreen button is not detected."
        fullscreen_btn.click_input()

    yield app_win

    with allure.step("Close app."):
        application.kill()


@pytest.fixture(scope='module')
def test_app():
    application = pywinauto.Application(backend='uia').start(APP_PATH). \
        connect(class_name_re=MAIN_WINDOW_CLASS_NAME_RE, timeout=30)
    app_win = application.window(class_name_re=MAIN_WINDOW_CLASS_NAME_RE)
    yield app_win



#def make_screenshot():
import pickle

@pytest.fixture(scope="function")
def screenshot_report():
    feedback = {"window": None, "file_name": "", "status": "failed"}
    yield feedback
    if feedback['window'] and feedback['status'] == 'failed':
        window_rect = feedback['window'].rectangle()
        left = window_rect.left
        top = window_rect.top
        width = window_rect.right - window_rect.left
        height = window_rect.bottom - window_rect.top
        date = datetime.date.today()
        if not os.path.exists(f"reports/screenshots/{date}/"):
            os.makedirs(f"reports/screenshots/{date}/")
        name = feedback['file_name']
        name_and_path = f"reports/screenshots/{date}/{name}.jpg"
        pyautogui.screenshot(region=(left, top, width, height)).save(name_and_path)
        screenshot = PIL.Image.open(name_and_path)
        with io.BytesIO() as buf:
            screenshot.save(buf, 'jpeg')
            image_bytes = buf.getvalue()
            allure.attach(image_bytes, name)


def return_func_name():
    return sys._getframe(1).f_code.co_name


def mouse_input(element, duration=0):
    rect = element.rectangle()
    center_h = int((rect.right + rect.left) / 2)
    center_v = int((rect.bottom + rect.top) / 2)
    pyautogui.moveTo(center_h, center_v, duration)

def find_elem_by_text(elements, text):
    for elem in elements:
        if elem.window_text().strip().lower() == text.strip().lower():
            return elem
    return None


