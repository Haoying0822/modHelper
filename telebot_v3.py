from certifi import contents
import telebot

from Messages_v1 import *
from MenuList import *
from ModuleList import *
from pairEngine import *

TOKEN = "TOKEN"
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
    user_to_id = None

    add_module_users(message.chat, mod)

    if not find_module_user(mod):
        print("no mod user")
        bot.send_message(user_id, m_is_not_free_users)
        return
    
    if module_users[user_id]["state"] == 0:
        bot.send_message(user_id, m_is_not_free_users)
        return

    if find_module_user(mod):
        #successfully find
        print("found")
        for user in module_users:
            if user["Module"] == mod:
                user_to_id = user["ID"]
                break
    
    if user_to_id is None:
        bot.send_message(user_id, m_is_not_free_users)
        return
    
    add_communications(user_id, user_to_id)

    keyboard = generate_markup()

    bot.send_message(user_id, m_is_connect, reply_markup=keyboard)
    bot.send_message(user_to_id, m_is_connect, reply_markup=keyboard)


def connect_user(user_id):
    if user_id in communications:
        return True
    else:
        bot.send_message(user_id, m_has_not_dialog)
        return False

@bot.message_handler(commands=["stop"])
def echo(message):
    menu = types.ReplyKeyboardRemove()
    user_id = message.chat.id

    if message.chat.id in communications:

        bot.send_message(
            communications[user_id]["UserTo"], m_disconnect_user, reply_markup=menu
        )

        tmp_id = communications[user_id]["UserTo"]
        delete_info(tmp_id)

    delete_Muser_from_db(user_id)

    bot.send_message(user_id, m_good_bye)

@bot.message_handler(
    func=lambda call: call.text == like_str or call.text == dislike_str
)
def echo(message):
    user_id = message.chat.id

    if user_id not in communications:
        bot.send_message(user_id, m_failed, reply_markup=types.ReplyKeyboardRemove())
        return

    user_to_id = communications[user_id]["UserTo"]

    flag = False

    if message.text == dislike_str:
        bot.send_message(
            user_id, m_dislike_user, reply_markup=types.ReplyKeyboardRemove()
        )
        bot.send_message(
            user_to_id, m_dislike_user_to, reply_markup=types.ReplyKeyboardRemove()
        )
        flag = True
    else:
        bot.send_message(user_id, m_like, reply_markup=types.ReplyKeyboardRemove())

        update_user_like(user_to_id)

        if communications[user_id]["like"]:
            bot.send_message(user_id, m_all_like(communications[user_id]["Username"]))
            bot.send_message(
                user_to_id, m_all_like(communications[user_to_id]["Username"])
            )
            flag = True

    if flag:
        delete_info(user_to_id)
        menu = start_menu()
        bot.send_message(user_id, m_play_again, reply_markup=menu)
        bot.send_message(user_to_id, m_play_again, reply_markup=menu)


@bot.message_handler(
    content_types=["text", "sticker", "photo"]
)
def echo(message):
    user_id = message.chat.id
    if message.content_type == "sticker":
        if not connect_user(user_id):
            return

        bot.send_sticker(communications[user_id]["UserTo"], message.sticker.file_id)
    elif message.content_type == "photo":
        if not connect_user(user_id):
            return

        file_id = None

        for item in message.photo:
            file_id = item.file_id

        bot.send_photo(
            communications[user_id]["UserTo"], file_id, caption=message.caption
        )
    elif message.content_type == "text":
        if (
            message.text != "/start"
            and message.text != "/stop"
            and message.text != dislike_str
            and message.text != like_str
            and message.text not in moduleList
            and message.text not in facultyList
        ):

            if not connect_user(user_id):
                return

            if message.reply_to_message is None:
                bot.send_message(communications[user_id]["UserTo"], message.text)
            elif message.from_user.id != message.reply_to_message.from_user.id:
                bot.send_message(
                    communications[user_id]["UserTo"],
                    message.text,
                    reply_to_message_id=message.reply_to_message.message_id - 1,
                )
            else:
                bot.send_message(user_id, m_send_some_messages)


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
