import pywinauto
from .common_utils import find_element_or_none


def cashier_window(timeout=0):
    try:
        cashier_app = pywinauto.Application(backend='uia').connect(class_name_re="CashierDesktopWindow_QMLTYPE_*",
                                                                   timeout=timeout)
        return find_element_or_none(cashier_app.window(class_name_re="CashierDesktopWindow_QMLTYPE_*"),
                                    timeout=timeout)
    except Exception:
        return None


def poker_table_window(timeout=0):
    try:
        poker_table_window = pywinauto.Application(backend='uia'). \
            connect(class_name_re="TableDesktopWindow_QMLTYPE_*", timeout=timeout). \
            window(class_name_re="TableDesktopWindow_QMLTYPE_*")
        return poker_table_window
    except Exception:
        return None


def my_tournaments_window(timeout=0):
    try:
        my_tours_app = pywinauto.Application(backend='uia').connect(class_name_re="DesktopDialog_QMLTYPE_*",
                                                                    timeout=timeout)
        return find_element_or_none(my_tours_app.window(class_name_re="DesktopDialog_QMLTYPE_*").
                                    child_window(class_name_re="MyTournamentsForm_QMLTYPE_*"), timeout=timeout)
    except Exception:
        return None


def tournament_lobby_window(timeout=0):
    try:
        tournament_lobby_app = pywinauto.Application(backend='uia'). \
            connect(class_name_re="TournamentLobbyDesktopWindow*", timeout=timeout). \
            window(class_name_re="TournamentLobbyDesktopWindow*")
        return tournament_lobby_app
    except Exception:
        return None
