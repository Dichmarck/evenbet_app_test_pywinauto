import time

from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.locators import BasePageLocators, LoginPageLocators
from evenbet_app_test_pywinauto.constants import *


class LoginPage(BasePage):
    def find_close_login_window_button(self):
        time_start = time.time()
        close_login_window_button = BasePageLocators.close_login_window_button(self.app)
        print("Close login form button: ", time.time() - time_start)
        return close_login_window_button

    def find_login_username_field(self):
        time_start = time.time()
        username_field = LoginPageLocators.username_field(self.app)
        print("Login field: ", time.time() - time_start)
        return username_field

    def find_login_password_field(self):
        time_start = time.time()
        password_field = LoginPageLocators.password_field(self.app)
        print("Password field: ", time.time() - time_start)
        return password_field

    def find_login_button(self):
        time_start = time.time()
        login_button = LoginPageLocators.login_button(self.app)
        print("Login button: ", time.time() - time_start)
        return login_button

    def find_signup_button(self):
        signup_button = LoginPageLocators.signup_button(self.app)
        return signup_button

    def print_username_in_login_username_field(self, username_field):
        username_field.click_input()
        username_field.type_keys(USERNAME)

    def print_password_in_login_username_field(self, password_field):
        password_field.click_input()
        password_field.type_keys(PASSWORD)


