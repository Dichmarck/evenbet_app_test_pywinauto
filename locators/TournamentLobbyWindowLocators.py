import pywinauto
from .locators_utils import find_element_or_none


def tabs(app, timeout=0):
    tabbar = find_element_or_none(app.child_window(class_name_re="PTabBarHeader_*"), timeout=timeout)
    try:
        tabs = tabbar.children()
        return tabs if len(tabs) != 0 else None
    except Exception:
        return None


def status_pane(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="TournamentStatusTab_*"), timeout=timeout)


def prize_pane(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="TournamentPrizeTab*"), timeout=timeout)


def satellites_pane(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="TournamentSatellitesTab*"), timeout=timeout)


def cashier_button(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="PButtonSecondary_*"), timeout=timeout)


def swipe_view(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="SwipeView_QMLTYPE_*"), timeout=timeout)
