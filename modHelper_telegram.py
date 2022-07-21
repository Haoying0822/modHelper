from certifi import contents
import telebot

from telegram import ParseMode
from Messages_v2 import *
from MenuList import *
from Option import *
from pairEngine import *
from ModuleInfo import *

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
    
    if call.data == "module_info":
        msg = bot.send_message(user_id, "Please send your module code \nPlease type in CAPITAL letter:)")
        bot.register_next_step_handler(msg, module_info_handler)

    if call.data == "module_group":
        bot.send_message(user_id, "You may find your module's telegram group on the TeleNUS website: https://telenus.nusmods.com/")
        bot.send_message(user_id, m_play_again)

    if call.data == "module_mate":
        msg = bot.send_message(user_id, "Please send your module code \nPlease type in CAPITAL letter:)")
        bot.register_next_step_handler(msg, module_mate_handler)
       
    if call.data == "study_buddy":
        menu = faculty_menu()
        msg = bot.send_message(user_id, "Please select your faculty", reply_markup = menu)
        bot.register_next_step_handler(msg, module_mate_handler)

@bot.message_handler(func = lambda message: message.text in option_dict.keys())
def general_case(message):
    user_id = message.chat.id
    bot.send_message(user_id, m_invalid_command, reply_markup = start_menu())

def module_info_handler(message):
    module_code = message.text
    if module_code in faculty:
        msg = bot.send_message(message.chat.id, "Sorry, the input module code is invalid. Please check and try again.\n\nRemember that you need to type in capital letter:)")
        bot.register_next_step_handler(msg, module_info_handler)
    elif module_code in option_dict.keys():
        module_info = search_modinfo(module_code)
        bot.send_message(message.chat.id, module_info, parse_mode = ParseMode.HTML)
        bot.send_message(message.chat.id, m_play_again)
    else:
        msg = bot.send_message(message.chat.id, "Sorry, the input module code is invalid. Please check and try again.\n\nRemember that you need to type in capital letter:)")
        bot.register_next_step_handler(msg, module_info_handler)

def module_mate_handler(message):
    user_id = message.chat.id
    opt = message.text
    user_to_id = None

    if bot_users[user_id]:
        bot.send_message(user_id, m_clash)
        return
    
    if user_id in communications:
        bot.send_message(user_id, m_in_a_dialog)
        return
    
    if message.chat.username == None:
        bot.send_message(user_id, m_is_not_user_name)
        return

    add_users(user_id, message.chat.username, opt)

    if not find_user(opt):
        bot.send_message(user_id, m_is_not_free_users, reply_markup = types.ReplyKeyboardRemove())
        print("not enough user")
        return
    
    if bot_users[user_id]["state"] == 0:
        bot.send_message(user_id, m_is_not_free_users, reply_markup = types.ReplyKeyboardRemove())
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
        bot.send_message(user_id, m_is_not_free_users, reply_markup = types.ReplyKeyboardRemove())
        return
    
    add_communications(user_id, user_to_id)

    keyboard = generate_markup()

    bot.send_message(user_id, m_is_connect, reply_markup=keyboard)
    bot.send_message(user_to_id, m_is_connect, reply_markup=keyboard)


def connect_user(user_id):
    if user_id in communications:
        return True
    else:
        bot.send_message(user_id, m_invalid_command, reply_markup = start_menu())
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
        bot.send_message(user_id, m_play_again)
        bot.send_message(user_to_id, m_play_again)

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

    if bot_users[user_id]["state"] == 0:
        out_users[option_dict[bot_users[user_id]["Option"]]] -= 1
    if bot_users[user_id]["state"] == 1:
        in_users[option_dict[bot_users[user_id]["Option"]]] -= 1

    delete_user_from_db(user_id)

    bot.send_message(user_id, m_good_bye)
    menu = start_menu()
    bot.send_message(user_id, m_play_again)

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
            and message.text not in option_dict.keys()
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
