from evenbet_app_test_pywinauto.utils import timer
from evenbet_app_test_pywinauto.pages.BasePage import BasePage
from evenbet_app_test_pywinauto.pages import locators


class ChatDialogPage(BasePage):

    @timer("Chat text field")
    def find_chat_text_field(self):
        text_field = locators.ChatDialogPageLocators.chat_text_field(self.app)
        return text_field

    @timer("Chat message str list")
    def find_chat_messages_str_list(self):
        chat_messages_str_list = locators.ChatDialogPageLocators.chat_messages_str_list(self.app)
        return chat_messages_str_list

    @timer("Send message in chat")
    def send_message_in_chat(self, text_field, message):
        text_field.click_input()
        text_field.type_keys(message)
        text_field.type_keys('{ENTER}')
        return
