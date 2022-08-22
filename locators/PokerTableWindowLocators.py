import pywinauto
from .locators_utils import find_element_or_none


def buy_in_form(poker_table_win, timeout=0):
    return find_element_or_none(poker_table_win.child_window(class_name_re="BuyInForm_QMLTYPE_*"), timeout=timeout)
