import  requests
from time import sleep

url = "https://api.telegram.org/bot560891526:AAE4CUMq1tg33BVQ6ChghHvWEncs56R9nug/"

def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()



    #
    #
    # -*- coding: utf-8 -*-
    import config
    import telebot

    bot = telebot.TeleBot(config.token)


    @bot.message_handler(content_types=["text"])
    def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
        bot.send_message(message.chat.id, message.text)


    if __name__ == '__main__':
        bot.polling(none_stop=True)