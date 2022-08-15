import time
import allure
import pytest
import pywinauto
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
        login_window = page.wait_for_login_window(timeout=5)
        if not login_window:
            main_page_login_button = page.find_main_page_login_button()
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

    #with allure.step("Make window fullscreen."):
    #    fullscreen_btn = page.find_fullscreen_button()
    #    assert fullscreen_btn, "Right top fullscreen button is not detected."
    #    fullscreen_btn.click_input()

    yield app_win

    with allure.step("Close app."):
        application.kill()


@pytest.fixture(scope='module')
def test_app():
    application = pywinauto.Application(backend='uia').start(APP_PATH). \
        connect(class_name_re=MAIN_WINDOW_CLASS_NAME_RE, timeout=30)
    app_win = application.window(class_name_re=MAIN_WINDOW_CLASS_NAME_RE)

    yield app_win