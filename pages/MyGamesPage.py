from evenbet_app_test_pywinauto.pages.MainPage import MainPage
from evenbet_app_test_pywinauto.locators import MyGamesPageLocators
from evenbet_app_test_pywinauto.utils import timer


class MyGamesPage(MainPage):

    @timer("My games lobby tabs")
    def wait_for_my_games_lobby_tabs(self, timeout=0):
        return MyGamesPageLocators.my_games_lobby_tabs(self.app, timeout=timeout)

    @timer("My games results form")
    def wait_for_my_games_results_form(self, timeout=0):
        return MyGamesPageLocators.my_games_results_form(self.app, timeout=timeout)

    @timer("My games tournaments form")
    def wait_for_my_games_tournaments_form(self, timeout=0):
        return MyGamesPageLocators.my_games_tournaments_form(self.app, timeout=timeout)

    @timer("My games cash hans form")
    def wait_for_my_games_cash_hands_form(self, timeout=0):
        return MyGamesPageLocators.my_games_cash_hands_form(self.app, timeout=timeout)

    @timer("My games my statistics form")
    def wait_for_my_games_my_statistics_form(self, timeout=0):
        return MyGamesPageLocators.my_games_my_statistics_form(self.app, timeout=timeout)

    @timer("My games my casino form")
    def wait_for_my_games_my_casino_form(self, timeout=0):
        return MyGamesPageLocators.my_games_my_casino_form(self.app, timeout=timeout)
