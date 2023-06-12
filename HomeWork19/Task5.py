def bot_init(self, name):
    self.name = name


def bot_send_message(self, message):
    print(message)


def bot_say_name(self):
    print(self.name)


Bot = type('Bot', (), {
    '__init__': bot_init,
    'send_message': bot_send_message,
    'say_name': bot_say_name
})


def telegram_bot_init(self, name, url=None, chat_id=None):
    Bot.__init__(self, name)
    self.url = url
    self.chat_id = chat_id


def telegram_bot_set_url(self, url):
    self.url = url


def telegram_bot_set_chat_id(self, chat_id):
    self.chat_id = chat_id


def telegram_bot_send_message(self, message):
    print(f"The message '{message}' is sent to the chat located at {self.url} with id {self.chat_id}")


TelegramBot = type('TelegramBot', (Bot,), {
    '__init__': telegram_bot_init,
    'set_url': telegram_bot_set_url,
    'set_chat_id': telegram_bot_set_chat_id,
    'send_message': telegram_bot_send_message
})
