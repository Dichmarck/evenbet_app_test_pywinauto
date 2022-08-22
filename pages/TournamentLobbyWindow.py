from evenbet_app_test_pywinauto.utils import timer
from evenbet_app_test_pywinauto.pages.MainPage import MainPage
from evenbet_app_test_pywinauto.locators import TournamentLobbyWindowLocators


class TournamentLobbyPage(MainPage):

    @timer("Tournament lobby tabs")
    def find_tournament_lobby_tabs(self):
        return TournamentLobbyWindowLocators.tabs(app=self.app)

    @timer("Tournament lobby status pane")
    def wait_for_tournament_lobby_status_pane(self, timeout=0):
        return TournamentLobbyWindowLocators.status_pane(app=self.app, timeout=timeout)

    @timer("Tournament lobby prize pane")
    def wait_for_tournament_lobby_prize_pane(self, timeout=0):
        return TournamentLobbyWindowLocators.prize_pane(app=self.app, timeout=timeout)

    @timer("Tournament lobby satellites pane")
    def wait_for_tournament_lobby_satellites_pane(self, timeout=0):
        return TournamentLobbyWindowLocators.satellites_pane(app=self.app, timeout=timeout)

    @timer("Tournament lobby cashier button")
    def wait_for_tournament_lobby_cashier_button(self, timeout=0):
        return TournamentLobbyWindowLocators.cashier_button(app=self.app, timeout=timeout)

    @timer("Tournament lobby swipe view")
    def wait_for_swipe_view(self, timeout=0):
        return TournamentLobbyWindowLocators.swipe_view(app=self.app, timeout=timeout)
