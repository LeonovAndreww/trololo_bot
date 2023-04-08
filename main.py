import telebot
from config import *
from random import randint

bot = telebot.TeleBot('5009176955:AAGDFHzueY32XbNs0dffKDF8z539jM7C0Ek')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    random_number = randint(0, 100)
    if 'английский' in message.text.lower():
        img = open('data/cock.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    elif '😭' in message.text or '😢' in message.text or '😞' in message.text:
        img = open('data/cry1.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    elif 'днр' in message.text.lower() or 'лнр' in message.text.lower() \
            or 'украина' in message.text.lower() or 'донбасс' in message.text.lower():
        img = open('data/don.jpg', 'rb')
        bot.send_photo(message.chat.id, img, caption='#SaveDonbassPeople', reply_to_message_id=message.message_id)
    elif len(message.text) > 300:
        anim = open('data/dr1.gif', 'rb')
        bot.send_animation(message.chat.id, anim, reply_to_message_id=message.message_id)
    elif 'сухарь' in message.text.lower():
        img = open('data/dry1.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    elif 'спокойной ночи' in message.text.lower():
        img = open('data/goodnight.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
    elif 'математика' in message.text.lower() or 'алгебра' in message.text.lower() \
            or 'геометрия' in message.text.lower():
        img = open('data/math.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    elif 'доброе утро' in message.text.lower():
        img = open('data/morning1.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
    elif 'ццц' in message.text.lower():
        img = open('data/shutup.jpg', 'rb')
        bot.send_photo(message.chat.id, img, caption='Без негатива', reply_to_message_id=message.message_id)

    if random_number == 0:
        anim = open('data/timurgif1.gif', 'rb')
        bot.send_animation(message.chat.id, anim, reply_to_message_id=message.message_id)
    elif random_number == 1:
        anim = open('data/timurgif2.gif', 'rb')
        bot.send_animation(message.chat.id, anim, reply_to_message_id=message.message_id)
    elif random_number == 2:
        anim = open('data/okniggaand.gif', 'rb')
        bot.send_animation(message.chat.id, anim, reply_to_message_id=message.message_id)
    elif random_number == 3:
        anim = open('data/literallyme.gif', 'rb')
        bot.send_animation(message.chat.id, anim, reply_to_message_id=message.message_id)
    elif random_number == 4:
        bot.send_message(message.chat.id, 'ццц', reply_to_message_id=message.message_id)
    elif random_number == 5:
        bot.send_message(message.chat.id, 'хуйхуй соевое масло', reply_to_message_id=message.message_id)
    elif random_number == 6:
        bot.send_message(message.chat.id, 'ладно', reply_to_message_id=message.message_id)
    elif random_number == 7:
        bot.send_message(message.chat.id, f'"{message.text}" - само поняло, что высрало?', reply_to_message_id=message.message_id)


bot.polling(none_stop=True, interval=0)
