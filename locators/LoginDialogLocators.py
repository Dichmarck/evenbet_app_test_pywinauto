import pywinauto
from .locators_utils import find_element_or_none


def username_field(login_win, timeout=0):
    return find_element_or_none(login_win.Edit1, timeout=timeout)


def password_field(login_win, timeout=0):
    return find_element_or_none(login_win.Edit2, timeout=timeout)


def login_button(login_win, timeout=0):
    return find_element_or_none(login_win.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                child_window(class_name_re="PButtonPrimary_QMLTYPE_*"), timeout=timeout)


def signup_button(login_win, timeout=0):
    return find_element_or_none(login_win.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                child_window(class_name_re="PButtonQuaternary_QMLTYPE_*"), timeout=timeout)

def close_login_dlg_button(login_win, timeout=0):
    return find_element_or_none(login_win.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                child_window(class_name_re="PButtonWithIcon_QMLTYPE_*"), timeout=timeout)
