import pywinauto
from .locators_utils import find_element_or_none


def chat_text_field(chat_dlg, timeout=0):
    return find_element_or_none(chat_dlg.child_window(class_name_re="ChatTextField_QMLTYPE_*"), timeout=timeout)


def chat_messages_str_list(chat_dlg, timeout=0):
    try:
        chat_messages_string_list = []
        chat = find_element_or_none(chat_dlg.child_window(class_name_re="LobbyChat_QMLTYPE_*"), timeout=timeout)
        chat_messages = chat.descendants(control_type="Edit")
        for message in chat_messages:
            chat_messages_string_list.append(message.window_text())
        return chat_messages_string_list if len(chat_messages_string_list) != 0 else None
    except Exception:
        return None
