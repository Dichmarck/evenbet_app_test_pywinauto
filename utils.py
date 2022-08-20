import sys
import time

import pyautogui


def return_func_name():
    return sys._getframe(1).f_code.co_name


def mouse_input(element, duration=0):
    """Move mouse to center of element."""
    rect = element.rectangle()
    center_h = int((rect.right + rect.left) / 2)
    center_v = int((rect.bottom + rect.top) / 2)
    pyautogui.moveTo(center_h, center_v, duration)


def find_elem_by_text(elements, text):
    """Select one element from list of elements by window_text()."""
    for elem in elements:
        if elem.window_text().strip().lower() == text.strip().lower():
            return elem
    return None


def timer(label=""):
    """Decorator that prints function runtime with given label."""
    def timer_decorator(func):
        def timer_wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            print(label + ": ", time.time() - time_start)
            return result
        return timer_wrapper
    return timer_decorator


def get_rect_center(rect):
    h_center = int((rect.left + rect.right)/2)
    v_center = int((rect.top + rect.bottom) / 2)
    return (h_center, v_center)
