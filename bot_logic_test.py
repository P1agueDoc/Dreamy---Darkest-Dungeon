import telebot
from Level_gen import *
map1 = Map(8, 8)
bot = telebot.TeleBot("7531771529:AAElMlwTxyzKC9ySVkQLCtGg91P8ZsuJ8xc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('action','item', 'preception' )
    bot.send_message(message.chat.id, "Howdy, how are you doing?", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def button_handler(message):
    map_print = map1.map_gen()
    if message.text == 'test level grid':
        bot.reply_to(message, map_print)
    elif message.text == 'action':
        action_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        action_keyboard.add('attack', 'defend', 'run', 'return')  # Example action buttons
        bot.reply_to(message, "Choose an action:", reply_markup=action_keyboard)
    elif message.text == 'item':
        bot.reply_to(message, "item use!")
    elif message.text == 'preception':
        bot.reply_to(message, "You look around the place")
    elif message.text == 'return':
        # Remove the current keyboard and send the main menu keyboard
        main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        main_keyboard.add('action', 'item', 'preception')
        bot.send_message(message.chat.id, "Main Menu:", reply_markup=main_keyboard)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()