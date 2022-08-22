from ..utils import timer
from ..pages.MainPage import MainPage
from ..locators import ChatDialogLocators


class ChatDialog(MainPage):

    @timer("Chat text field")
    def find_chat_text_field(self):
        text_field = ChatDialogLocators.chat_text_field(self.app)
        return text_field

    @timer("Chat message str list")
    def find_chat_messages_str_list(self):
        chat_messages_str_list = ChatDialogLocators.chat_messages_str_list(self.app)
        return chat_messages_str_list

    @timer("Send message in chat")
    def send_message_in_chat(self, text_field, message):
        text_field.click_input()
        text_field.type_keys(message)
        text_field.type_keys('{ENTER}')
        return
