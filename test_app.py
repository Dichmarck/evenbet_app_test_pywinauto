import time
import allure
import pytest
from evenbet_app_test_pywinauto.utils import return_func_name, mouse_input, find_elem_by_text
from evenbet_app_test_pywinauto.pages.ChatDialogPage import ChatDialogPage
from evenbet_app_test_pywinauto.pages.TournamentLobbyPage import TournamentLobbyPage
from evenbet_app_test_pywinauto.pages.locators import WindowsLocators
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.MyGamesPage import MyGamesPage
from evenbet_app_test_pywinauto.pages.PokerPage import PokerPage
from evenbet_app_test_pywinauto.pages.PokerTablePage import PokerTablePage


# pytest -s -v --tb=short --alluredir=reports/allure
# allure serve reports/allure

def test_languages_list_appears_after_click_languages_button(app, screenshot_report):
    """In this test we try to click languages button and wait for list of languages."""
    with allure.step("Initializing PokerPage."):
        page = PokerPage(app=app)
        screenshot_report['window'] = app
        screenshot_report['file_name'] = return_func_name()
    with allure.step("Find languages button."):
        languages_button = page.wait_for_languages_button(timeout=3)
        assert languages_button, "Languages button not found on main page."
    with allure.step("Click languages button and wait for languages list."):
        languages_button.click_input()
        languages_list = page.wait_for_languages_list(timeout=3)
        assert languages_list, "No languages appeared after click languages button."
        mouse_input(languages_list[0])
        assert len(languages_list) >= 12, f"Not all languages found (should be 12, but {len(languages_list)} found)."
    with allure.step("Close languages list."):
        page.close_dialog_by_esc(languages_list[0])
        languages_list_closed = page.ensure_element_disappears(languages_list[0], timeout=3)
        assert languages_list_closed, "Language list didn't close."
    screenshot_report['status'] = 'passed'


class TestTournamentLobbyAndRegistration:

    @staticmethod
    def find_registering_tables(tables):
        registering_tables = []
        for table in tables:
            table_status = table.children()[2].window_text()
            if table_status == 'Registering':
                registering_tables.append(table)
        return registering_tables if len(registering_tables) != 0 else None

    def test_tournament_registration(self, app, screenshot_report):
        """In this test we try to open 'Tournaments' page, click 'Registration' button and find 'Register' button on
            appeared registration form."""
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
        with allure.step("Go to 'Tournaments' tab and find tables with status 'Registering'."):
            poker_lobby_tabs[1].click_input()
            tables = page.wait_for_tables_in_poker(timeout=3)
            assert tables, "No tables found on 'Tournament' page of 'Poker' tab."
            registering_tables = TestTournamentLobbyAndRegistration.find_registering_tables(tables)
            assert registering_tables, "No tables with status 'Registering' found on 'Tournament' page of 'Poker' tab."
        with allure.step("Click table with status 'Registering' and wait for 'Registration' button."):
            registering_tables[0].click_input()
            time.sleep(1)
            tour_reg_btn = page.wait_for_tournament_registration_button(timeout=3)
            assert tour_reg_btn, "Registration button not found on Tournaments page."
        with allure.step("Click Registration button and find Register button on appeared registration form."):
            tour_reg_btn.click_input()
            register_button = page.wait_for_register_button_on_tournament_registration_form(timeout=3)
            assert register_button, "Register button not found on tournament registration form."
            mouse_input(register_button)
        with allure.step("Close tournament registration form."):
            page.close_dialog_by_esc(register_button)
            tour_reg_form_closed = page.ensure_element_disappears(register_button, timeout=3)
            assert tour_reg_form_closed, "Tournament registration form didn't close."
        screenshot_report['status'] = 'passed'

    def test_tournament_lobby(self, app, screenshot_report):
        """In this test we try to open 'Tournaments' page, click 'Tournament Lobby' button and find Tournament
            lobby window. In window we test 'Status', 'Prize' and 'Satellites' tabs and find 'Cashier' button."""
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
        with allure.step("Go to 'Tournaments' tab and find tables."):
            poker_lobby_tabs[1].click_input()
            tables = page.wait_for_tables_in_poker(timeout=3)
            assert tables, "No tables found on 'Tournament' page of 'Poker' tab."
        with allure.step("Click table and find 'Tournament lobby' button."):
            tables[0].click_input()
            tour_lobby_btn = page.wait_for_tournament_lobby_button(timeout=3)
            assert tour_lobby_btn, "Tournament lobby button not found on Tournaments page."
        with allure.step("Click 'Tournament lobby' button and find tournament lobby window with tabs."):
            tour_lobby_btn.click_input()
            tour_lobby_window = page.wait_for_tournament_lobby_window(timeout=5)
            assert tour_lobby_window, "Tournament lobby window didn't appear after click 'Tournament lobby' button."
            tour_lobby_page = TournamentLobbyPage(app=tour_lobby_window)
            tabs = tour_lobby_page.find_tournament_lobby_tabs()
            assert tabs, "Tabs not found in Tournament lobby window."
        with allure.step("Click 'Status' tab and find status tab pane."):
            status_tab = find_elem_by_text(tabs, 'Status')
            assert status_tab, "'Status' tab not found in Tournament lobby tabbar."
            status_tab.click_input()
            status_pane = tour_lobby_page.wait_for_tournament_lobby_status_pane(timeout=3)
            assert status_pane, "Status pane didn't appear after click 'Status' tab in Tournament lobby tabbar."
            mouse_input(status_pane)
        with allure.step("Click 'Prize' tab and find status tab pane."):
            prize_tab = find_elem_by_text(tabs, 'Prize')
            assert prize_tab, "'Prize' tab not found in Tournament lobby tabbar."
            prize_tab.click_input()
            prize_pane = tour_lobby_page.wait_for_tournament_lobby_prize_pane(timeout=3)
            assert prize_pane, "Prize pane didn't appear after click 'Prize' tab in Tournament lobby tabbar."
            mouse_input(prize_pane)
        with allure.step("Click 'Satellites' tab and find status tab pane."):
            satellites_tab = find_elem_by_text(tabs, 'Satellites')
            assert satellites_tab, "'Satellites' tab not found in Tournament lobby tabbar."
            satellites_tab.click_input()
            satellites_pane = tour_lobby_page.wait_for_tournament_lobby_satellites_pane(timeout=3)
            assert satellites_pane, "Satellites pane didn't appear after click " \
                                    "'Satellites' tab in Tournament lobby tabbar."
            mouse_input(satellites_pane)

        with allure.step("Click 'Tables' and find 'SwipeView'"):
            tables_tab = find_elem_by_text(tabs, 'Tables')
            assert tables_tab, "'Tables' tab not found in Tournament lobby tabbar."
            tables_tab.click_input()
            swipe_view = tour_lobby_page.wait_for_swipe_view(timeout=3)
            assert swipe_view, "'SwipeView' didn't after click 'Tables' tab in Tournament lobby tabbar"
            mouse_input(swipe_view)
        with allure.step("Click 'Players' and find 'SwipeView'"):
            players_tab = find_elem_by_text(tabs, 'Players')
            assert players_tab, "'Players' tab not found in Tournament lobby tabbar."
            players_tab.click_input()
            swipe_view = tour_lobby_page.wait_for_swipe_view(timeout=3)
            assert swipe_view, "'SwipeView' didn't appear after click 'Players' tab in Tournament lobby tabbar"
            mouse_input(swipe_view)
        with allure.step("Click 'Structure' and find 'SwipeView'"):
            structure_tab = find_elem_by_text(tabs, 'Structure')
            assert structure_tab, "'Structure' tab not found in Tournament lobby tabbar."
            structure_tab.click_input()
            swipe_view = tour_lobby_page.wait_for_swipe_view(timeout=3)
            assert swipe_view, "'SwipeView' didn't after click 'Structure' tab in Tournament lobby tabbar"
            mouse_input(swipe_view)

        with allure.step("Find 'Cashier' button."):
            cashier_button = tour_lobby_page.wait_for_tournament_lobby_cashier_button(timeout=1)
            assert cashier_button, "Cashier button not found in Tournament lobby window."
            mouse_input(cashier_button)
        with allure.step("Close Tournament lobby window."):
            tour_lobby_page.close_window_by_alt_f4(tour_lobby_window)
            tour_lobby_window_closed = tour_lobby_page.ensure_element_disappears(tour_lobby_window, timeout=3)
            assert tour_lobby_window_closed, "Tournament lobby window didn't close."
        screenshot_report['status'] = 'passed'


class TestLeftMenuBar:

    @staticmethod
    def find_left_menu_button(page):
        with allure.step("Find left menu button."):
            left_menu_button = page.find_left_menu_button()
            assert left_menu_button, "Left Menu button not found on main page."
        return left_menu_button

    @staticmethod
    def find_left_menu_tabs(page):
        with allure.step("Find left menu tabs."):
            left_menu_tabs = page.wait_for_left_menu_tabs(timeout=2)
            assert left_menu_tabs, "Left menu tabs not found."
        return left_menu_tabs

    class TestAccount:
        """In this tests we try to open every tabs in 'Account' tab of left menu bar,
            wait for it's forms and close them."""

        def click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(self, page):
            left_menu_button = TestLeftMenuBar.find_left_menu_button(page=page)
            left_menu_button.click_input()
            left_menu_tabs = TestLeftMenuBar.find_left_menu_tabs(page=page)
            if 7 < len(left_menu_tabs) < 14 or len(left_menu_tabs) > 14:
                left_menu_tabs[0].click_input()
                left_menu_tabs = TestLeftMenuBar.find_left_menu_tabs(page=page)
            if len(left_menu_tabs) < 14:
                left_menu_tabs[1].click_input()
                left_menu_tabs = TestLeftMenuBar.find_left_menu_tabs(page=page)
            return left_menu_tabs

        def test_account_information(self, app, screenshot_report):
            """Test 'Account' -> 'Account information' tab."""
            with allure.step("Initializing BasePage."):
                page = BasePage(app=app)
                screenshot_report['window'] = app
                screenshot_report['file_name'] = return_func_name()
            tabs = self.click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(page=page)
            with allure.step("Click 'Account information' tab (2) and wait for account information form."):
                tabs[2].click_input()
                acc_inf_form = page.wait_for_account_information_form(timeout=2)
                assert acc_inf_form, "'Account information' form didn't appear " \
                                     "after click 'Account information' (2) tab."
                mouse_input(acc_inf_form)
            with allure.step("Close 'Account information' form."):
                page.close_dialog_by_esc(acc_inf_form)
                acc_inf_form_closed = page.ensure_element_disappears(acc_inf_form, timeout=3)
                assert acc_inf_form_closed, "'Account information' form didn't close."
            screenshot_report['status'] = 'passed'

        def test_account_change_password_form(self, app, screenshot_report):
            """Test 'Account' -> 'Change password' tab."""
            with allure.step("Initializing BasePage."):
                page = BasePage(app=app)
                screenshot_report['window'] = app
                screenshot_report['file_name'] = return_func_name()
            tabs = self.click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(page=page)
            with allure.step("Click 'Change password' tab (3) and wait for change password form."):
                tabs[3].click_input()
                account_change_password_form = page.wait_for_account_change_password_form(timeout=2)
                assert account_change_password_form, "'Change password' form didn't appear " \
                                                     "after click 'Change password' (3) tab."
                mouse_input(account_change_password_form)
            with allure.step("Close 'Change password' form."):
                page.close_dialog_by_esc(account_change_password_form)
                account_change_password_form_closed = page.ensure_element_disappears(account_change_password_form,
                                                                                     timeout=3)
                assert account_change_password_form_closed, "'Change password' form didn't close."
            screenshot_report['status'] = 'passed'

        def test_account_change_address_form(self, app, screenshot_report):
            """Test 'Account' -> 'Change address' tab."""
            with allure.step("Initializing BasePage."):
                page = BasePage(app=app)
                screenshot_report['window'] = app
                screenshot_report['file_name'] = return_func_name()
            tabs = self.click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(page=page)
            with allure.step("Click 'Change address' tab (4) and wait for change password form."):
                tabs[4].click_input()
                account_change_address_form = page.wait_for_account_change_address_form(timeout=2)
                assert account_change_address_form, "'Change address' form didn't appear " \
                                                    "after click 'Change address' (4) tab."
                mouse_input(account_change_address_form)
            with allure.step("Close 'Change address' form."):
                page.close_dialog_by_esc(account_change_address_form)
                account_change_address_form_closed = page.ensure_element_disappears(account_change_address_form,
                                                                                    timeout=3)
                assert account_change_address_form_closed, "'Change address' form didn't close."
            screenshot_report['status'] = 'passed'

        def test_account_verification_form(self, app, screenshot_report):
            """Test 'Account' -> 'Verification' tab."""
            with allure.step("Initializing BasePage."):
                page = BasePage(app=app)
                screenshot_report['window'] = app
                screenshot_report['file_name'] = return_func_name()
            tabs = self.click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(page=page)
            with allure.step("Click 'Verification' tab (5) and wait for change password form."):
                tabs[5].click_input()
                account_verification_form = page.wait_for_account_verification_form(timeout=2)
                assert account_verification_form, "'Verification' form didn't appear " \
                                                  "after click 'Verification' (5) tab."
                mouse_input(account_verification_form)
            with allure.step("Close 'Verification' form."):
                page.close_dialog_by_esc(account_verification_form)
                form_closed = page.ensure_element_disappears(account_verification_form, timeout=3)
                assert form_closed, "'Verification' form didn't close."
            screenshot_report['status'] = 'passed'

        def test_account_2fa_settings_form(self, app, screenshot_report):
            """Test 'Account' -> '2FA settings' tab."""
            with allure.step("Initializing BasePage."):
                page = BasePage(app=app)
                screenshot_report['window'] = app
                screenshot_report['file_name'] = return_func_name()
            tabs = self.click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(page=page)
            with allure.step("Click '2FA settings' tab (6) and wait for change password form."):
                tabs[6].click_input()
                account_2fa_settings_form = page.wait_for_account_2fa_settings_form(timeout=2)
                assert account_2fa_settings_form, "'2FA settings' form didn't appear " \
                                                  "after click '2FA settings' (6) tab."
                mouse_input(account_2fa_settings_form)
            with allure.step("Close '2FA settings' form."):
                page.close_dialog_by_esc(account_2fa_settings_form)
                form_closed = page.ensure_element_disappears(account_2fa_settings_form, timeout=3)
                assert form_closed, "'2FA settings' form didn't close."
            screenshot_report['status'] = 'passed'

        def test_account_change_avatar_form(self, app, screenshot_report):
            """Test 'Account' -> 'Change avatar' tab."""
            with allure.step("Initializing BasePage."):
                page = BasePage(app=app)
                screenshot_report['window'] = app
                screenshot_report['file_name'] = return_func_name()
            tabs = self.click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(page=page)
            with allure.step("Click 'Change avatar' tab (7) and wait for change password form."):
                tabs[7].click_input()
                account_change_avatar_form = page.wait_for_account_change_avatar_form(timeout=2)
                assert account_change_avatar_form, "'Change avatar' form didn't appear " \
                                                   "after click 'Change avatar' (7) tab."
                mouse_input(account_change_avatar_form)
            with allure.step("Close 'Change avatar' form."):
                page.close_dialog_by_esc(account_change_avatar_form)
                form_closed = page.ensure_element_disappears(account_change_avatar_form, timeout=3)
                assert form_closed, "'Change avatar' form didn't close."
            screenshot_report['status'] = 'passed'

        def test_account_delete_account_form(self, app, screenshot_report):
            """Test 'Account' -> 'Delete account' tab."""
            with allure.step("Initializing BasePage."):
                page = BasePage(app=app)
                screenshot_report['window'] = app
                screenshot_report['file_name'] = return_func_name()
            tabs = self.click_left_menu_button_open_account_tab_and_close_other_tabs_and_return_tabs(page=page)
            with allure.step("Click 'Delete account' tab (8) and wait for change password form."):
                tabs[8].click_input()
                account_delete_account_form = page.wait_for_account_delete_account_form(timeout=2)
                assert account_delete_account_form, "'Delete account' form didn't appear " \
                                                    "after click 'Delete account' (8) tab."
                mouse_input(account_delete_account_form)
            with allure.step("Close 'Delete account' form."):
                page.close_dialog_by_esc(account_delete_account_form)
                form_closed = page.ensure_element_disappears(account_delete_account_form, timeout=3)
                assert form_closed, "'Delete account' form didn't close."
            screenshot_report['status'] = 'passed'

    def test_create_table(self, app, screenshot_report):
        """In this test we try to open left menu, choose 'Create table' (-5) tab and wait for 'Create table' form 
            with 'Create table' button."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Open left menu and find tabs."):
            left_menu_button = self.find_left_menu_button(page=page)
            left_menu_button.click_input()
            tabs = self.find_left_menu_tabs(page=page)
        with allure.step("Click 'Create Table' tab (-5) and wait for Create table form."):
            tabs[-5].click_input()
            create_table_button = page.wait_for_create_table_button_on_create_table_form(timeout=3)
            assert create_table_button, "'Create table' form didn't appear after click 'Create table' (-5) tab."
            mouse_input(create_table_button)
        with allure.step("Close 'Create Table' form."):
            page.close_dialog_by_esc(create_table_button)
            create_table_closed = page.ensure_element_disappears(create_table_button, timeout=3)
            assert create_table_closed, "'Create table' didn't close."
        screenshot_report['status'] = 'passed'

    def test_my_tables(self, app, screenshot_report):
        """In this test we try to open left menu, choose 'My Tables' (-4) tab, wait for 'My Tables' dialog."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Open left menu and find tabs."):
            left_menu_button = self.find_left_menu_button(page=page)
            left_menu_button.click_input()
            tabs = self.find_left_menu_tabs(page=page)
        with allure.step("Click 'My Tables' tab (-4) and wait for my tables dialog."):
            tabs[-4].click_input()
            my_tables_dialog = page.wait_for_my_tables_dialog(timeout=3)
            assert my_tables_dialog, "'My Tables' dialog didn't appear after click 'My Tables' (-4) tab."
            mouse_input(my_tables_dialog)
        with allure.step("Close 'My tables' dialog."):
            page.close_dialog_by_esc(my_tables_dialog)
            my_tables_dialog_closed = page.ensure_element_disappears(my_tables_dialog, timeout=3)
            assert my_tables_dialog_closed, "'My Tables' form didn't close after click 'OK' button."
        screenshot_report['status'] = 'passed'

    def test_create_tournament(self, app, screenshot_report):
        """In this test we try to open left menu, choose 'Create tournament' (-3) tab
            and wait for 'Create tournament' form with 'Create tournament' button."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Open left menu and find tabs."):
            left_menu_button = self.find_left_menu_button(page=page)
            left_menu_button.click_input()
            tabs = self.find_left_menu_tabs(page=page)
        with allure.step("Click 'Create tournament' tab (-3) and wait for Create tournament form."):
            tabs[-3].click_input()
            create_tournament_button = page.wait_for_create_tournament_button_on_create_tournament_form(timeout=3)
            assert create_tournament_button, "'Create tournament' form didn't appear after " \
                                             "click 'Create tournament' (-3) tab."
            mouse_input(create_tournament_button)
        with allure.step("Close 'Create tournament' form."):
            page.close_dialog_by_esc(create_tournament_button)
            create_tournament_closed = page.ensure_element_disappears(create_tournament_button, timeout=3)
            assert create_tournament_closed, "'Create tournament' didn't close."
        screenshot_report['status'] = 'passed'

    def test_about(self, app, screenshot_report):
        """In this test we try to open left menu, choose 'About' (-2) tab, wait for 'About' form with 'OK' button 
                and click it"""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        with allure.step("Open left menu and find tabs."):
            left_menu_button = self.find_left_menu_button(page=page)
            left_menu_button.click_input()
            tabs = self.find_left_menu_tabs(page=page)
        with allure.step("Click 'About' tab (-2) and wait for About form."):
            tabs[-2].click_input()
            ok_button = page.wait_for_ok_button_on_about_form(timeout=3)
            assert ok_button, "'About' form didn't appear after click 'About' (-2) tab."
        with allure.step("Click 'OK' button."):
            ok_button.click_input()
            ok_button_closed = page.ensure_element_disappears(ok_button, timeout=3)
            assert ok_button_closed, "'About' form didn't close after click 'OK' button."
        screenshot_report['status'] = 'passed'


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
            mouse_input(cashier_window)
        with allure.step("Close Cashier window."):
            BasePage.close_window_by_alt_f4(cashier_window)
            window_closed = BasePage.ensure_element_disappears(cashier_window, timeout=3)
            assert window_closed, "Cashier window didn't close."
        screenshot_report['status'] = 'Passed'

    def test_poker_table_appears_after_click_play_button_on_cash_tables_page(self, app, screenshot_report):
        """In this test we try to click 'Play' button, ensure that 'Poker Table' window opens and close it."""
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
        with allure.step("Go to 'Cash Tables' tab and find cash tables."):
            poker_lobby_tabs[0].click_input()
            cash_tables = page.wait_for_tables_in_poker(timeout=3)
            assert cash_tables, "No tables found on 'Cash Tables' page of 'Poker' tab."
        with allure.step("Click table and wait for 'Play' button."):
            cash_tables[0].click_input()
            play_button = page.wait_for_play_button(timeout=3)
            assert play_button, "Play button not found after click table on 'Cash tables' page."
        with allure.step("Click 'Play' button and wait for Poker Table window and connect to it."):
            play_button.click_input()
            poker_table_window = WindowsLocators.poker_table_window(timeout=10)
            assert poker_table_window, "Poker window didn't appear after click Play button."
            mouse_input(poker_table_window)
            poker_page = PokerTablePage(app=poker_table_window)
        with allure.step("Find and close BuyIn form."):
            buy_in_form = poker_page.wait_for_buy_in_form(timeout=3)
            if buy_in_form:
                mouse_input(buy_in_form)
                PokerPage.close_dialog_by_esc(buy_in_form)
            buy_in_form_closed = PokerPage.ensure_element_disappears(buy_in_form, timeout=2)
            assert buy_in_form_closed, "Buy In form didn't close."
        with allure.step("Close Poker Table window."):
            PokerTablePage.close_window_by_alt_f4(poker_table_window)
            poker_table_window_closed = PokerTablePage.ensure_element_disappears(poker_table_window, timeout=3)
            assert poker_table_window_closed, "Poker Table window didn't close."
        screenshot_report['status'] = 'Passed'


class TestRightTopSettings:

    def click_right_top_settings_button_and_find_tabs(self, app):
        with allure.step("Find right top settings button."):
            page = BasePage(app=app)
            right_top_settings_button = page.find_right_top_settings_button()
            assert right_top_settings_button, "Right top settings button not found on main page."
        with allure.step("Click settings button and wait for tabs in settings menu."):
            right_top_settings_button.click_input()
            settings_tabs = page.wait_for_right_top_settings_tabs(timeout=3)
            assert settings_tabs, "Settings menu didn't appear after click right top settings button."
        return settings_tabs

    def test_settings_sounds(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'Sounds' settings tab,
                check that 'Sounds settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        settings_tabs = self.click_right_top_settings_button_and_find_tabs(app)
        with allure.step("Click 'Sounds settings' tab and wait for 'Sounds Settings' form."):
            settings_tabs[0].click_input()
            sounds_settings_form = page.wait_for_sounds_settings_form(timeout=2)
            assert sounds_settings_form, "Sounds settings form didn't appear " \
                                         "after click 'Sounds' tab in right top settings menu."
            mouse_input(sounds_settings_form)
        with allure.step("Close 'Sounds' settings form."):
            page.close_dialog_by_esc(sounds_settings_form)
            sounds_settings_form_closed = page.ensure_element_disappears(sounds_settings_form, timeout=3)
            assert sounds_settings_form_closed, "'Sounds settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_rates_slider(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'Rates Slider' settings tab,
                check that 'Rates slider settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        settings_tabs = self.click_right_top_settings_button_and_find_tabs(app)
        with allure.step("Click 'Rates Slider settings' tab and wait for 'Sounds Settings' form."):
            settings_tabs[1].click_input()
            rates_slider_settings_form = page.wait_for_rates_slider_settings_form(timeout=2)
            assert rates_slider_settings_form, "Rates slider settings form didn't appear " \
                                               "after click 'Rates Slider' tab in right top settings menu."
            mouse_input(rates_slider_settings_form)
        with allure.step("Close 'Rates Slider settings' form."):
            page.close_dialog_by_esc(rates_slider_settings_form)
            rates_slider_settings_form_closed = page.ensure_element_disappears(rates_slider_settings_form, timeout=3)
            assert rates_slider_settings_form_closed, "'Rates slider settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_system_chat(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'System & chat' settings tab,
                check that 'System & Chat settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        settings_tabs = self.click_right_top_settings_button_and_find_tabs(app)
        with allure.step("Click 'System & Chat settings' tab and wait for 'System & Chat' form."):
            settings_tabs[2].click_input()
            system_chat_settings_form = page.wait_for_system_chat_settings_form(timeout=2)
            assert system_chat_settings_form, "System & chat settings form didn't appear " \
                                              "after click 'System & Chat' tab in right top settings menu."
            mouse_input(system_chat_settings_form)
        with allure.step("Close 'System & Chat settings' form."):
            page.close_dialog_by_esc(system_chat_settings_form)
            system_chat_settings_form_closed = page.ensure_element_disappears(system_chat_settings_form, timeout=3)
            assert system_chat_settings_form_closed, "'System & Chat settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_buyin_rebuy(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'BuyIn & rebuy' settings tab,
                check that 'BuyIn & Rebuy settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        settings_tabs = self.click_right_top_settings_button_and_find_tabs(app)
        with allure.step("Click 'BuyIn & Rebuy settings' tab and wait for 'BuyIn & rebuy' form."):
            settings_tabs[3].click_input()
            buyin_rebuy_settings_form = page.wait_for_buyin_rebuy_settings_form(timeout=2)
            assert buyin_rebuy_settings_form, "BuyIn & Rebuy settings form didn't appear " \
                                              "after click 'BuyIn & rebuy' tab in right top settings menu."
            mouse_input(buyin_rebuy_settings_form)
        with allure.step("Close 'BuyIn & Rebuy settings' form."):
            page.close_dialog_by_esc(buyin_rebuy_settings_form)
            buyin_rebuy_settings_form_closed = page.ensure_element_disappears(buyin_rebuy_settings_form, timeout=3)
            assert buyin_rebuy_settings_form_closed, "'BuyIn & rebuy settings' form didn't close."
        screenshot_report['status'] = 'passed'

    def test_settings_table(self, app, screenshot_report):
        """In this test we try to press right top settings button, choose 'Table settings' tab,
                        check that 'Table settings' window appears and then close it."""
        with allure.step("Initializing BasePage."):
            page = BasePage(app=app)
            screenshot_report['window'] = app
            screenshot_report['file_name'] = return_func_name()
        settings_tabs = self.click_right_top_settings_button_and_find_tabs(app)
        with allure.step("Click 'Table settings' settings tab and wait for 'Table settings' form."):
            settings_tabs[4].click_input()
            table_settings_form = page.wait_for_table_settings_form(timeout=2)
            assert table_settings_form, "Table settings form didn't appear " \
                                        "after click 'Table settings' tab in right top settings menu."
            mouse_input(table_settings_form)
        with allure.step("Close 'Table settings' form."):
            page.close_dialog_by_esc(table_settings_form)
            table_settings_form_closed = page.ensure_element_disappears(table_settings_form, timeout=3)
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
            mouse_input(chat_dialog)
        with allure.step("Generate new message and check that message is not contained in chat yet."):
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
            mouse_input(my_tables_dialog)
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
            mouse_input(my_tournaments_window)
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
            mouse_input(poker_lobby_cash_tables_view)

        with allure.step("Go to 'Tournaments' tab and find tournaments view."):
            poker_lobby_tabs[1].click_input()
            poker_lobby_tournaments_view = page.wait_for_poker_lobby_tournaments_view(timeout=3)
            assert poker_lobby_tournaments_view, "Tournaments view didn't appear after clicking 'Tournaments' tab."
            mouse_input(poker_lobby_tournaments_view)

        with allure.step("Go to 'Sit & Go' tab and find tournaments view."):
            poker_lobby_tabs[2].click_input()
            poker_lobby_sit_and_go_tournaments_view = page.wait_for_poker_lobby_tournaments_view(timeout=3)
            assert poker_lobby_sit_and_go_tournaments_view, \
                "Tournaments view didn't appear after clicking 'Tournaments' tab."
            mouse_input(poker_lobby_sit_and_go_tournaments_view)

        with allure.step("Go to 'Spins' tab and find spins view."):
            poker_lobby_tabs[3].click_input()
            poker_lobby_spins_view = page.wait_for_poker_lobby_spins_view(timeout=3)
            assert poker_lobby_spins_view, "Spins view didn't appear after clicking 'Spins' tab."
            mouse_input(poker_lobby_spins_view)
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
            mouse_input(my_games_results_form)

        with allure.step("Go to 'Tournaments' tab and find tournaments view."):
            my_games_lobby_tabs[1].click_input()
            my_games_tournaments_form = page.wait_for_my_games_tournaments_form(timeout=3)
            assert my_games_tournaments_form, "Tournaments form didn't appear after clicking 'Tournaments' tab."
            mouse_input(my_games_tournaments_form)

        with allure.step("Go to 'Cash Hands' tab and find cash hands view."):
            my_games_lobby_tabs[2].click_input()
            my_games_cash_hands_form = page.wait_for_my_games_cash_hands_form(timeout=3)
            assert my_games_cash_hands_form, "Cash Hands form didn't appear after clicking 'Cash Hands' tab."
            mouse_input(my_games_cash_hands_form)

        with allure.step("Go to 'My Statistics' tab and find my statistics view."):
            my_games_lobby_tabs[3].click_input()
            my_games_my_statistics_form = page.wait_for_my_games_my_statistics_form(timeout=3)
            assert my_games_my_statistics_form, "My Statistics form didn't appear after clicking 'My Statistics' tab."
            mouse_input(my_games_my_statistics_form)

        with allure.step("Go to 'My Casino' tab and find my casino view."):
            my_games_lobby_tabs[4].click_input()
            my_games_my_casino_form = page.wait_for_my_games_my_casino_form(timeout=3)
            assert my_games_my_casino_form, "My Casino form didn't appear after clicking 'My Casino' tab."
            mouse_input(my_games_my_casino_form)
        screenshot_report['status'] = 'Passed'

# pytest -s -v  --tb=short --alluredir=reports/allure
