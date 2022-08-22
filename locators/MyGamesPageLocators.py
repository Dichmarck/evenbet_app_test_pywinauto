import pywinauto
from .locators_utils import find_element_or_none


def my_games_lobby_tabs(my_games_page, timeout=0):
    try:
        my_games_lobby_tabbar = find_element_or_none(
            my_games_page.child_window(class_name_re="MyGamesLobbyPageTabBar_QMLTYPE_*"), timeout=timeout)
        tabs = my_games_lobby_tabbar.children()
        return tabs if len(tabs) != 0 else None
    except Exception:
        return None


def my_games_results_form(my_games_page, timeout=0):
    return find_element_or_none(my_games_page.child_window(class_name_re="MyGamesMyResultsForm_QMLTYPE_*"), 
                                timeout=timeout)


def my_games_tournaments_form(my_games_page, timeout=0):
    return find_element_or_none(my_games_page.child_window(class_name_re="MyGamesTournamentsForm_QMLTYPE_*"), 
                                timeout=timeout)


def my_games_cash_hands_form(my_games_page, timeout=0):
    return find_element_or_none(my_games_page.child_window(class_name_re="MyGamesCashHandsForm_QMLTYPE_*"), 
                                timeout=timeout)


def my_games_my_statistics_form(my_games_page, timeout=0):
    return find_element_or_none(my_games_page.child_window(class_name_re="MyGamesMyStatisticsForm_QMLTYPE_*"), 
                                timeout=timeout)


def my_games_my_casino_form(my_games_page, timeout=0):
    return find_element_or_none(my_games_page.child_window(class_name_re="MyGamesCasinoForm_QMLTYPE_*"),
                                timeout=timeout)
