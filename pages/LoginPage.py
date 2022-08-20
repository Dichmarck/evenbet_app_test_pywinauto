import time
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators
from evenbet_app_test_pywinauto.constants import PASSWORD, USERNAME
from evenbet_app_test_pywinauto.utils import timer


class LoginPage(BasePage):

    @timer("Close login window button")
    def find_close_login_window_button(self):
        close_login_window_button = locators.BasePageLocators.close_login_window_button(self.app)
        return close_login_window_button

    @timer("Login username field")
    def find_login_username_field(self):
        username_field = locators.LoginPageLocators.username_field(self.app)
        return username_field

    @timer("Login password field")
    def find_login_password_field(self):
        password_field = locators.LoginPageLocators.password_field(self.app)
        return password_field

    @timer("Login button")
    def find_login_button(self):
        login_button = locators.LoginPageLocators.login_button(self.app)
        return login_button

    @timer("SignUp button")
    def find_signup_button(self):
        signup_button = locators.LoginPageLocators.signup_button(self.app)
        return signup_button

    @timer("Print username")
    def print_username_in_login_username_field(self, username_field):
        username_field.click_input()
        username_field.type_keys(USERNAME)

    @timer("Print password")
    def print_password_in_login_username_field(self, password_field):
        password_field.click_input()
        password_field.type_keys(PASSWORD)


