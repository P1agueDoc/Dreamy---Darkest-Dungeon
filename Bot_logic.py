import telebot
from Level_gen import *
map1 = Map(16, 16)
bot = telebot.TeleBot("")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('test level grid', 'Option 2', 'Option 3')
    bot.send_message(message.chat.id, "Howdy, how are you doing :fog:?", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def button_handler(message):
    map_print = map1.map_gen()
    if message.text == 'test level grid':
        bot.reply_to(message, map_print)
    elif message.text == 'Option 2':
        bot.reply_to(message, "You chose Option 2!")
    elif message.text == 'Option 3':
        bot.reply_to(message, "You chose Option 3!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()