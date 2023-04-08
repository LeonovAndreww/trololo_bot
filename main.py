import telebot
from config import *
from random import randint

bot = telebot.TeleBot('5009176955:AAGDFHzueY32XbNs0dffKDF8z539jM7C0Ek')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    random_number = randint(0, 100)
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

    if random_number == 0:
        anim = open('data/timurgif1.gif', 'rb')
        bot.send_animation(message.chat.id, anim)
    elif random_number == 1:
        anim = open('data/timurgif2.gif', 'rb')
        bot.send_animation(message.chat.id, anim)
    elif random_number == 2:
        anim = open('data/okniggaand.gif', 'rb')
        bot.send_animation(message.chat.id, anim)
    elif random_number == 3:
        anim = open('data/literallyme.gif', 'rb')
        bot.send_animation(message.chat.id, anim)


bot.polling(none_stop=True, interval=0)
