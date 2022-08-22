from ..utils import timer
from ..pages.MainPage import MainPage
from ..locators import PokerTableWindowLocators


class PokerTableWindow(MainPage):

    @timer("BuyIn form")
    def wait_for_buy_in_form(self, timeout=0):
        return PokerTableWindowLocators.buy_in_form(self.app, timeout=timeout)
