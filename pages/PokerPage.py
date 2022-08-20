from evenbet_app_test_pywinauto.utils import timer
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class PokerPage(BasePage):

    @timer("Poker lobby tabs")
    def wait_for_poker_lobby_tabs(self, timeout=0):
        poker_lobby_tabs = locators.PokerPageLocators.poker_lobby_tabs(self.app, timeout=timeout)
        return poker_lobby_tabs

    @timer("Poker lobby cash tables view")
    def wait_for_poker_lobby_cash_tables_view(self, timeout=0):
        poker_lobby_cash_tables_view = locators.PokerPageLocators.poker_lobby_cash_tables_view(self.app,
                                                                                               timeout=timeout)
        return poker_lobby_cash_tables_view

    @timer("Poker lobby tournaments view")
    def wait_for_poker_lobby_tournaments_view(self, timeout=0):
        poker_lobby_tournaments_view = locators.PokerPageLocators.poker_lobby_tournaments_view(self.app,
                                                                                               timeout=timeout)
        return poker_lobby_tournaments_view

    @timer("Poker lobby spins view")
    def wait_for_poker_lobby_spins_view(self, timeout=0):
        poker_lobby_spins_view = locators.PokerPageLocators.poker_lobby_spins_view(self.app, timeout=timeout)
        return poker_lobby_spins_view

    @timer("Tournament registration button")
    def wait_for_tournament_registration_button(self, timeout=0):
        tournament_registration_button = locators.PokerPageLocators.tournament_registration_button(self.app,
                                                                                                   timeout=timeout)
        return tournament_registration_button

    @timer("Tournament lobby button")
    def wait_for_tournament_lobby_button(self, timeout=0):
        tournament_lobby_button = locators.PokerPageLocators.tournament_lobby_button(self.app, timeout=timeout)
        return tournament_lobby_button

    @timer("Register button on tournament registration form")
    def wait_for_register_button_on_tournament_registration_form(self, timeout=0):
        reg_from_reg_btn = locators.PokerPageLocators.register_button_on_tournament_registration_form(self.app,
                                                                                                      timeout=timeout)
        return reg_from_reg_btn

    @timer("Tables in poker")
    def wait_for_tables_in_poker(self, timeout=0):
        poker_tables = locators.PokerPageLocators.poker_tables(self.app, timeout=timeout)
        return poker_tables
