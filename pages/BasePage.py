import time

import _ctypes
import allure
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

    def wait_for_main_page_login_button(self, timeout=0):
        time_start = time.time()
        login_button_main_page = BasePageLocators.login_button_main_page(self.app, timeout=timeout)
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

    def find_right_top_settings_button(self):
        time_start = time.time()
        right_top_settings_button = BasePageLocators.right_top_settings_button(self.app)
        print("Right top settings button: ", time.time() - time_start)
        return right_top_settings_button

    def wait_for_right_top_settings_tabs(self, timeout=0):
        time_start = time.time()
        right_top_settings_tabs = BasePageLocators.right_top_settings_tabs(self.app)
        print("Right top settings tabs: ", time.time() - time_start)
        return right_top_settings_tabs

    def wait_for_sounds_settings_form(self, timeout=0):
        time_start = time.time()
        sounds_settings_form = BasePageLocators.sounds_settings_form(self.app, timeout=timeout)
        print("Sounds settings form: ", time.time() - time_start)
        return sounds_settings_form

    def wait_for_rates_slider_settings_form(self, timeout=0):
        time_start = time.time()
        rates_slider_settings_form = BasePageLocators.rates_slider_settings_form(self.app, timeout=timeout)
        print("Rates slider settings form: ", time.time() - time_start)
        return rates_slider_settings_form

    def wait_for_system_chat_settings_form(self, timeout=0):
        time_start = time.time()
        system_chat_settings_form = BasePageLocators.system_chat_settings_form(self.app, timeout=timeout)
        print("System & Chat settings form: ", time.time() - time_start)
        return system_chat_settings_form

    def wait_for_buyin_rebuy_settings_form(self, timeout=0):
        time_start = time.time()
        buyin_rebuy_settings_form = BasePageLocators.buyin_rebuy_settings_form(self.app, timeout=timeout)
        print("BuyIn & Rebuy settings form: ", time.time() - time_start)
        return buyin_rebuy_settings_form

    def wait_for_table_settings_form(self, timeout=0):
        time_start = time.time()
        table_settings_form = BasePageLocators.table_settings_form(self.app, timeout=timeout)
        print("Table settings form: ", time.time() - time_start)
        return table_settings_form

    def find_left_menu_button(self):
        time_start = time.time()
        left_menu_button = BasePageLocators.left_menu_button(self.app)
        print("Left Menu button: ", time.time() - time_start)
        return left_menu_button

    def wait_for_left_menu_tabs(self, timeout=0):
        time_start = time.time()
        left_menu_tabs = BasePageLocators.left_menu_tabs(self.app, timeout=timeout)
        print("Left Menu tabs: ", time.time() - time_start)
        return left_menu_tabs

    def wait_for_account_information_form(self, timeout=0):
        time_start = time.time()
        account_information_form = BasePageLocators.account_information_form(self.app, timeout=timeout)
        print("Account information form: ", time.time() - time_start)
        return account_information_form

    def wait_for_account_change_password_form(self, timeout=0):
        time_start = time.time()
        account_change_password_form = BasePageLocators.account_change_password_form(self.app, timeout=timeout)
        print("Change password form: ", time.time() - time_start)
        return account_change_password_form

    def wait_for_account_change_address_form(self, timeout=0):
        time_start = time.time()
        account_change_address_form = BasePageLocators.account_change_address_form(self.app, timeout=timeout)
        print("Change address form: ", time.time() - time_start)
        return account_change_address_form

    def wait_for_account_verification_form(self, timeout=0):
        time_start = time.time()
        account_verification_form = BasePageLocators.account_verification_form(self.app, timeout=timeout)
        print("Verification form: ", time.time() - time_start)
        return account_verification_form

    def wait_for_account_2fa_settings_form(self, timeout=0):
        time_start = time.time()
        account_2fa_settings_form = BasePageLocators.account_2fa_settings_form(self.app, timeout=timeout)
        print("2FA settings form: ", time.time() - time_start)
        return account_2fa_settings_form

    def wait_for_account_change_avatar_form(self, timeout=0):
        time_start = time.time()
        account_change_avatar_form = BasePageLocators.account_change_avatar_form(self.app, timeout=timeout)
        print("Change avatar form: ", time.time() - time_start)
        return account_change_avatar_form

    def wait_for_account_delete_account_form(self, timeout=0):
        time_start = time.time()
        account_delete_account_form = BasePageLocators.account_delete_account_form(self.app, timeout=timeout)
        print("Delete account form: ", time.time() - time_start)
        return account_delete_account_form

    def wait_for_tournament_lobby_window(self, timeout=0):
        time_start = time.time()
        tournament_lobby_window = WindowsLocators.tournament_lobby_window(timeout=timeout)
        print("Tournament lobby windows: ", time.time() - time_start)
        return tournament_lobby_window

    def wait_for_logout_dialog_yes_button(self, timeout=0):
        time_start = time.time()
        logout_dialog_yes_button = BasePageLocators.logout_dialog_yes_button(self.app, timeout=timeout)
        print("Logout dialog YES button: ", time.time() - time_start)
        return logout_dialog_yes_button






