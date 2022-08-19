import time
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class MyGamesPage(BasePage):
    def wait_for_my_games_lobby_tabs(self, timeout=0):
        time_start = time.time()
        my_games_lobby_tabs = locators.MyGamesPageLocators.my_games_lobby_tabs(self.app, timeout=timeout)
        print("My Games lobby tabs: ", time.time() - time_start)
        return my_games_lobby_tabs

    def wait_for_my_games_results_form(self, timeout=0):
        time_start = time.time()
        my_games_results_form = locators.MyGamesPageLocators.my_games_results_form(self.app, timeout=timeout)
        print("My Games results form: ", time.time() - time_start)
        return my_games_results_form

    def wait_for_my_games_tournaments_form(self, timeout=0):
        time_start = time.time()
        my_games_tournaments_form = locators.MyGamesPageLocators.my_games_tournaments_form(self.app, timeout=timeout)
        print("My Games tournaments form: ", time.time() - time_start)
        return my_games_tournaments_form

    def wait_for_my_games_cash_hands_form(self, timeout=0):
        time_start = time.time()
        my_games_cash_hands_form = locators.MyGamesPageLocators.my_games_cash_hands_form(self.app, timeout=timeout)
        print("My Games cash hands form: ", time.time() - time_start)
        return my_games_cash_hands_form

    def wait_for_my_games_my_statistics_form(self, timeout=0):
        time_start = time.time()
        my_games_my_statistics_form = locators.MyGamesPageLocators.my_games_my_statistics_form(self.app,
                                                                                               timeout=timeout)
        print("My Games my statistics form: ", time.time() - time_start)
        return my_games_my_statistics_form

    def wait_for_my_games_my_casino_form(self, timeout=0):
        time_start = time.time()
        my_games_my_casino_form = locators.MyGamesPageLocators.my_games_my_casino_form(self.app, timeout=timeout)
        print("My Games my casino form: ", time.time() - time_start)
        return my_games_my_casino_form
