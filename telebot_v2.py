from certifi import contents
import telebot
from telebot import types

from Messages_v1 import *
from MenuList import *
from ModuleList import *
from pairEngine import *

TOKEN = "YOUR TOKEN HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start"])
def echo(message):
    message.chat.type = "private"
    user_id = message.chat.id

    menu = start_menu()

    bot.send_message(user_id, m_start, reply_markup=menu)


#Match module mate

@bot.callback_query_handler(func = lambda call: call.data == "module_mate")
def echo(call):
    user_id = call.message.chat.id
    bot.send_message(user_id, "Please send your module code")

@bot.message_handler(func = lambda message: message.text in moduleList)
def echo(message):
    user_id = message.chat.id
    mod = message.text
    if find_module_user(mod):
        #successfully find
        bot.send_message(user_id, "SUCCESSFULLY MATCHED")
    else:
        add_module_users(message.chat, mod)
        bot.send_message(user_id, m_is_not_free_users)


#Match study buddy


@bot.callback_query_handler(func = lambda call: True)
def echo(call):
    user_id = call.message.chat.id

    if call.data == "study_buddy":
        menu = faculty_menu()
        bot.send_message(user_id, "Please select your faculty", reply_markup = menu)
    
    #if call.data == "resume_chat":
        #bot.send_message(user_id, "Please send the user ID")

@bot.message_handler(func = lambda message: message.text in facultyList)
def echo(message):
    user_id = message.chat.id
    bot.send_message(user_id, "YAY the bot works!!!")

if __name__ == "__main__":
    #recovery_data()
    bot.stop_polling()
    bot.polling(none_stop=True)
