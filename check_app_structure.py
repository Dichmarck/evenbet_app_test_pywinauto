import pywinauto
from pywinauto.controls.uia_controls import ButtonWrapper

from constants import MAIN_WINDOW_CLASS_NAME_RE, APP_PATH




application = pywinauto.Application(backend='uia').start(APP_PATH).\
                        connect(class_name_re=MAIN_WINDOW_CLASS_NAME_RE, timeout=30)
app_win = application.window(class_name_re=MAIN_WINDOW_CLASS_NAME_RE)

login_btn = app_win.child_window(class_name_re="PLoginButton_QMLTYPE_*")

