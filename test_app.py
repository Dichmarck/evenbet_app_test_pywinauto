import time

import allure
import pyautogui
import pytest
import pywinauto
from evenbet_app_test_pywinauto.conftest import return_func_name
from evenbet_app_test_pywinauto.pages.ChatDialogPage import ChatDialogPage
from evenbet_app_test_pywinauto.pages.locators import WindowsLocators
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.LoginPage import LoginPage
from evenbet_app_test_pywinauto.pages.MyGamesPage import MyGamesPage
from evenbet_app_test_pywinauto.pages.PokerPage import PokerPage
from evenbet_app_test_pywinauto.pages.PokerTablePage import PokerTablePage
from evenbet_app_test_pywinauto.pages.RegistraionPage import SignUpPage


# pytest -s -v  --tb=short --alluredir=reports/allure
# allure serve reports/allure


class TestBasePageButtons:

    def test_cashier_window_appears_after_click_cashier_button(self, app, screenshot_report):
        """In this test we try to click 'Cashier' button, ensure that 'Cashier' window opens and close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find Cashier button."):
            cashier_button = page.find_cashier_button()
            assert cashier_button, "Cashier button not found on main page."

        with allure.step("Click Cashier button and wait for Cashier window."):
            cashier_button.click_input()
            cashier_window = page.wait_for_cashier_window(timeout=3)
            assert cashier_window, "Cashier window didn't appear after clicking Cashier button."

        with allure.step("Close Cashier window."):
            BasePage.close_window_by_alt_f4(cashier_window)
            window_closed = BasePage.ensure_element_disappears(cashier_window, timeout=3)
            assert window_closed, "Cashier window didn't close."
        screenshot_report['status'] = 'Passed'

    def test_poker_table_appears_after_click_play_button(self, app, screenshot_report):
        """In this test we try to click 'Play' button, ensure that 'Poker Table' window opens and close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find and click Play button."):
            play_button = page.find_play_button()
            assert play_button, "Play button not found on main page."
            play_button.click_input()

        with allure.step("Find Poker Table window and connect to it."):
            poker_table_window = WindowsLocators.poker_table_window(timeout=5)
            assert poker_table_window, "Poker window didn't appear after click Play button."
            poker_page = PokerTablePage(app=poker_table_window)

        with allure.step("Find and close BuyIn form."):
            buy_in_form = poker_page.wait_for_buy_in_form(timeout=3)
            if buy_in_form:
                PokerPage.close_dialog_by_esc(buy_in_form)
            buy_in_form_closed = PokerPage.ensure_element_disappears(buy_in_form, timeout=2)
            assert buy_in_form_closed, "Buy In form didn't close."

        with allure.step("Close Poker Table window."):
            PokerTablePage.close_window_by_alt_f4(poker_table_window)
            poker_table_window_closed = PokerTablePage.ensure_element_disappears(poker_table_window, timeout=3)
            assert poker_table_window_closed, "Poker Table window didn't close."
        screenshot_report['status'] = 'Passed'

@pytest.mark.go
class TestRightTopSettings:

    def test_settings_sounds(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'Sounds' settings tab,
                check that 'Sounds settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right top settings button."):
            page = BasePage(app=app)
            right_top_settings_button = page.find_right_top_settings_button()
            assert right_top_settings_button, "Right top settings button not found on main page."
        with allure.step("Click settings button and wait for tabs in settings menu."):
            right_top_settings_button.click_input()
            settings_tabs = page.wait_for_right_top_settings_tabs(timeout=3)
            assert settings_tabs, "Settings menu didn't appear after click right top settings button."
        with allure.step("Click 'Sounds settings' tab and wait for 'Sounds Settings' form."):
            settings_tabs[0].click_input()
            sounds_settings_form = page.wait_for_sounds_settings_form(timeout=2)
            assert sounds_settings_form, "Sounds settings form didin't appear " \
                                         "after click 'Sounds' tab in right top settings menu."
        with allure.step("Close 'Sounds' settings form."):
            page.close_dialog_by_esc(sounds_settings_form)
            sounds_settings_form_closed = page.ensure_element_disappears(sounds_settings_form)
            assert sounds_settings_form_closed, "'Sounds settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_rates_slider(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'Rates Slider' settings tab,
                check that 'Rates slider settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right top settings button."):
            page = BasePage(app=app)
            right_top_settings_button = page.find_right_top_settings_button()
            assert right_top_settings_button, "Right top settings button not found on main page."
        with allure.step("Click settings button and wait for tabs in settings menu."):
            right_top_settings_button.click_input()
            settings_tabs = page.wait_for_right_top_settings_tabs(timeout=3)
            assert settings_tabs, "Settings menu didn't appear after click right top settings button."
        with allure.step("Click 'Rates Slider settings' tab and wait for 'Sounds Settings' form."):
            settings_tabs[1].click_input()
            rates_slider_settings_form = page.wait_for_rates_slider_settings_form(timeout=2)
            assert rates_slider_settings_form, "Rates slider settings form didin't appear " \
                                         "after click 'Rates Slider' tab in right top settings menu."
        with allure.step("Close 'Rates Slider settings' form."):
            page.close_dialog_by_esc(rates_slider_settings_form)
            rates_slider_settings_form_closed = page.ensure_element_disappears(rates_slider_settings_form)
            assert rates_slider_settings_form_closed, "'Rates slider settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_system_chat(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'System & chat' settings tab,
                check that 'System & Chat settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right top settings button."):
            page = BasePage(app=app)
            right_top_settings_button = page.find_right_top_settings_button()
            assert right_top_settings_button, "Right top settings button not found on main page."
        with allure.step("Click settings button and wait for tabs in settings menu."):
            right_top_settings_button.click_input()
            settings_tabs = page.wait_for_right_top_settings_tabs(timeout=3)
            assert settings_tabs, "Settings menu didn't appear after click right top settings button."
        with allure.step("Click 'System & Chat settings' tab and wait for 'System & Chat' form."):
            settings_tabs[2].click_input()
            system_chat_settings_form = page.wait_for_system_chat_settings_form(timeout=2)
            assert system_chat_settings_form, "System & chat settings form didin't appear " \
                                               "after click 'System & Chat' tab in right top settings menu."
        with allure.step("Close 'System & Chat settings' form."):
            page.close_dialog_by_esc(system_chat_settings_form)
            system_chat_settings_form_closed = page.ensure_element_disappears(system_chat_settings_form)
            assert system_chat_settings_form_closed, "'System & Chat settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_buyin_rebuy(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'BuyIn & rebuy' settings tab,
                check that 'BuyIn & Rebuy settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right top settings button."):
            page = BasePage(app=app)
            right_top_settings_button = page.find_right_top_settings_button()
            assert right_top_settings_button, "Right top settings button not found on main page."
        with allure.step("Click settings button and wait for tabs in settings menu."):
            right_top_settings_button.click_input()
            settings_tabs = page.wait_for_right_top_settings_tabs(timeout=3)
            assert settings_tabs, "Settings menu didn't appear after click right top settings button."
        with allure.step("Click 'BuyIn & Rebuy settings' tab and wait for 'BuyIn & rebuy' form."):
            settings_tabs[3].click_input()
            buyin_rebuy_settings_form = page.wait_for_buyin_rebuy_settings_form(timeout=2)
            assert buyin_rebuy_settings_form, "BuyIn & Rebuy settings form didin't appear " \
                                              "after click 'BuyIn & rebuy' tab in right top settings menu."
        with allure.step("Close 'BuyIn & Rebuy settings' form."):
            page.close_dialog_by_esc(buyin_rebuy_settings_form)
            buyin_rebuy_settings_form_closed = page.ensure_element_disappears(buyin_rebuy_settings_form)
            assert buyin_rebuy_settings_form_closed, "'BuyIn & rebuy settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_table(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'Table settings' tab,
                        check that 'Table settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right top settings button."):
            page = BasePage(app=app)
            right_top_settings_button = page.find_right_top_settings_button()
            assert right_top_settings_button, "Right top settings button not found on main page."
        with allure.step("Click settings button and wait for tabs in settings menu."):
            right_top_settings_button.click_input()
            settings_tabs = page.wait_for_right_top_settings_tabs(timeout=3)
            assert settings_tabs, "Settings menu didn't appear after click right top settings button."
        with allure.step("Click 'Table settings' settings tab and wait for 'Table settings' form."):
            settings_tabs[4].click_input()
            table_settings_form = page.wait_for_table_settings_form(timeout=2)
            assert table_settings_form, "Table settings form didin't appear " \
                                              "after click 'Table settings' tab in right top settings menu."
        with allure.step("Close 'Table settings' form."):
            page.close_dialog_by_esc(table_settings_form)
            table_settings_form_closed = page.ensure_element_disappears(table_settings_form)
            assert table_settings_form_closed, "'Table settings' form didn't close."
        screenshot_report['status'] = 'passed'


class TestRightBottomButtons:

    def test_chat_button(self, app, screenshot_report):
        """In this test we try to open Chat dialog, send new message and close it."""

        with allure.step("Initializing BasePage."):
            page = ChatDialogPage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right bottom buttons."):
            right_bottom_buttons = page.find_right_bottom_buttons()
            assert right_bottom_buttons, "Right bottom buttons not found on main page."
        with allure.step("Click 'Chat' and check that chat-dialog appeared."):
            right_bottom_buttons[0].click_input()
            chat_dialog = page.wait_for_chat_dialog(timeout=3)
            assert chat_dialog, "Chat dialog didn't appear after click right bottom 'Chat' button."
        with allure.step("Generate new message and check that ensure that it is not contained in chat already."):
            new_message = str(int(time.time()))
            chat_messages_str_list = page.find_chat_messages_str_list()
            assert new_message not in chat_messages_str_list, f"Message {new_message} is already in chat messages."
        with allure.step("Find text field for new message"):
            chat_text_field = page.find_chat_text_field()
            assert chat_text_field, "Chat message field not found in chat dialog."
        with allure.step("Send message in chat and ensure that it was displayed."):
            page.send_message_in_chat(text_field=chat_text_field, message=new_message)
            chat_messages_str_list = page.find_chat_messages_str_list()
            assert new_message in chat_messages_str_list, "New message wasn't displayed in chat."
        with allure.step("Close chat dialog."):
            page.close_dialog_by_esc(chat_dialog)
            chat_closed = page.ensure_element_disappears(chat_dialog, timeout=3)
            assert chat_closed, "Chat didn't close."
        screenshot_report['status'] = 'Passed'

    def test_my_tables(self, app, screenshot_report):
        """In this test we try to open 'My Tables' dialog and close it."""

        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right bottom buttons."):
            right_bottom_buttons = page.find_right_bottom_buttons()
            assert right_bottom_buttons, "Right bottom buttons not found on main page."
        with allure.step("Click 'My Tables' and check that 'My Tables' dialog appeared."):
            right_bottom_buttons[1].click_input()
            my_tables_dialog = page.wait_for_my_tables_dialog(timeout=3)
            assert my_tables_dialog, "'My Tables' dialog didn't appear after click right bottom 'My Tables' button."
        with allure.step("Close 'My Tables' dialog."):
            page.close_dialog_by_esc(my_tables_dialog)
            my_tables_dialog_closed = page.ensure_element_disappears(my_tables_dialog, timeout=3)
            assert my_tables_dialog_closed, "'My Tables' dialog didn't close."
        screenshot_report['status'] = 'Passed'

    def test_my_tournaments(self, app, screenshot_report):
        """In this test we try to open 'My Tournaments' window and close it."""

        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find right bottom buttons."):
            right_bottom_buttons = page.find_right_bottom_buttons()
            assert right_bottom_buttons, "Right bottom buttons not found on main page."
        with allure.step("Click 'My Tournaments' button and check that 'My Tournaments' window appeared."):
            right_bottom_buttons[2].click_input()
            my_tournaments_window = page.wait_for_my_tournaments_window(timeout=5)
            assert my_tournaments_window, "'My Tournaments' window didn't appear after click right bottom" \
                                          "'My Tournaments' button."
            my_tournaments_window.click_input()
        with allure.step("Close 'My Tournaments' window."):
            BasePage.close_window_by_alt_f4(my_tournaments_window)
            my_tournaments_window_closed = page.ensure_element_disappears(my_tournaments_window, timeout=2)
            assert my_tournaments_window_closed, "'My Tournaments' window didn't close."
        screenshot_report['status'] = 'Passed'



class TestTabsInTabBar:

    def test_tabs_inside_poker_tab(self, app, screenshot_report):
        """In this test we try to click every tabs in 'Poker' tab and ensure that certain pages opens."""
        with allure.step("Initializing PokerPage."):
            page = PokerPage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find main lobby tabs (Poker, Casino, Promo, ...)"):
            lobby_tabs = page.find_main_lobby_tabs()
            assert lobby_tabs, "Lobby tabs not found on main page."

        with allure.step("Go to 'Poker' tab and find poker lobby tabs (Cash Tables, Tournaments, ...)"):
            lobby_tabs[0].click_input()
            poker_lobby_tabs = page.wait_for_poker_lobby_tabs(timeout=3)
            assert poker_lobby_tabs, "Poker lobby tabs not found on poker page."

        with allure.step("Go to 'Cash Tables' tab and find cash tables view."):
            poker_lobby_tabs[0].click_input()
            poker_lobby_cash_tables_view = page.wait_for_poker_lobby_cash_tables_view(timeout=3)
            assert poker_lobby_cash_tables_view, "Cash tables view didn't appear after clicking 'Cash Tables' tab."

        with allure.step("Go to 'Tournaments' tab and find tournaments view."):
            poker_lobby_tabs[1].click_input()
            poker_lobby_tournaments_view = page.wait_for_poker_lobby_tournaments_view(timeout=3)
            assert poker_lobby_tournaments_view, "Tournaments view didn't appear after clicking 'Tournaments' tab."

        with allure.step("Go to 'Sit & Go' tab and find tournaments view."):
            poker_lobby_tabs[2].click_input()
            poker_lobby_sit_and_go_tournaments_view = page.wait_for_poker_lobby_tournaments_view(timeout=3)
            assert poker_lobby_sit_and_go_tournaments_view, \
                "Tournaments view didn't appear after clicking 'Tournaments' tab."

        with allure.step("Go to 'Spins' tab and find spins view."):
            poker_lobby_tabs[3].click_input()
            poker_lobby_spins_view = page.wait_for_poker_lobby_spins_view(timeout=3)
            assert poker_lobby_spins_view, "Spins view didn't appear after clicking 'Spins' tab."
        screenshot_report['status'] = 'Passed'

    def test_tabs_inside_my_games_tab(self, app, screenshot_report):
        """In this test we try to click every tabs in 'My Games' tab and ensure that certain pages opens."""
        with allure.step("Initializing MyGamesPage."):
            page = MyGamesPage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Find main lobby tabs (Poker, Casino, Promo, ...)"):
            lobby_tabs = page.find_main_lobby_tabs()
            assert lobby_tabs, "Lobby tabs not found on main page."

        with allure.step("Go to 'My Games' tab and find my games lobby tabs (My Results, Tournaments, ...)"):
            lobby_tabs[4].click_input()
            my_games_lobby_tabs = page.wait_for_my_games_lobby_tabs(timeout=3)
            assert my_games_lobby_tabs, "My Games tabs didn't appear after clicking My Games tab."

        with allure.step("Go to 'My Results' tab and find my results view."):
            my_games_lobby_tabs[0].click_input()
            my_games_results_form = page.wait_for_my_games_results_form(timeout=3)
            assert my_games_results_form, "Results form didn't appear after clicking 'My Results' tab."

        with allure.step("Go to 'Tournaments' tab and find tournaments view."):
            my_games_lobby_tabs[1].click_input()
            my_games_tournaments_form = page.wait_for_my_games_tournaments_form(timeout=3)
            assert my_games_tournaments_form, "Tournaments form didn't appear after clicking 'Tournaments' tab."

        with allure.step("Go to 'Cash Hands' tab and find cash hands view."):
            my_games_lobby_tabs[2].click_input()
            my_games_cash_hands_form = page.wait_for_my_games_cash_hands_form(timeout=3)
            assert my_games_cash_hands_form, "Cash Hands form didn't appear after clicking 'Cash Hands' tab."

        with allure.step("Go to 'My Statistics' tab and find my statistics view."):
            my_games_lobby_tabs[3].click_input()
            my_games_my_statistics_form = page.wait_for_my_games_my_statistics_form(timeout=3)
            assert my_games_my_statistics_form, "My Statistics form didn't appear after clicking 'My Statistics' tab."

        with allure.step("Go to 'My Casino' tab and find my casino view."):
            my_games_lobby_tabs[4].click_input()
            my_games_my_casino_form = page.wait_for_my_games_my_casino_form(timeout=3)
            assert my_games_my_casino_form, "My Casino form didn't appear after clicking 'My Casino' tab."
        screenshot_report['status'] = 'Passed'

# pytest -s -v  --tb=short --alluredir=reports/allure

