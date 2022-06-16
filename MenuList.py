from telebot import types
from Messages_v2 import *

def start_menu():
    callback1 = types.InlineKeyboardButton(
        text = "Find Module Mate", callback_data = "module_mate"
    )

    callback2 = types.InlineKeyboardButton(
        text = "Find Study Buddy", callback_data = "study_buddy"
    )

    """
    callback3 = types.InlineKeyboardButton(
        text = "Start a chat with user ID", callback_data = "resume_chat"
    )
    """

    menu = types.InlineKeyboardMarkup()
    menu.add(callback1)
    menu.add(callback2)
    #menu.add(callback3)

    return menu

def faculty_menu():

    menu = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    menu.add("Alice Lee Centre for Nursing Studies")
    menu.add("Business School")
    menu.add("College of Design and Engineering")
    menu.add("College of Humanities and Sciences - FASS")
    menu.add("College of Humanities and Sciences - FoS")
    menu.add("Faculty of Dentistry")
    menu.add("Faculty of Law")
    menu.add("School of Computing")
    menu.add("Yong Loo Lin School of Medicine")
    menu.add("Yong Siew Toh Conservatory of Music")

    return menu

def generate_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    markup.add(like_str)
    markup.add(dislike_str)
    return markup
