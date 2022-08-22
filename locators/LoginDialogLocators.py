import pywinauto
from .locators_utils import find_element_or_none


def username_field(app, timeout=0):
    return find_element_or_none(app.Edit1, timeout=timeout)


def password_field(app, timeout=0):
    return find_element_or_none(app.Edit2, timeout=timeout)


def login_button(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                child_window(class_name_re="PButtonPrimary_QMLTYPE_*"), timeout=timeout)


def signup_button(app, timeout=0):
    return find_element_or_none(app.child_window(class_name_re="LoginPanel_QMLTYPE_*").
                                child_window(class_name_re="PButtonQuaternary_QMLTYPE_*"), timeout=timeout)
