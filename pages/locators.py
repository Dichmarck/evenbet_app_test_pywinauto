import re
import pywinauto
import time


def find_element_or_none(element, timeout=0):
    time_start = time.time()
    while time.time() - time_start <= timeout:
        try:
            return element.wrapper_object()
        except pywinauto.findwindows.ElementNotFoundError:
            pass
    return None


class WindowsLocators:

    @staticmethod
    def cashier_window(timeout=0):
        try:
            cashier_app = pywinauto.Application(backend='uia').connect(class_name_re="CashierDesktopWindow_QMLTYPE_*",
                                                                       timeout=timeout)
            return find_element_or_none(cashier_app.window(class_name_re="CashierDesktopWindow_QMLTYPE_*"),
                                        timeout=timeout)
        except Exception:
            return None

    @staticmethod
    def poker_table_window(timeout=0):
        try:
            poker_table_window = pywinauto.Application(backend='uia'). \
                connect(class_name_re="TableDesktopWindow_QMLTYPE_*", timeout=timeout). \
                window(class_name_re="TableDesktopWindow_QMLTYPE_*")
            return poker_table_window
        except Exception:
            return None

    @staticmethod
    def my_tournaments_window(timeout=0):
        try:
            my_tours_app = pywinauto.Application(backend='uia').connect(class_name_re="DesktopDialog_QMLTYPE_*",
                                                                        timeout=timeout)
            return find_element_or_none(my_tours_app.window(class_name_re="DesktopDialog_QMLTYPE_*").
                                        child_window(class_name_re="MyTournamentsForm_QMLTYPE_*"), timeout=timeout)
        except Exception:
            return None

    @staticmethod
    def tournament_lobby_window(timeout=0):
        try:
            tournament_lobby_app = pywinauto.Application(backend='uia'). \
                connect(class_name_re="TournamentLobbyDesktopWindow*", timeout=timeout). \
                window(class_name_re="TournamentLobbyDesktopWindow*")
            return tournament_lobby_app
        except Exception:
            return None


class BasePageLocators:

    @staticmethod
    def close_app_right_top_button(app, timeout=0):
        return find_element_or_none(app.child_window(control_type="TitleBar").Button3, timeout=timeout)

    @staticmethod
    def fullscreen_button(app, timeout=0):
        return find_element_or_none(app.child_window(control_type="TitleBar").Button2, timeout=timeout)

    @staticmethod
    def yes_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PDialogButtonBox_QMLTYPE_*").
                                    child_window(class_name_re="PButton_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def login_window(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="LoginPanel_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def close_login_window_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                    child_window(class_name_re="PButtonWithIcon_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def login_button_main_page(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PLoginButton_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def show_user_balance_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="UserInfoBalanceButton_*"), timeout=timeout)

    @staticmethod
    def main_lobby_tabs(app, timeout=0):
        try:
            main_lobby_tabbar = find_element_or_none(app.child_window(class_name_re="LobbyPagesTabBar_QMLTYPE_*"),
                                                     timeout=timeout)
            tabs = main_lobby_tabbar.children()
            return tabs if len(tabs) != 0 else None
        except Exception:
            return None

    @staticmethod
    def cashier_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re=r"PButton_QMLTYPE_[\d]{1,3}$"))

    @staticmethod
    def play_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PokerLobbyCashTableDetailsView_QMLTYPE_*").
                                    child_window(class_name_re="PButtonPrimary_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def right_bottom_buttons(app, timeout=0):
        try:
            buttons = app.descendants(control_type="Button")
            right_bot_buttons = []
            for button in buttons:
                if re.fullmatch(r"PButton_QMLTYPE_[\d]{1,3}_QML_[\d]{1,3}$", button.class_name()) and \
                        re.fullmatch(r"[\d]+", button.window_text()):
                    right_bot_buttons.append(button)
            return right_bot_buttons if len(right_bot_buttons) != 0 else None
        except Exception:
            return None

    @staticmethod
    def chat_dialog(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="LobbyChat_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def my_tables_dialog(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="Stub_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def right_top_settings_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PComboBox_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def right_top_settings_tabs(app, timeout=0):
        popup_settings_menu = find_element_or_none(app.child_window(class_name="QQuickPopupItem"), timeout=timeout)
        try:
            settings_tabs = popup_settings_menu.children(control_type="MenuItem")
            return settings_tabs if len(settings_tabs) != 0 else None
        except Exception:
            return None

    @staticmethod
    def sounds_settings_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="SoundsForm_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def rates_slider_settings_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="RatesSliderFormTemplate_*"), timeout=timeout)

    @staticmethod
    def system_chat_settings_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="SystemChatForm_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def buyin_rebuy_settings_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="BuyInRebuyForm_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def table_settings_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="TableSettingsForm_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def left_menu_button(app):
        buttons = app.descendants(control_type="Button")
        for button in buttons:
            if "PButtonWithIcon_QMLTYPE_" in button.class_name():
                return button
        return None

    @staticmethod
    def left_menu_tabs(app, timeout=0):
        left_menu_bar = find_element_or_none(app.child_window(class_name="QQuickPopupItem"), timeout=timeout)
        try:
            tabs = left_menu_bar.children(control_type="ListItem")
            return tabs if len(tabs) != 0 else None
        except Exception:
            return None

    @staticmethod
    def account_information_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="AccountInformationFormTemplate_*"), timeout=timeout)

    @staticmethod
    def account_change_password_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="ChangePasswordFormTemplate*"), timeout=timeout)

    @staticmethod
    def account_change_address_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="ChangeAddressFormTemplate*"), timeout=timeout)

    @staticmethod
    def account_verification_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="VerificationFormTemplate*"), timeout=timeout)

    @staticmethod
    def account_2fa_settings_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="TFASettingsFormTemplate*"), timeout=timeout)

    @staticmethod
    def account_change_avatar_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="ChangeAvatarFormTemplate*"), timeout=timeout)

    @staticmethod
    def account_delete_account_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="MessageBoxDesktopDialog*"), timeout=timeout)

    @staticmethod
    def logout_dialog_yes_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="MessageBoxDesktopDialog_*").
                                    child_window(class_name_re="PButton_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def create_table_button_on_create_table_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="CreateTableFormTemplate_*").
                                    child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)

    @staticmethod
    def create_tournament_button_on_create_tournament_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="CreateTournamentFormTemplate_*").
                                    child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)

    @staticmethod
    def ok_button_on_about_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="AboutForm_QMLTYPE_*").
                                    child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)

    @staticmethod
    def languages_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PComboBoxLanguages_*"), timeout=timeout)

    @staticmethod
    def languages_list(app, timeout=0):
        languages_popup_item = find_element_or_none(app.child_window(class_name="QQuickPopupItem"), timeout=timeout)
        try:
            list_items = languages_popup_item.children(control_type="ListItem")
            languages = []
            for item in list_items:
                if "PItemDelegateLanguages" in item.class_name():
                    languages.append(item)
            return languages if len(languages) != 0 else None
        except Exception:
            return None



class LoginPageLocators(BasePageLocators):
    @staticmethod
    def username_field(app, timeout=0):
        return find_element_or_none(app.Edit1, timeout=timeout)

    @staticmethod
    def password_field(app, timeout=0):
        return find_element_or_none(app.Edit2, timeout=timeout)

    @staticmethod
    def login_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                    child_window(class_name_re="PButtonPrimary_QMLTYPE_*"), timeout=timeout)

    @staticmethod
    def signup_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                    child_window(class_name_re="PButtonQuaternary_QMLTYPE_*"), timeout=timeout)


class PokerPageLocators(BasePageLocators):

    @staticmethod
    def poker_lobby_tabs(app, timeout=0):
        try:
            poker_lobby_main_view_tabbar = find_element_or_none(
                app.child_window(class_name_re="PokerLobbyMainViewTabBar_QMLTYPE_*"), timeout=timeout)
            tabs = poker_lobby_main_view_tabbar.children()
            return tabs if len(tabs) != 0 else None
        except Exception:
            return None

    @staticmethod
    def poker_lobby_cash_tables_view(app, timeout=0):
        cash_tables_view = find_element_or_none(app.child_window(class_name_re="PokerLobbyCashTablesView_QMLTYPE_*"),
                                                timeout=timeout)
        return cash_tables_view

    @staticmethod
    def poker_lobby_tournaments_view(app, timeout=0):
        tournaments_view = find_element_or_none(app.child_window(class_name_re="PokerLobbyTournamentsView_QMLTYPE_*"),
                                                timeout=timeout)
        return tournaments_view

    @staticmethod
    def poker_lobby_spins_view(app, timeout=0):
        spins_view = find_element_or_none(app.child_window(class_name_re="PokerLobbySpinsView_QMLTYPE_*"),
                                          timeout=timeout)
        return spins_view

    @staticmethod
    def tournament_registration_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PokerLobbyTournamentDetailsView_*").
                                    child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)

    @staticmethod
    def register_button_on_tournament_registration_form(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="TournamentRegistrationForm_*").
                                    child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)

    @staticmethod
    def tournament_lobby_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PokerLobbyTournamentDetailsView_*").
                                    child_window(class_name_re="PButtonSecondary*"), timeout=timeout)

    @staticmethod
    def poker_tables(app, timeout=0):
        time_start = time.time()
        while time.time() - time_start <= timeout:
            try:
                list_items = app.descendants(control_type="ListItem")
                tables = []
                for item in list_items:
                    if "TableViewItemDelegate_" in item.class_name():
                        tables.append(item)
                if len(tables) != 0:
                    return tables
            except Exception:
                pass
        return None


class MyGamesPageLocators(BasePageLocators):
    @staticmethod
    def my_games_lobby_tabs(app, timeout=0):
        try:
            my_games_lobby_tabbar = find_element_or_none(
                app.child_window(class_name_re="MyGamesLobbyPageTabBar_QMLTYPE_*"), timeout=timeout)
            tabs = my_games_lobby_tabbar.children()
            return tabs if len(tabs) != 0 else None
        except Exception:
            return None

    @staticmethod
    def my_games_results_form(app, timeout=0):
        my_games_results_form = find_element_or_none(app.child_window(class_name_re="MyGamesMyResultsForm_QMLTYPE_*"),
                                                     timeout=timeout)
        return my_games_results_form

    @staticmethod
    def my_games_tournaments_form(app, timeout=0):
        my_games_tournaments_form = find_element_or_none(
            app.child_window(class_name_re="MyGamesTournamentsForm_QMLTYPE_*"), timeout=timeout)
        return my_games_tournaments_form

    @staticmethod
    def my_games_cash_hands_form(app, timeout=0):
        my_games_cash_hands_form = find_element_or_none(
            app.child_window(class_name_re="MyGamesCashHandsForm_QMLTYPE_*"), timeout=timeout)
        return my_games_cash_hands_form

    @staticmethod
    def my_games_my_statistics_form(app, timeout=0):
        my_games_my_statistics_form = find_element_or_none(
            app.child_window(class_name_re="MyGamesMyStatisticsForm_QMLTYPE_*"), timeout=timeout)
        return my_games_my_statistics_form

    @staticmethod
    def my_games_my_casino_form(app, timeout=0):
        my_games_my_casino_form = find_element_or_none(
            app.child_window(class_name_re="MyGamesCasinoForm_QMLTYPE_*"), timeout=timeout)
        return my_games_my_casino_form


class ChatDialogPageLocators(BasePageLocators):

    @staticmethod
    def chat_text_field(app, timeout=0):
        chat_text_field = find_element_or_none(app.child_window(class_name_re="ChatTextField_QMLTYPE_*"),
                                               timeout=timeout)
        return chat_text_field

    @staticmethod
    def chat_messages_str_list(app, timeout=0):
        chat_messages_str_list = []
        chat = find_element_or_none(app.child_window(class_name_re="LobbyChat_QMLTYPE_*"), timeout=timeout)
        chat_messages = chat.descendants(control_type="Edit")
        for message in chat_messages:
            chat_messages_str_list.append(message.window_text())
        return chat_messages_str_list


class PokerTablePageLocators(BasePageLocators):

    @staticmethod
    def buy_in_form(app, timeout=0):
        buy_in_form = find_element_or_none(app.child_window(class_name_re="BuyInForm_QMLTYPE_*"), timeout=timeout)
        return buy_in_form


class TournamentsLobbyPageLocators(BasePageLocators):

    @staticmethod
    def tabs(app, timeout=0):
        tabbar = find_element_or_none(app.child_window(class_name_re="PTabBarHeader_*"), timeout=timeout)
        try:
            tabs = tabbar.children()
            return tabs if len(tabs) != 0 else None
        except Exception:
            return None

    @staticmethod
    def status_pane(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="TournamentStatusTab_*"), timeout=timeout)

    @staticmethod
    def prize_pane(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="TournamentPrizeTab*"), timeout=timeout)

    @staticmethod
    def satellites_pane(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="TournamentSatellitesTab*"), timeout=timeout)

    @staticmethod
    def cashier_button(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="PButtonSecondary_*"), timeout=timeout)

    @staticmethod
    def swipe_view(app, timeout=0):
        return find_element_or_none(app.child_window(class_name_re="SwipeView_QMLTYPE_*"), timeout=timeout)