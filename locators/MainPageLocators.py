import pywinauto
from .locators_utils import find_element_or_none
import re


def close_main_win_right_top_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(control_type="TitleBar").Button3, timeout=timeout)


def fullscreen_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(control_type="TitleBar").Button2, timeout=timeout)


def yes_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="PDialogButtonBox_QMLTYPE_*").
                                child_window(class_name_re="PButton_QMLTYPE_*"), timeout=timeout)


def login_window(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="LoginPanel_QMLTYPE_*"), timeout=timeout)


def login_button_main_page(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="PLoginButton_QMLTYPE_*"), timeout=timeout)


def show_user_balance_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="UserInfoBalanceButton_*"), timeout=timeout)


def main_lobby_tabs(main_win, timeout=0):
    try:
        main_lobby_tabbar = find_element_or_none(main_win.child_window(class_name_re="LobbyPagesTabBar_QMLTYPE_*"),
                                                 timeout=timeout)
        tabs = main_lobby_tabbar.children()
        return tabs if len(tabs) != 0 else None
    except Exception:
        return None


def cashier_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re=r"PButton_QMLTYPE_[\d]{1,3}$"), timeout=timeout)


def play_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="PokerLobbyCashTableDetailsView_QMLTYPE_*").
                                child_window(class_name_re="PButtonPrimary_QMLTYPE_*"), timeout=timeout)


def right_bottom_buttons(main_win, timeout=0):
    try:
        buttons = main_win.descendants(control_type="Button")
        right_bot_buttons = []
        for button in buttons:
            if re.fullmatch(r"PButton_QMLTYPE_[\d]{1,3}_QML_[\d]{1,3}$", button.class_name()) and \
                    re.fullmatch(r"[\d]+", button.window_text()):
                right_bot_buttons.append(button)
        return right_bot_buttons if len(right_bot_buttons) != 0 else None
    except Exception:
        return None


def chat_dialog(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="LobbyChat_QMLTYPE_*"), timeout=timeout)


def my_tables_dialog(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="Stub_QMLTYPE_*"), timeout=timeout)


def right_top_settings_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="PComboBox_QMLTYPE_*"), timeout=timeout)


def right_top_settings_tabs(main_win, timeout=0):
    popup_settings_menu = find_element_or_none(main_win.child_window(class_name="QQuickPopupItem"), timeout=timeout)
    try:
        settings_tabs = popup_settings_menu.children(control_type="MenuItem")
        return settings_tabs if len(settings_tabs) != 0 else None
    except Exception:
        return None


def sounds_settings_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="SoundsForm_QMLTYPE_*"), timeout=timeout)


def rates_slider_settings_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="RatesSliderFormTemplate_*"), timeout=timeout)


def system_chat_settings_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="SystemChatForm_QMLTYPE_*"), timeout=timeout)


def buyin_rebuy_settings_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="BuyInRebuyForm_QMLTYPE_*"), timeout=timeout)


def table_settings_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="TableSettingsForm_QMLTYPE_*"), timeout=timeout)


def left_menu_button(main_win):
    try:
        buttons = main_win.descendants(control_type="Button")
        for button in buttons:
            if "PButtonWithIcon_QMLTYPE_" in button.class_name():
                return button
        return None
    except Exception:
        return None


def left_menu_tabs(main_win, timeout=0):
    try:
        left_menu_bar = find_element_or_none(main_win.child_window(class_name="QQuickPopupItem"), timeout=timeout)
        tabs = left_menu_bar.children(control_type="ListItem")
        return tabs if len(tabs) != 0 else None
    except Exception:
        return None


def account_information_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="AccountInformationFormTemplate_*"), timeout=timeout)


def account_change_password_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="ChangePasswordFormTemplate*"), timeout=timeout)


def account_change_address_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="ChangeAddressFormTemplate*"), timeout=timeout)


def account_verification_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="VerificationFormTemplate*"), timeout=timeout)


def account_2fa_settings_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="TFASettingsFormTemplate*"), timeout=timeout)


def account_change_avatar_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="ChangeAvatarFormTemplate*"), timeout=timeout)


def account_delete_account_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="MessageBoxDesktopDialog*"), timeout=timeout)


def logout_dialog_yes_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="MessageBoxDesktopDialog_*").
                                child_window(class_name_re="PButton_QMLTYPE_*"), timeout=timeout)


def create_table_button_on_create_table_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="CreateTableFormTemplate_*").
                                child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)


def create_tournament_button_on_create_tournament_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="CreateTournamentFormTemplate_*").
                                child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)


def ok_button_on_about_form(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="AboutForm_QMLTYPE_*").
                                child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)


def languages_button(main_win, timeout=0):
    return find_element_or_none(main_win.child_window(class_name_re="PComboBoxLanguages_*"), timeout=timeout)


def languages_list(main_win, timeout=0):
    languages_popup_item = find_element_or_none(main_win.child_window(class_name="QQuickPopupItem"), timeout=timeout)
    try:
        list_items = languages_popup_item.children(control_type="ListItem")
        languages = []
        for item in list_items:
            if "PItemDelegateLanguages" in item.class_name():
                languages.append(item)
        return languages if len(languages) != 0 else None
    except Exception:
        return None
