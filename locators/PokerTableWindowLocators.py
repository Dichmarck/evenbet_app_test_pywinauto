import pywinauto
from .common_utils import find_element_or_none


def buy_in_form(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="BuyInForm_QMLTYPE_*"), timeout=timeout)
