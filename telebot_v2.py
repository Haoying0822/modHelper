import telebot
from telebot import types

from Messages_v1 import *
from MenuList import *

TOKEN = "5458457619:AAFzvBHIMTRzze_G44Ktx6lvxt77vdYAozw"
bot = telebot.TeleBot(TOKEN)

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
        menu = faculty_menu()
        bot.send_message(user_id, "Please select your faculty", reply_markup = menu)
    
    if call.data == "resume_chat":
        user_id = call.message.chat.id
        bot.send_message(user_id, "Please send the user ID") 
    
    else:
        pass

if __name__ == "__main__":
    #recovery_data()
    bot.stop_polling()
    bot.polling(none_stop=True)
