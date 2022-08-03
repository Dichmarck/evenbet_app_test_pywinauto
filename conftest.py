import time
import pytest
import pywinauto
from .constants import *
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.LoginPage import LoginPage
from .pages.locators import *


@pytest.fixture(scope='class')
def app():
    application = pywinauto.Application(backend='uia').start(APP_PATH).connect(title_re=APP_TITLE_RE, timeout=30)
    app_win = application.window(title_re=APP_TITLE_RE)
    page = LoginPage(app_win)

    page.should_appear_login_window(timeout=3)
    close_login_window_button = page.should_be_close_login_window_button()
    close_login_window_button.click_input()

    yield app_win

    close_btn = page.should_be_close_app_right_top_cross()
    close_btn.click_input()

    yes_button = page.should_appear_yes_button(timeout=2)
    yes_button.click_input()

