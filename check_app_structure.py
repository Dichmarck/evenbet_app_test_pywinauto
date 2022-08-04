import pywinauto
from evenbet_app_test_pywinauto.constants import *

application = pywinauto.Application(backend='uia').start(APP_PATH).connect(title_re=APP_TITLE_RE, timeout=30)
app_win = application.window(title_re=APP_TITLE_RE)
app_win.print_ctrl_ids()
