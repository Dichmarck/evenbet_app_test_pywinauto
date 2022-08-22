from evenbet_app_test_pywinauto.utils import timer
from evenbet_app_test_pywinauto.pages.MainPage import MainPage
from evenbet_app_test_pywinauto.locators import PokerTableWindowLocators


class PokerTableWindow(MainPage):

    @timer("BuyIn form")
    def wait_for_buy_in_form(self, timeout=0):
        return PokerTableWindowLocators.buy_in_form(self.app, timeout=timeout)
