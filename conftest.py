import time
import allure
import pytest
import pywinauto
from evenbet_app_test_pywinauto.constants import *
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.LoginPage import LoginPage
from evenbet_app_test_pywinauto.pages.locators import *


@pytest.fixture(scope='class')
def app():
    with allure.step("Start app and connect to it."):
        application = pywinauto.Application(backend='uia').start(APP_PATH).connect(title_re=APP_TITLE_RE, timeout=30)
        app_win = application.window(title_re=APP_TITLE_RE)
        page = LoginPage(app_win)

    with allure.step("Find and clsoe login form."):
        page.should_appear_login_window(timeout=2)
        close_login_window_button = page.should_be_close_login_window_button()
        close_login_window_button.click_input()

    yield app_win

    with allure.step("Close app."):
        close_btn = page.should_be_close_app_right_top_cross()
        close_btn.click_input()
        yes_button = page.should_appear_yes_button(timeout=2)
        yes_button.click_input()

