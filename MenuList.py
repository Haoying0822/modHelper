from telebot import types

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

def faculty_menu():
    Biz = types.InlineKeyboardButton(
        text = "Business School", callback_data= "biz"
    )

    FASS = types.InlineKeyboardButton(
        text = "College of Humanities and Sciences - FASS", callback_data = "fass"
    )

    Fos = types.InlineKeyboardButton(
        text = "College of Humanities and Sciences - FoS", callback_data = "fos"
    )

    Soc = types.InlineKeyboardButton(
        text = "School of Computing", callback_data = "soc"
    )

    Fod = types.InlineKeyboardButton(
        text = "Faculty of Dentistry", callback_data = "fod"
    )

    CDE = types.InlineKeyboardButton(
        text = "College of Design and Engineering", callback_data = "cde"
    )

    Med = types.InlineKeyboardButton(
        text = "Yong Loo Lin School of Medicine", callback_data = "med"
    )

    Fol = types.InlineKeyboardButton(
        text = "Faculty of Law", callback_data = "fol"
    )

    Music = types.InlineKeyboardButton(
        text = "Yong Siew Toh Conservatory of Music", callback_data = "music"
    )

    Nur = types.InlineKeyboardButton(
        text = "Alice Lee Centre for Nursing Studies", callback_data = "nur"
    )

    menu = types.InlineKeyboardMarkup()
    menu.add(Nur)
    menu.add(Biz)
    menu.add(CDE)
    menu.add(FASS)
    menu.add(Fos)
    menu.add(Fod)
    menu.add(Fol)
    menu.add(Soc)
    menu.add(Med)
    menu.add(Music)

    return menu