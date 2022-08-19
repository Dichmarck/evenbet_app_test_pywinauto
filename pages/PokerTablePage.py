import time
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class PokerTablePage(BasePage):
    def wait_for_buy_in_form(self, timeout=0):
        time_start = time.time()
        buy_in_form = locators.PokerTablePageLocators.buy_in_form(self.app, timeout=timeout)
        print("Buy In form: ", time.time() - time_start)
        return buy_in_form
