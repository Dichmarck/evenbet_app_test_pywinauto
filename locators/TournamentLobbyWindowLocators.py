import pywinauto
from .locators_utils import find_element_or_none


def tabs(tour_win, timeout=0):
    tabbar = find_element_or_none(tour_win.child_window(class_name_re="PTabBarHeader_*"), timeout=timeout)
    try:
        tabs = tabbar.children()
        return tabs if len(tabs) != 0 else None
    except Exception:
        return None


def status_pane(tour_win, timeout=0):
    return find_element_or_none(tour_win.child_window(class_name_re="TournamentStatusTab_*"), timeout=timeout)


def prize_pane(tour_win, timeout=0):
    return find_element_or_none(tour_win.child_window(class_name_re="TournamentPrizeTab*"), timeout=timeout)


def satellites_pane(tour_win, timeout=0):
    return find_element_or_none(tour_win.child_window(class_name_re="TournamentSatellitesTab*"), timeout=timeout)


def cashier_button(tour_win, timeout=0):
    return find_element_or_none(tour_win.child_window(class_name_re="PButtonSecondary_*"), timeout=timeout)


def swipe_view(tour_win, timeout=0):
    return find_element_or_none(tour_win.child_window(class_name_re="SwipeView_QMLTYPE_*"), timeout=timeout)
