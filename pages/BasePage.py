import time
import pywinauto
from .locators import *



class BasePage:
    def __init__(self, app):
        self.app = app

    def should_be_close_app_right_top_cross(self):
        close_app_right_top_cross = BasePageLocators.close_app_right_top_button(self.app)
        assert close_app_right_top_cross, "Right top close-app-cross is not detected."
        return close_app_right_top_cross

    def should_appear_yes_button(self, timeout=0):
        yes_button = BasePageLocators.yes_button(self.app, timeout=timeout)
        assert yes_button, "Yes-button is not detected."
        return yes_button

    def should_appear_login_window(self, timeout=0):
        login_window = BasePageLocators.login_window(self.app, timeout=timeout)
        assert login_window, "Login Window didn't appear."
        return login_window

    def should_be_main_page_login_button(self):
        login_button_main_page = BasePageLocators.login_button_main_page(self.app)
        assert login_button_main_page, "Login button is not detected on Main page."
        return login_button_main_page

    def should_appear_show_balance_button(self, timeout=0):
        show_balance_button = BasePageLocators.show_balance_button(self.app, timeout=timeout)
        assert show_balance_button, "Show Balance button didn't appear on Main page after login."
        return show_balance_button

    def should_appear_cashier_button(self, timeout=0):
        cashier_button = BasePageLocators.cashier_button(self.app, timeout=timeout)
        assert cashier_button, "Cashier button didn't appear on Main page after login."
        return cashier_button

