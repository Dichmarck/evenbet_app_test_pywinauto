from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.LoginPage import LoginPage


def test_login_from_main_page(app):
    login_page = LoginPage(app)
    main_page_login_btn = login_page.should_be_main_page_login_button()
    main_page_login_btn.click_input()
    login_page.should_appear_login_window(timeout=2)
    login_page.print_username_in_login_username_field()
    login_page.print_password_in_login_username_field()
    login_btn = login_page.should_be_login_button()
    login_btn.click_input()
    login_page.should_appear_cashier_button(timeout=5)
    login_page.should_appear_show_balance_button(timeout=5)

