import time
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class ChatDialogPage(BasePage):
    def find_chat_text_field(self):
        time_start = time.time()
        text_field = locators.ChatDialogPageLocators.chat_text_field(self.app)
        print("Chat dialog text field: ", time.time() - time_start)
        return text_field

    def find_chat_messages_str_list(self):
        time_start = time.time()
        chat_messages_str_list = locators.ChatDialogPageLocators.chat_messages_str_list(self.app)
        print("Chat messages (list of str): ", time.time() - time_start)
        return chat_messages_str_list

    def send_message_in_chat(self, text_field, message):
        time_start = time.time()
        text_field.click_input()
        text_field.type_keys(message)
        text_field.type_keys('{ENTER}')
        print("Send message in chat: ", time.time() - time_start)
        return
