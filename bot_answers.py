import collections
import datetime
from dialog import *
from bot_handler import BotHandler
from constants import *
from photo import new_photo

WHtC_bot = BotHandler(token)
now = datetime.datetime.now()


# class Dialog():
#     new_offset = None
#     while True:
#         WHtC_bot.get_updates(new_offset)
#
#         last_update = WHtC_bot.get_last_update()
#         if not last_update:
#             continue
#         last_update_id = last_update['update_id']
#         last_chat_text = last_update['message']['text']
#         last_chat_id = last_update['message']['chat']['id']
#         last_chat_name = last_update['message']['chat']['first_name']
#
#         if last_chat_text.lower() in greetings:
#
#
#
#
#         new_offset = last_update_id + 1


def user_greeting():
    today = now.day
    hour = now.hour

    if today == now.day and 6 <= hour < 12:
        WHtC_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
        today += 1

    elif today == now.day and 12 <= hour < 17:
        WHtC_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
        today += 1

    elif today == now.day and 17 <= hour < 23:
        WHtC_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
        today += 11

def photo_from_computer():

    new_photo()
    WHtC_bot.send_photo(last_chat_id, photo=open('new_photo.jpg', 'rb'))








def ask_yes_or_no(question):
    """Спросить вопрос и дождаться ответа, содержащего «да» или «нет».

    Возвращает:
        bool
    """
    answer = yield question
    while not ("да" in answer.text.lower() or "нет" in answer.text.lower()):
        answer = yield "Так да или нет?"
    return "да" in answer.text.lower()

# def turn_off_computer():
#
#
#
