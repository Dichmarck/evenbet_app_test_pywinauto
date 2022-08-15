import time

import _ctypes
import pywinauto
from .locators import *


class BasePage:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def ensure_element_disappears(element, timeout=0):
        time_start = time.time()
        while time.time() - time_start <= timeout:
            try:
                element.rectangle()
            except (_ctypes.COMError, pywinauto.findwindows.ElementNotFoundError) as e:
                return True
        return False

    @staticmethod
    def close_window_by_alt_f4(window):
        window.type_keys("%{F4}")

    @staticmethod
    def close_dialog_by_esc(dialog):
        dialog.type_keys("{VK_ESCAPE}")

    def find_close_app_right_top_cross(self):
        time_start = time.time()
        close_app_right_top_cross = BasePageLocators.close_app_right_top_button(self.app)
        print("Close app button: ", time.time() - time_start)
        return close_app_right_top_cross

    def find_fullscreen_button(self):
        time_start = time.time()
        fullscreen_button = BasePageLocators.fullscreen_button(self.app)
        print("Fullscreen button: ", time.time() - time_start)
        return fullscreen_button

    def wait_for_yes_button(self, timeout=0):
        time_start = time.time()
        yes_button = BasePageLocators.yes_button(self.app, timeout=timeout)
        print("Yes button: ", time.time() - time_start)
        return yes_button

    def wait_for_login_window(self, timeout=0):
        time_start = time.time()
        login_window = BasePageLocators.login_window(self.app, timeout=timeout)
        print("Login window: ", time.time() - time_start)
        return login_window

    def find_main_page_login_button(self):
        time_start = time.time()
        login_button_main_page = BasePageLocators.login_button_main_page(self.app)
        print("Main page login button: ", time.time() - time_start)
        return login_button_main_page

    def wait_for_show_user_balance_button(self, timeout=0):
        time_start = time.time()
        show_balance_button = BasePageLocators.show_user_balance_button(self.app, timeout=timeout)
        print("Show Balance button: ", time.time() - time_start)
        return show_balance_button

    def find_cashier_button(self):
        time_start = time.time()
        cashier_button = BasePageLocators.cashier_button(self.app)
        print("Cashier button: ", time.time() - time_start)
        return cashier_button

    def wait_for_cashier_window(self, timeout=0):
        time_start = time.time()
        cashier_window = WindowsLocators.cashier_window(timeout=timeout)
        print("Cashier window: ", time.time() - time_start)
        return cashier_window

    def find_main_lobby_tabs(self):
        time_start = time.time()
        main_lobby_tabs = PokerPageLocators().main_lobby_tabs(self.app)
        print("Main lobby tabs: ", time.time() - time_start)
        return main_lobby_tabs

    def find_play_button(self, timeout=0):
        time_start = time.time()
        play_button = BasePageLocators.play_button(self.app, timeout=timeout)
        print("Play button: ", time.time() - time_start)
        return play_button

    def find_right_bottom_buttons(self):
        time_start = time.time()
        right_bottom_buttons = BasePageLocators.right_bottom_buttons(self.app)
        print("Right bottom buttons: ", time.time() - time_start)
        return right_bottom_buttons

    def wait_for_chat_dialog(self, timeout=0):
        time_start = time.time()
        chat_dialog = BasePageLocators.chat_dialog(self.app)
        print("Chat dialog: ", time.time() - time_start)
        return chat_dialog

    def wait_for_my_tables_dialog(self, timeout=0):
        time_start = time.time()
        my_tables_dialog = BasePageLocators.my_tables_dialog(self.app)
        print("My Tables dialog: ", time.time() - time_start)
        return my_tables_dialog

    def wait_for_my_tournaments_window(self, timeout=0):
        time_start = time.time()
        my_tournaments_window = WindowsLocators.my_tournaments_window(timeout=timeout)
        print("My Tournaments window: ", time.time() - time_start)
        return my_tournaments_window


