from ..utils import timer
from ..pages.MainPage import MainPage
from ..locators import TournamentLobbyWindowLocators


class TournamentLobbyPage(MainPage):

    @timer("Tournament lobby tabs")
    def find_tournament_lobby_tabs(self):
        return TournamentLobbyWindowLocators.tabs(self.app)

    @timer("Tournament lobby status pane")
    def wait_for_tournament_lobby_status_pane(self, timeout=0):
        return TournamentLobbyWindowLocators.status_pane(self.app, timeout=timeout)

    @timer("Tournament lobby prize pane")
    def wait_for_tournament_lobby_prize_pane(self, timeout=0):
        return TournamentLobbyWindowLocators.prize_pane(self.app, timeout=timeout)

    @timer("Tournament lobby satellites pane")
    def wait_for_tournament_lobby_satellites_pane(self, timeout=0):
        return TournamentLobbyWindowLocators.satellites_pane(self.app, timeout=timeout)

    @timer("Tournament lobby cashier button")
    def wait_for_tournament_lobby_cashier_button(self, timeout=0):
        return TournamentLobbyWindowLocators.cashier_button(self.app, timeout=timeout)

    @timer("Tournament lobby swipe view")
    def wait_for_swipe_view(self, timeout=0):
        return TournamentLobbyWindowLocators.swipe_view(self.app, timeout=timeout)
