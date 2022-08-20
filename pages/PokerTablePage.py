from evenbet_app_test_pywinauto.utils import timer
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class PokerTablePage(BasePage):

    @timer("BuyIn form")
    def wait_for_buy_in_form(self, timeout=0):
        buy_in_form = locators.PokerTablePageLocators.buy_in_form(self.app, timeout=timeout)
        return buy_in_form
