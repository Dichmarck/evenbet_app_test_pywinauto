from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators
from evenbet_app_test_pywinauto.utils import timer


class MyGamesPage(BasePage):

    @timer("My games lobby tabs")
    def wait_for_my_games_lobby_tabs(self, timeout=0):
        my_games_lobby_tabs = locators.MyGamesPageLocators.my_games_lobby_tabs(self.app, timeout=timeout)
        return my_games_lobby_tabs

    @timer("My games results form")
    def wait_for_my_games_results_form(self, timeout=0):
        my_games_results_form = locators.MyGamesPageLocators.my_games_results_form(self.app, timeout=timeout)
        return my_games_results_form

    @timer("My games tournaments form")
    def wait_for_my_games_tournaments_form(self, timeout=0):
        my_games_tournaments_form = locators.MyGamesPageLocators.my_games_tournaments_form(self.app, timeout=timeout)
        return my_games_tournaments_form

    @timer("My games cash hans form")
    def wait_for_my_games_cash_hands_form(self, timeout=0):
        my_games_cash_hands_form = locators.MyGamesPageLocators.my_games_cash_hands_form(self.app, timeout=timeout)
        return my_games_cash_hands_form

    @timer("My games my statistics form")
    def wait_for_my_games_my_statistics_form(self, timeout=0):
        my_games_my_statistics_form = locators.MyGamesPageLocators.my_games_my_statistics_form(self.app,
                                                                                               timeout=timeout)
        return my_games_my_statistics_form

    @timer("My games my casino form")
    def wait_for_my_games_my_casino_form(self, timeout=0):
        my_games_my_casino_form = locators.MyGamesPageLocators.my_games_my_casino_form(self.app, timeout=timeout)
        return my_games_my_casino_form
