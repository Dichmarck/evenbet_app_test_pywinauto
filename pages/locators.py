import pywinauto
import time
import pytest


def find_element_or_none(element, timeout=0):
    time_now = time.time()
    time_start = time.time()
    while time_now - time_start <= timeout:
        try:
            return element.wrapper_object()
        except pywinauto.findbestmatch.MatchError:
            pass
        time_now = time.time()
    return None


class BasePageLocators:

    @staticmethod
    def close_app_right_top_button(app, timeout=0):
        return find_element_or_none(app.TitleBar.Button3, timeout=timeout)

    @staticmethod
    def yes_button(app, timeout=0):
        return find_element_or_none(app.Yes, timeout=timeout)

    @staticmethod
    def login_window(app, timeout=0):
        return find_element_or_none(app.Login.Dialog.TabItem, timeout=timeout)

    @staticmethod
    def close_login_window_button(app, timeout=0):
        return find_element_or_none(app.Login.Dialog.TabItem.ToolBar.Button, timeout=timeout)

    @staticmethod
    def login_button_main_page(app, timeout=0):
        return find_element_or_none(app.child_window(title="Login", control_type="Button"), timeout=timeout)

    @staticmethod
    def show_balance_button(app, timeout=0):
        return find_element_or_none(app.ShowBalance, timeout=timeout)

    @staticmethod
    def cashier_button(app, timeout=0):
        return find_element_or_none(app.Cashier, timeout=timeout)


class LoginPageLocators(BasePageLocators):
    @staticmethod
    def username_field(app, timeout=0):
        return find_element_or_none(app.Login.Dialog.TabItem.Edit1, timeout=timeout)

    @staticmethod
    def password_field(app, timeout=0):
        return find_element_or_none(app.Login.Dialog.TabItem.Edit2, timeout=timeout)

    @staticmethod
    def login_button(app, timeout=0):
        return find_element_or_none(app.Login.Dialog.TabItem.Button1, timeout=timeout)

