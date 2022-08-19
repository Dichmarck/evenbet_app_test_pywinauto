import time
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class TournamentLobbyPage(BasePage):

    def find_tournament_lobby_tabs(self):
        time_start = time.time()
        tabs = locators.TournamentsLobbyPageLocators.tabs(app=self.app)
        print("Tournament lobby window tabs: ", time.time() - time_start)
        return tabs

    def wait_for_tournament_lobby_status_pane(self, timeout=0):
        time_start = time.time()
        status_pane = locators.TournamentsLobbyPageLocators.status_pane(app=self.app, timeout=timeout)
        print("Tournament status pane: ", time.time() - time_start)
        return status_pane

    def wait_for_tournament_lobby_prize_pane(self, timeout=0):
        time_start = time.time()
        prize_pane = locators.TournamentsLobbyPageLocators.prize_pane(app=self.app, timeout=timeout)
        print("Tournament prize pane: ", time.time() - time_start)
        return prize_pane

    def wait_for_tournament_lobby_satellites_pane(self, timeout=0):
        time_start = time.time()
        satellites_pane = locators.TournamentsLobbyPageLocators.satellites_pane(app=self.app, timeout=timeout)
        print("Tournament satellites pane: ", time.time() - time_start)
        return satellites_pane

    def wait_for_tournament_lobby_cashier_button(self, timeout=0):
        time_start = time.time()
        cashier_button = locators.TournamentsLobbyPageLocators.cashier_button(app=self.app, timeout=timeout)
        print("Tournament Cashier button: ", time.time() - time_start)
        return cashier_button

    def wait_for_swipe_view(self, timeout=0):
        time_start = time.time()
        swipe_view = locators.TournamentsLobbyPageLocators.swipe_view(app=self.app, timeout=timeout)
        print("Tournament Lobby SwipeView: ", time.time() - time_start)
        return swipe_view
