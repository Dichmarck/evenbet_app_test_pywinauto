import allure
from evenbet_app_test_pywinauto.utils import return_func_name, mouse_input
from evenbet_app_test_pywinauto.pages.BasePage import BasePage


def test_logout_from_left_menu(app, screenshot_report):
    """Im this test we try to open left menu, choose 'Logout' tab, click 'Yes' button on logout dialog
        and find 'Login' button on main page."""
    with allure.step("Initializing MyGamesPage."):
        page = BasePage(app=app)
        screenshot_report['window'] = app
        screenshot_report['file_name'] = return_func_name()
    with allure.step("Find left menu button."):
        left_menu_button = page.find_left_menu_button()
        assert left_menu_button, "Left Menu button not found on main page."
    with allure.step("Click left menu button and find left menu tabs."):
        left_menu_button.click_input()
        left_menu_tabs = page.wait_for_left_menu_tabs(timeout=2)
        assert left_menu_tabs, "Left menu tabs not found."
    with allure.step("Click 'Logout' (last) tab and wait for logout dialog with 'Yes' button."):
        left_menu_tabs[-1].click_input()
        logout_dialog_yes_btn = page.wait_for_logout_dialog_yes_button(timeout=2)
        assert logout_dialog_yes_btn, "Logout form with 'Yes' button didn't appear after click 'Logout' left menu tab."
    with allure.step("Click 'Yes' button and wait for 'Login' button on main page."):
        logout_dialog_yes_btn.click_input()
        main_page_login_button = page.wait_for_main_page_login_button(timeout=5)
        assert main_page_login_button, "Main page 'Login' button didn't appear after click 'Yes' " \
                                       "button on logout dialog."
        mouse_input(main_page_login_button)
    screenshot_report['status'] = 'passed'
