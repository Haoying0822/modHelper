import telebot
from telebot import types

from Messages_v1 import *

TOKEN = "5458457619:AAFzvBHIMTRzze_G44Ktx6lvxt77vdYAozw"
bot = telebot.TeleBot(TOKEN)

def start_menu():
    callback1 = types.InlineKeyboardButton(
        text = "Find Module Mate", callback_data = "module_mate"
    )

    callback2 = types.InlineKeyboardButton(
        text = "Find Study Buddy", callback_data = "study_buddy"
    )

    callback3 = types.InlineKeyboardButton(
        text = "Start a chat with user ID", callback_data = "resume_chat"
    )

    menu = types.InlineKeyboardMarkup()
    menu.add(callback1)
    menu.add(callback2)
    menu.add(callback3)

    return menu

@bot.message_handler(commands = ["start"])
def echo(message):
    message.chat.type = "private"
    user_id = message.chat.id

    menu = start_menu()

    bot.send_message(user_id, m_start, reply_markup=menu)

@bot.callback_query_handler(func=lambda call: True)
def echo(call):
    if call.data == "module_mate":
        user_id = call.message.chat.id
        bot.send_message(user_id, "Please send your module code")

    if call.data == "study_buddy":
        user_id = call.message.chat.id
        bot.send_message(user_id, "Please select your faculty")
    
    if call.data == "resume_chat":
        user_id = call.message.chat.id
        bot.send_message(user_id, "Please send the user ID") 

if __name__ == "__main__":
    #recovery_data()
    bot.stop_polling()
    bot.polling(none_stop=True)
