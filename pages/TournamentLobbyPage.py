from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.locators import *
from evenbet_app_test_pywinauto import constants


class TournamentLobbyPage(BasePage):

    def find_tournament_lobby_tabs(self):
        time_start = time.time()
        tabs = TournamentsLobbyPageLocators.tabs(app=self.app)
        print("Tournament lobby window tabs: ", time.time() - time_start)
        return tabs

    def wait_for_tournament_lobby_status_pane(self, timeout=0):
        time_start = time.time()
        status_pane = TournamentsLobbyPageLocators.status_pane(app=self.app, timeout=timeout)
        print("Tournament status pane: ", time.time() - time_start)
        return status_pane

    def wait_for_tournament_lobby_prize_pane(self, timeout=0):
        time_start = time.time()
        prize_pane = TournamentsLobbyPageLocators.prize_pane(app=self.app, timeout=timeout)
        print("Tournament prize pane: ", time.time() - time_start)
        return prize_pane

    def wait_for_tournament_lobby_satellites_pane(self, timeout=0):
        time_start = time.time()
        satellites_pane = TournamentsLobbyPageLocators.satellites_pane(app=self.app, timeout=timeout)
        print("Tournament satellites pane: ", time.time() - time_start)
        return satellites_pane

    def wait_for_tournament_lobby_cashier_button(self, timeout=0):
        time_start = time.time()
        cashier_button = TournamentsLobbyPageLocators.cashier_button(app=self.app, timeout=timeout)
        print("Tournament Cashier button: ", time.time() - time_start)
        return cashier_button
