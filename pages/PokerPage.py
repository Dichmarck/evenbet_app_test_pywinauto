from evenbet_app_test_pywinauto.utils import timer
from evenbet_app_test_pywinauto.pages.MainPage import MainPage
from evenbet_app_test_pywinauto.locators import PokerPageLocators


class PokerPage(MainPage):

    @timer("Poker lobby tabs")
    def wait_for_poker_lobby_tabs(self, timeout=0):
        return PokerPageLocators.poker_lobby_tabs(self.app, timeout=timeout)

    @timer("Poker lobby cash tables view")
    def wait_for_poker_lobby_cash_tables_view(self, timeout=0):
        return PokerPageLocators.poker_lobby_cash_tables_view(self.app, timeout=timeout)

    @timer("Poker lobby tournaments view")
    def wait_for_poker_lobby_tournaments_view(self, timeout=0):
        return PokerPageLocators.poker_lobby_tournaments_view(self.app, timeout=timeout)

    @timer("Poker lobby spins view")
    def wait_for_poker_lobby_spins_view(self, timeout=0):
        return PokerPageLocators.poker_lobby_spins_view(self.app, timeout=timeout)

    @timer("Tournament registration button")
    def wait_for_tournament_registration_button(self, timeout=0):
        return PokerPageLocators.tournament_registration_button(self.app, timeout=timeout)

    @timer("Tournament lobby button")
    def wait_for_tournament_lobby_button(self, timeout=0):
        return PokerPageLocators.tournament_lobby_button(self.app, timeout=timeout)

    @timer("Register button on tournament registration form")
    def wait_for_register_button_on_tournament_registration_form(self, timeout=0):
        return PokerPageLocators.register_button_on_tournament_registration_form(self.app, timeout=timeout)

    @timer("Tables in poker")
    def wait_for_tables_in_poker(self, timeout=0):
        return PokerPageLocators.poker_tables(self.app, timeout=timeout)
