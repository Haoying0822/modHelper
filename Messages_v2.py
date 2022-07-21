m_start = "Hello, welcome to modHelper. This is a bot aiming to help NUS students on anything and everything related to our modules. Here, you can find information, tele groups and mates based on module code. You can also match with study buddies based on your major. To start, press any of the buttons below. /help"

m_help = "Hi, Welcome to modHelper!\n\nThis is a bot dedicated to helping NUS students with all matters related to their modules. \n\nBefore you start, please check and ensure you have setup a username for your telegram account, as the bot cannot proceed without a username :)\n\nHere you can: \n\n<b>Search Module Info</b>\nSend us a module code and we will provide you with the module’s information from its credit, preclusion and description to workload distribution. All information are generated from NUSMods for max accuracy. Use this feature to gauge your expectations for the project component! \n\n<b>Find Module Group</b>\nWe will send you the link to TeleNUS, where you can find NUS-related Telegram groups. If you know groups that are not yet updated on TeleNUS, please also help them out! \n\n<b>Find Module Mate & Find Study Buddy</b>\nSend us the module code or select the faculty that you wish to find a module mate or study buddy for. We will immediately start searching for another user with the same selection for you. This process may need some time as other users might still be on the way!\nWe will send a message to notify you once a match is found. You can then start a chat with your match inside our bot. The chat is for you to exchange your expectations about the module’s project with each other, and is anonymous to protect you. Once both of you agree to match with each other, the bot will exchange the usernames for you and chat in the bot will be ended. Grab the username and start learning together! \nRemember, you can always stop searching or exiting from the chat. \n\nWe hope you have fun here!!\n\nPress /start to begin your journey🚀"
m_is_not_free_users = (
    "Got it! We have began searching for your perfect match! However, this might take a while...... \n\nTo keep searching, please check your notificatitons and come back later. \n\nTo exit this search, please press /stop. "
)

m_clash = "You are currently searching for a match. To start searching for a new match, please press /stop to stop the ongoing searching first."

m_is_connect = " 👀 A match is found! Now you are in the chat with your match, please start sending your messages!"

m_play_again = " 🧐 Looking for something else? Press /start to begin another session! /help"

m_is_not_user_name = " ☹️ Sorry, we are unable to facilitate your matches if you do not have a username. "

m_good_bye = " You have left the chat."

m_disconnect_user = "😨 Sorry, the connection was lost."

m_failed = "😦 An unknown failure has occured. Please retry again later. "

m_like = "✅ You have given permission to send your username to your match! Usernames will be revealed together once both parties give permission. "

m_dislike_user = "Chat has ended. "

m_dislike_user_to = (
    "Your match has left the chat. Better luck next time!"
)

m_send_some_messages = "🙈 Our bot could not forward the message. Please try something else. "

m_invalid_command = "😞 Sorry, we cannot recognise the content you have entered. \n\nWhat are you looking for? /help"

m_start_again = "To start a search, please select from below. /help"

m_in_a_dialog = "😦 You are currently in a match. To start another session, please terminate this session first. \nPress the button below to choose either exchange the username or directly exit."

dislike_str = "⛔ Exit"

like_str = "😊 Match and send username"

def m_all_like(x):
    return "Successfully matched!\n" + "The username of your buddy : @" + str(x) + "\nThe chat session is ended."
