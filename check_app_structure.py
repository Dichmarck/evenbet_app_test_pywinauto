import time
import pyautogui
import pywinauto
from evenbet_app_test_pywinauto.constants import *

def get_rect_center(rect):
    h_center = int((rect.left + rect.right)/2)
    v_center = int((rect.top + rect.bottom) / 2)
    return (h_center, v_center)

def is_inside_window(elem_rect, win_rect):
    if elem_rect.left < win_rect.left:
        return False
    if elem_rect.top < win_rect.top:
        return False
    if elem_rect.right > win_rect.right:
        return False
    if elem_rect.bottom > win_rect.bottom:
        return False
    return True



application = pywinauto.Application(backend='uia').start(APP_PATH).connect(title_re=APP_TITLE_RE, timeout=30)
app_win = application.window(title_re=APP_TITLE_RE)


tables_tabitem = app_win.child_window(class_name="PokerLobbyCashTablesView_QMLTYPE_505")
tables_tabitem_rect = tables_tabitem.rectangle()
#tables_tabitem.print_ctrl_ids()
buttons = tables_tabitem.descendants(control_type="Button")
#pyautogui.moveTo(*get_center(scrollbar_v.rectangle()))


clicked_buttons = []
while True:
    loaded_buttons = tables_tabitem.descendants(control_type="Button")
    new_visible_tables_buttons = []
    for button in loaded_buttons:
        if button not in clicked_buttons and "PButtonPrimary_QMLTYPE_" in button.class_name():
            button_rect = button.rectangle()
            if not is_inside_window(button_rect, tables_tabitem_rect):
                continue
            new_visible_tables_buttons.append(button)

    print(new_visible_tables_buttons)
    for button in new_visible_tables_buttons:
        pyautogui.moveTo(*get_rect_center(button.rectangle()))
        clicked_buttons.append(button)



    tables_tabitem.wheel_mouse_input(wheel_dist=-1)






#ables_buttons = []
#or i in range(3000):
#



