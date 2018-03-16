from bot_handler import BotHandler
from constants import *
from bot_answers import *

WHtC_bot = BotHandler(token)
new_offset = None
def bot_dialog():
    while True:
        WHtC_bot.get_updates(new_offset)
        last_update = WHtC_bot.get_last_update()
        if not last_update:
            continue

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings:
            user_greeting()

        if last_chat_text.lower() in photography:
            new_photo()

        new_offset = last_update_id + 1

