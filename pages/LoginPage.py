from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.locators import BasePageLocators, LoginPageLocators
from evenbet_app_test_pywinauto.constants import *


class LoginPage(BasePage):
    def should_be_close_login_window_button(self):
        close_login_window_button = BasePageLocators.close_login_window_button(self.app)
        assert close_login_window_button, "Close login window button is not detected"
        return close_login_window_button

    def should_be_login_username_field(self):
        username_field = LoginPageLocators.username_field(self.app)
        assert username_field, "No Username field on Login page"
        return username_field

    def should_be_login_password_field(self):
        password_field = LoginPageLocators.password_field(self.app)
        assert password_field, "No Password field on Login page"
        return password_field

    def should_be_login_button(self):
        login_button = LoginPageLocators.login_button(self.app)
        assert login_button, "No Password field on Login page"
        return login_button

    def print_username_in_login_username_field(self):
        username_field = self.should_be_login_username_field()
        username_field.click_input()
        username_field.type_keys(USERNAME)

    def print_username_in_login_username_field(self):
        username_field = self.should_be_login_username_field()
        username_field.click_input()
        username_field.type_keys(USERNAME)

    def print_password_in_login_username_field(self):
        password_field = self.should_be_login_password_field()
        password_field.click_input()
        password_field.type_keys(PASSWORD)


