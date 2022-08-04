import allure

from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages.LoginPage import LoginPage
from evenbet_app_test_pywinauto.pages.RegistraionPage import SignUpPage


def test_login_from_main_page(app):
    """In this test we try to open login-form, type username and password in it's fields,
    click 'LOGIN' button and ensure, that 'Cashier' and 'Show balance' buttons appear."""
    login_page = LoginPage(app)
    with allure.step("Find and click 'Login' button on main page."):
        main_page_login_btn = login_page.should_be_main_page_login_button()
        main_page_login_btn.click_input()
    with allure.step("Find login form and type username and password in it's fields."):
        login_page.should_appear_login_window(timeout=2)
        login_page.print_username_in_login_username_field()
        login_page.print_password_in_login_username_field()
    with allure.step("Find and click 'Login' button in login form."):
        login_btn = login_page.should_be_login_button()
        login_btn.click_input()
    with allure.step("Check 'Cashier' and 'Show Balance' buttons on main page."):
        login_page.should_appear_cashier_button(timeout=5)
        login_page.should_appear_show_balance_button(timeout=5)


#def test_registration_from_main_page(app):
#    signup_page = SignUpPage(app)
#    main_page_login_btn = signup_page.should_be_main_page_login_button()
#    main_page_login_btn.click_input()
#    signup_page.should_appear_login_window(timeout=2)
#    signup_btn = signup_page.should_be_signup_button()
#    signup_btn.click_input()




