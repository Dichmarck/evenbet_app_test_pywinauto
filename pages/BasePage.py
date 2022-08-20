import time
import _ctypes
import pywinauto
from evenbet_app_test_pywinauto.pages import locators
from evenbet_app_test_pywinauto.utils import timer



class BasePage:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def ensure_element_disappears(element, timeout=0):
        time_start = time.time()
        while time.time() - time_start <= timeout:
            try:
                element.rectangle()
            except (_ctypes.COMError, pywinauto.findwindows.ElementNotFoundError):
                return True
        return False

    @staticmethod
    def close_window_by_alt_f4(window):
        window.type_keys("%{F4}")

    @staticmethod
    def close_dialog_by_esc(dialog):
        dialog.type_keys("{VK_ESCAPE}")

    @timer("Right top close app cross")
    def find_close_app_right_top_cross(self):
        close_app_right_top_cross = locators.BasePageLocators.close_app_right_top_button(self.app)
        return close_app_right_top_cross

    @timer("Fullscreen button")
    def find_fullscreen_button(self):
        fullscreen_button = locators.BasePageLocators.fullscreen_button(self.app)
        return fullscreen_button

    @timer("YES button")
    def wait_for_yes_button(self, timeout=0):
        yes_button = locators.BasePageLocators.yes_button(self.app, timeout=timeout)
        return yes_button

    @timer("Login window")
    def wait_for_login_window(self, timeout=0):
        login_window = locators.BasePageLocators.login_window(self.app, timeout=timeout)
        return login_window

    @timer("Main page login button")
    def wait_for_main_page_login_button(self, timeout=0):
        login_button_main_page = locators.BasePageLocators.login_button_main_page(self.app, timeout=timeout)
        return login_button_main_page

    @timer("Show balance")
    def wait_for_show_user_balance_button(self, timeout=0):
        show_balance_button = locators.BasePageLocators.show_user_balance_button(self.app, timeout=timeout)
        return show_balance_button

    @timer("Cashier button")
    def find_cashier_button(self):
        cashier_button = locators.BasePageLocators.cashier_button(self.app)
        return cashier_button

    @timer("Cashier window")
    def wait_for_cashier_window(self, timeout=0):
        cashier_window = locators.WindowsLocators.cashier_window(timeout=timeout)
        return cashier_window

    @timer("Main lobby tabs")
    def find_main_lobby_tabs(self):
        main_lobby_tabs = locators.PokerPageLocators().main_lobby_tabs(self.app)
        return main_lobby_tabs

    @timer("Play button")
    def wait_for_play_button(self, timeout=0):
        play_button = locators.BasePageLocators.play_button(self.app, timeout=timeout)
        return play_button

    @timer("Right bottom buttons")
    def find_right_bottom_buttons(self):
        right_bottom_buttons = locators.BasePageLocators.right_bottom_buttons(self.app)
        return right_bottom_buttons

    @timer("Chat dialog")
    def wait_for_chat_dialog(self, timeout=0):
        chat_dialog = locators.BasePageLocators.chat_dialog(self.app, timeout=timeout)
        return chat_dialog

    @timer("My tables dialog")
    def wait_for_my_tables_dialog(self, timeout=0):
        my_tables_dialog = locators.BasePageLocators.my_tables_dialog(self.app, timeout=timeout)
        return my_tables_dialog

    @timer("My tournaments window")
    def wait_for_my_tournaments_window(self, timeout=0):
        my_tournaments_window = locators.WindowsLocators.my_tournaments_window(timeout=timeout)
        return my_tournaments_window

    @timer("Right top settings button")
    def find_right_top_settings_button(self):
        right_top_settings_button = locators.BasePageLocators.right_top_settings_button(self.app)
        return right_top_settings_button

    @timer("Right top settings tabs")
    def wait_for_right_top_settings_tabs(self, timeout=0):
        right_top_settings_tabs = locators.BasePageLocators.right_top_settings_tabs(self.app, timeout=timeout)
        return right_top_settings_tabs

    @timer("Sounds settings form")
    def wait_for_sounds_settings_form(self, timeout=0):
        sounds_settings_form = locators.BasePageLocators.sounds_settings_form(self.app, timeout=timeout)
        return sounds_settings_form

    @timer("Rates slider settings form")
    def wait_for_rates_slider_settings_form(self, timeout=0):
        rates_slider_settings_form = locators.BasePageLocators.rates_slider_settings_form(self.app, timeout=timeout)
        return rates_slider_settings_form

    @timer("Systen & chat settings form")
    def wait_for_system_chat_settings_form(self, timeout=0):
        system_chat_settings_form = locators.BasePageLocators.system_chat_settings_form(self.app, timeout=timeout)
        return system_chat_settings_form

    @timer("ByuIn & Rebuy settings form")
    def wait_for_buyin_rebuy_settings_form(self, timeout=0):
        buyin_rebuy_settings_form = locators.BasePageLocators.buyin_rebuy_settings_form(self.app, timeout=timeout)
        return buyin_rebuy_settings_form

    @timer("Table settings form")
    def wait_for_table_settings_form(self, timeout=0):
        table_settings_form = locators.BasePageLocators.table_settings_form(self.app, timeout=timeout)
        return table_settings_form

    @timer("Left menu button")
    def find_left_menu_button(self):
        left_menu_button = locators.BasePageLocators.left_menu_button(self.app)
        return left_menu_button

    @timer("Left menu tabs")
    def wait_for_left_menu_tabs(self, timeout=0):
        left_menu_tabs = locators.BasePageLocators.left_menu_tabs(self.app, timeout=timeout)
        return left_menu_tabs

    @timer("Account information form")
    def wait_for_account_information_form(self, timeout=0):
        account_information_form = locators.BasePageLocators.account_information_form(self.app, timeout=timeout)
        return account_information_form

    @timer("Account change password form")
    def wait_for_account_change_password_form(self, timeout=0):
        account_change_password_form = locators.BasePageLocators.account_change_password_form(self.app, timeout=timeout)
        return account_change_password_form

    @timer("Account change adress form")
    def wait_for_account_change_address_form(self, timeout=0):
        account_change_address_form = locators.BasePageLocators.account_change_address_form(self.app, timeout=timeout)
        return account_change_address_form

    @timer("Account verification form")
    def wait_for_account_verification_form(self, timeout=0):
        account_verification_form = locators.BasePageLocators.account_verification_form(self.app, timeout=timeout)
        return account_verification_form

    @timer("Account 2FA settings form")
    def wait_for_account_2fa_settings_form(self, timeout=0):
        account_2fa_settings_form = locators.BasePageLocators.account_2fa_settings_form(self.app, timeout=timeout)
        return account_2fa_settings_form

    @timer("Account change avatar form")
    def wait_for_account_change_avatar_form(self, timeout=0):
        account_change_avatar_form = locators.BasePageLocators.account_change_avatar_form(self.app, timeout=timeout)
        return account_change_avatar_form

    @timer("Account delete account form")
    def wait_for_account_delete_account_form(self, timeout=0):
        account_delete_account_form = locators.BasePageLocators.account_delete_account_form(self.app, timeout=timeout)
        return account_delete_account_form

    @timer("Tournament lobby window")
    def wait_for_tournament_lobby_window(self, timeout=0):
        tournament_lobby_window = locators.WindowsLocators.tournament_lobby_window(timeout=timeout)
        return tournament_lobby_window

    @timer("Logout dialog yes button")
    def wait_for_logout_dialog_yes_button(self, timeout=0):
        logout_dialog_yes_button = locators.BasePageLocators.logout_dialog_yes_button(self.app, timeout=timeout)
        return logout_dialog_yes_button

    @timer("Create table button on create table form")
    def wait_for_create_table_button_on_create_table_form(self, timeout=0):
        create_table_button = locators.BasePageLocators.create_table_button_on_create_table_form(self.app,
                                                                                                 timeout=timeout)
        return create_table_button

    @timer("Create tournament button on create tournament form")
    def wait_for_create_tournament_button_on_create_tournament_form(self, timeout=0):
        create_tournament_button = locators.BasePageLocators.\
            create_tournament_button_on_create_tournament_form(self.app, timeout=timeout)
        return create_tournament_button

    @timer("OK button on about form")
    def wait_for_ok_button_on_about_form(self, timeout=0):
        ok_button_on_about_form = locators.BasePageLocators.ok_button_on_about_form(self.app, timeout=timeout)
        return ok_button_on_about_form

    @timer("Languages form")
    def wait_for_languages_button(self, timeout=0):
        languages_button = locators.BasePageLocators.languages_button(self.app, timeout=timeout)
        return languages_button

    @timer("Languages list")
    def wait_for_languages_list(self, timeout=0):
        languages_list = locators.BasePageLocators.languages_list(self.app, timeout=timeout)
        return languages_list
    
