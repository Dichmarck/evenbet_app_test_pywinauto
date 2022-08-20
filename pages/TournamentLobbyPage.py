from evenbet_app_test_pywinauto.utils import timer
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class TournamentLobbyPage(BasePage):

    @timer("Tournament lobby tabs")
    def find_tournament_lobby_tabs(self):
        tabs = locators.TournamentsLobbyPageLocators.tabs(app=self.app)
        return tabs

    @timer("Tournament lobby status pane")
    def wait_for_tournament_lobby_status_pane(self, timeout=0):
        status_pane = locators.TournamentsLobbyPageLocators.status_pane(app=self.app, timeout=timeout)
        return status_pane

    @timer("Tournament lobby prize pane")
    def wait_for_tournament_lobby_prize_pane(self, timeout=0):
        prize_pane = locators.TournamentsLobbyPageLocators.prize_pane(app=self.app, timeout=timeout)
        return prize_pane

    @timer("Tournament lobby satellites pane")
    def wait_for_tournament_lobby_satellites_pane(self, timeout=0):
        satellites_pane = locators.TournamentsLobbyPageLocators.satellites_pane(app=self.app, timeout=timeout)
        return satellites_pane

    @timer("Tournament lobby cashier button")
    def wait_for_tournament_lobby_cashier_button(self, timeout=0):
        cashier_button = locators.TournamentsLobbyPageLocators.cashier_button(app=self.app, timeout=timeout)
        return cashier_button

    @timer("Tournament lobby swipe view")
    def wait_for_swipe_view(self, timeout=0):
        swipe_view = locators.TournamentsLobbyPageLocators.swipe_view(app=self.app, timeout=timeout)
        return swipe_view
