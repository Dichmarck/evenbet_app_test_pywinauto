from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.locators import *
from evenbet_app_test_pywinauto import constants


class PokerPage(BasePage):
    def wait_for_poker_lobby_tabs(self, timeout=0):
        time_start = time.time()
        poker_lobby_tabs = PokerPageLocators.poker_lobby_tabs(self.app, timeout=timeout)
        print("Poker lobby tabs: ", time.time() - time_start)
        return poker_lobby_tabs

    def wait_for_poker_lobby_cash_tables_view(self, timeout=0):
        time_start = time.time()
        poker_lobby_cash_tables_view = PokerPageLocators.poker_lobby_cash_tables_view(self.app, timeout=timeout)
        print("Poker lobby cash tables view: ", time.time() - time_start)
        return poker_lobby_cash_tables_view

    def wait_for_poker_lobby_tournaments_view(self, timeout=0):
        time_start = time.time()
        poker_lobby_tournaments_view = PokerPageLocators.poker_lobby_tournaments_view(self.app, timeout=timeout)
        print("Poker lobby tournaments view: ", time.time() - time_start)
        return poker_lobby_tournaments_view

    def wait_for_poker_lobby_spins_view(self, timeout=0):
        time_start = time.time()
        poker_lobby_spins_view = PokerPageLocators.poker_lobby_spins_view(self.app, timeout=timeout)
        print("Poker lobby spins view: ", time.time() - time_start)
        return poker_lobby_spins_view

    def wait_for_tournament_registration_button(self, timeout=0):
        time_start = time.time()
        tournament_registration_button = PokerPageLocators.tournament_registration_button(self.app, timeout=timeout)
        print("Tournament registration button: ", time.time() - time_start)
        return tournament_registration_button

    def wait_for_tournament_lobby_button(self, timeout=0):
        time_start = time.time()
        tournament_lobby_button = PokerPageLocators.tournament_lobby_button(self.app, timeout=timeout)
        print("Tournament lobby button: ", time.time() - time_start)
        return tournament_lobby_button

    def wait_for_register_button_on_tournament_registration_form(self, timeout=0):
        time_start = time.time()
        reg_from_reg_btn = PokerPageLocators.register_button_on_tournament_registration_form(self.app, timeout=timeout)
        print("Register button on registration form: ", time.time() - time_start)
        return reg_from_reg_btn

