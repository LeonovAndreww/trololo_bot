import telebot
from config import *

bot = telebot.TeleBot('5009176955:AAGDFHzueY32XbNs0dffKDF8z539jM7C0Ek')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # if message.from_user.id == misha_id:
    #     img = open('data/cock.jpg', 'rb')
    #     bot.send_message(message.chat.id, 'misha')
    #     bot.send_photo(message.chat.id, img)
    if 'английский' in message.text.lower():
        img = open('data/cock.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif '😭' in message.text or '😢' in message.text or '😞' in message.text:
        img = open('data/cry1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'днр' in message.text.lower() or 'лнр' in message.text.lower() \
            or 'украина' in message.text.lower() or 'донбасс' in message.text.lower():
        img = open('data/don.jpg', 'rb')
        bot.send_photo(message.chat.id, img, caption='#SaveDonbassPeople')
    elif len(message.text) > 300:
        anim = open('data/dr1.gif', 'rb')
        bot.send_animation(message.chat.id, anim)
    elif 'сухарь' in message.text.lower():
        img = open('data/dry1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'спокойной ночи' in message.text.lower():
        img = open('data/goodnight.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'математика' in message.text.lower() or 'алгебра' in message.text.lower() \
            or 'геометрия' in message.text.lower():
        img = open('data/math.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'доброе утро' in message.text.lower():
        img = open('data/morning1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'ццц' in message.text.lower():
        img = open('data/shutup.jpg', 'rb')
        bot.send_photo(message.chat.id, img, caption='Без негатива')


bot.polling(none_stop=True, interval=0)
