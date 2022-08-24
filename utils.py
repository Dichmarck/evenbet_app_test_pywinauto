import sys
import time

import _ctypes
import pyautogui
import pywinauto


def return_func_name():
    return sys._getframe(1).f_code.co_name


def mouse_input(element, duration=0):
    """Move mouse to center of element.
        :Args:
            - element - instance of classes WindowSpecification or UIAWrapper.
            - duration - the time it takes for the cursor to move.
        """
    rect = element.rectangle()
    center_h = int((rect.right + rect.left) / 2)
    center_v = int((rect.bottom + rect.top) / 2)
    pyautogui.moveTo(center_h, center_v, duration)


def find_elem_by_text(elements, text):
    """Select one element from list of elements by window_text().
        :Args:
            - element - list of instances of classes WindowSpecification or UIAWrapper.
            - text - text, that will be compared with window_text() of element.
    """
    for elem in elements:
        if elem.window_text().strip().lower() == text.strip().lower():
            return elem
    return None


def timer(label=""):
    """Decorator that prints function runtime with given label.
        :Args:
            - label - text, that will be printed in terminal before time.
    """
    def timer_decorator(func):
        def timer_wrapper(*args, **kwargs):
            time_start = time.time()
            result = func(*args, **kwargs)
            print(label + ": ", time.time() - time_start)
            return result
        return timer_wrapper
    return timer_decorator


def get_rect_center(rect):
    """Returns the X,Y coordinates of center of given rectangle.
        :Args:
            - rect - instance of class Rectangle.
    """
    h_center = int((rect.left + rect.right)/2)
    v_center = int((rect.top + rect.bottom) / 2)
    return (h_center, v_center)


def ensure_element_disappears(element, timeout=0):
    """Returns True if element disappears in given time else False.
        :Args:
            - element - instance of classes WindowSpecification or UIAWrapper.
            - timeout - time range.
    """
    time_start = time.time()
    while time.time() - time_start <= timeout:
        try:
            element.rectangle()
        except (_ctypes.COMError, pywinauto.findwindows.ElementNotFoundError):
            return True
    return False


def close_window_by_alt_f4(window):
    window.type_keys("%{F4}")


def close_dialog_by_esc(dialog):
    dialog.type_keys("{VK_ESCAPE}")
