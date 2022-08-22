from ..pages.MainPage import MainPage
from ..locators import LoginDialogLocators, MainPageLocators
from ..constants import PASSWORD, USERNAME
from ..utils import timer


class LoginDialog(MainPage):

    @timer("Close login window button")
    def find_close_login_window_button(self):
        close_login_window_button = MainPageLocators.close_login_window_button(self.app)
        return close_login_window_button

    @timer("Login username field")
    def find_login_username_field(self):
        username_field = LoginDialogLocators.username_field(self.app)
        return username_field

    @timer("Login password field")
    def find_login_password_field(self):
        password_field = LoginDialogLocators.password_field(self.app)
        return password_field

    @timer("Login button")
    def find_login_button(self):
        login_button = LoginDialogLocators.login_button(self.app)
        return login_button

    @timer("SignUp button")
    def find_signup_button(self):
        signup_button = LoginDialogLocators.signup_button(self.app)
        return signup_button

    @timer("Print username")
    def print_username_in_login_username_field(self, username_field):
        username_field.click_input()
        username_field.type_keys(USERNAME)

    @timer("Print password")
    def print_password_in_login_username_field(self, password_field):
        password_field.click_input()
        password_field.type_keys(PASSWORD)


