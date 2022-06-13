from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("Token to be inserted here",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"""Hello, welcome to modHelper. This is a bot aiming to help NUS students find module mates and study buddies.
                To protect your privacy, the bot will facilitate an anonymous chat between users based on your specified preferences.
                You may exchange usernames once you both find each other a satisfactory match.
                Please write\
		/help to see the commands available.""")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/module_mate - input "/module_mate" with module code to match with others in the same mod! eg: /module_mate GE1000
	/study_buddy - input "/study_buddy" with your faculty to match! eg: /study_buddy CHS
	""")

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)

def test_printer(update: Update, context: CallbackContext):
        update.message.reply_text(
                "You have sent me {}".format(update.message.text.split()[1]))

        
def module_mate_func(update: Update, context: CallbackContext):
        #add user to database and anonymous matching here
        update.message.reply_text(
                "Sure {}! Others looking for module/project mates in {} will contact you shortly. Please look out for notif as the matching might take a while."
                .format(update.message.from_user.first_name, update.message.text.split()[1]))

def study_buddy_func(update: Update, context: CallbackContext):
        #add user to database and anonymous matching here
        update.message.reply_text(
                "Sure {}! Others looking for study buddy in {} will contact you shortly. Please look out for notif as the matching might take a while."
                .format(update.message.from_user.first_name, update.message.text.split()[1]))



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.dispatcher.add_handler(CommandHandler("test", test_printer))
updater.dispatcher.add_handler(CommandHandler('module_mate', module_mate_func))
updater.dispatcher.add_handler(CommandHandler('study_buddy', study_buddy_func))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()


