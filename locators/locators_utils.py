import time
import pywinauto


def find_element_or_none(element_specification, timeout=0):
    """This function tries to find wrapper of given element specification.
        :Args:
            - element_specification: instance of class WindowSpecification or wrapper_object() of some element.
            - timeout: the time during which the search is going on.
    """
    time_start = time.time()
    while time.time() - time_start <= timeout:
        try:
            return element_specification.wrapper_object()
        except pywinauto.findwindows.ElementNotFoundError:
            pass
    return None
