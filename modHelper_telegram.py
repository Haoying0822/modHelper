from certifi import contents
import telebot

from Messages_v2 import *
from MenuList import *
from Option import *
from pairEngine import *

TOKEN = "YOUR TOKEN HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start"])
def echo(message):
    message.chat.type = "private"
    user_id = message.chat.id

    menu = start_menu()

    bot.send_message(user_id, m_start, reply_markup=menu)


@bot.callback_query_handler(func = lambda call: True)
def echo(call):
    user_id = call.message.chat.id

    if user_id in communications:
        bot.send_message(user_id, m_in_a_dialog)
        return
    
    if call.data == "module_mate":
        bot.send_message(user_id, "Please send your module code")

    if call.data == "study_buddy":
        menu = faculty_menu()
        bot.send_message(user_id, "Please select your faculty", reply_markup = menu)


@bot.message_handler(func = lambda message: message.text in option)
def echo(message):
    user_id = message.chat.id
    opt = message.text
    user_to_id = None

    add_users(message.chat, opt)


    if not find_user(opt):
        bot.send_message(user_id, m_is_not_free_users)
        print("not enough user")
        return
    
    if bot_users[user_id]["state"] == 0:
        bot.send_message(user_id, m_is_not_free_users)
        print("matching failed")
        return    

    if find_user(opt):
        #successfully find
        print("found")
        for user in bot_users:
            if user["Option"] == opt:
                if user["state"] == 0:
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
        bot.send_message(user_id, m_invalid_command)
        bot.send_message(user_id, m_start_again, reply_markup = start_menu())
        return False


@bot.message_handler(
    func=lambda call: call.text == like_str or call.text == dislike_str
)
def echo(message):
    user_id = message.chat.id

    if user_id not in communications:
        bot.send_message(user_id, m_failed, reply_markup = types.ReplyKeyboardRemove())
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
        bot.send_message(user_id, m_play_again, reply_markup = menu)
        bot.send_message(user_to_id, m_play_again, reply_markup = menu)

@bot.message_handler(commands=["stop"])
def echo(message):
    menu = types.ReplyKeyboardRemove()
    user_id = message.chat.id

    if message.chat.id in communications:

        bot.send_message(
            communications[user_id]["UserTo"], m_disconnect_user, reply_markup = menu
        )

        tmp_id = communications[user_id]["UserTo"]
        delete_info(tmp_id)

    delete_user_from_db(user_id)

    bot.send_message(user_id, m_good_bye)
    menu = start_menu()
    bot.send_message(user_id, m_play_again, reply_markup = menu)

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
            and message.text not in option
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


if __name__ == "__main__":
    recovery_data()
    bot.stop_polling()
    bot.polling(none_stop=True)
