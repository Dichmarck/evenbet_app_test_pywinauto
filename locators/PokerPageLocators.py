import time
import pywinauto
from .locators_utils import find_element_or_none


def poker_lobby_tabs(poker_page, timeout=0):
    try:
        poker_lobby_main_view_tabbar = find_element_or_none(
            poker_page.child_window(class_name_re="PokerLobbyMainViewTabBar_QMLTYPE_*"), timeout=timeout)
        tabs = poker_lobby_main_view_tabbar.children()
        return tabs if len(tabs) != 0 else None
    except Exception:
        return None


def poker_lobby_cash_tables_view(poker_page, timeout=0):
    return find_element_or_none(poker_page.child_window(class_name_re="PokerLobbyCashTablesView_QMLTYPE_*"), timeout=timeout)


def poker_lobby_tournaments_view(poker_page, timeout=0):
    return find_element_or_none(poker_page.child_window(class_name_re="PokerLobbyTournamentsView_QMLTYPE_*"), timeout=timeout)


def poker_lobby_spins_view(poker_page, timeout=0):
    return find_element_or_none(poker_page.child_window(class_name_re="PokerLobbySpinsView_QMLTYPE_*"), timeout=timeout)


def tournament_registration_button(poker_page, timeout=0):
    return find_element_or_none(poker_page.child_window(class_name_re="PokerLobbyTournamentDetailsView_*").
                                child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)


def register_button_on_tournament_registration_form(poker_page, timeout=0):
    return find_element_or_none(poker_page.child_window(class_name_re="TournamentRegistrationForm_*").
                                child_window(class_name_re="PButtonPrimary_*"), timeout=timeout)


def tournament_lobby_button(poker_page, timeout=0):
    return find_element_or_none(poker_page.child_window(class_name_re="PokerLobbyTournamentDetailsView_*").
                                child_window(class_name_re="PButtonSecondary*"), timeout=timeout)


def poker_tables(poker_page, timeout=0):
    time_start = time.time()
    while time.time() - time_start <= timeout:
        try:
            list_items = poker_page.descendants(control_type="ListItem")
            tables = []
            for item in list_items:
                if "TableViewItemDelegate_" in item.class_name():
                    tables.append(item)
            if len(tables) != 0:
                return tables
        except Exception:
            pass
    return None
