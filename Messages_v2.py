m_start = "Hello, welcome to modHelper. This is a bot aiming to help NUS students on anything and everything related to our modules. Here, you can find information, tele groups and mates based on module code. You can also match with study buddies based on your major. To start, press any of the buttons below. "

#m_chat_start = "💯  Welcome to modHelper's matching session! \n\n 🖥  We hope you find a satisfactory mate/buddy here! \n\n ⚠️  To protect your safety, all chats are to remain anonymous and usernames will only be revealed when both parties agree! \n\n ⏩  To start searching for a match, please press the button New Chat"

m_is_not_free_users = (
    "Got it! We have began searching for your perfect match! However, this might take a while...... \n\nTo keep searching, please check your notificatitons and come back later. \n\nTo exit this search, please type command /stop. "
)

m_clash = "You are currently in a search session. To start searching for a new match, please press /stop to stop the ongoing session first."

m_is_connect = " 👀 A match is found! Now you are in the chat with your match, please start sending your messages!"

m_play_again = " 🧐 Looking for something else? Press /start to begin another session! "

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

m_invalid_command = "😞 Sorry, we cannot recognise the content you have entered. \n\nWhat are you looking for?"

m_start_again = "To start a search, please select from below. "

m_in_a_dialog = "😦 You are currently in a match. To start another session, please terminate this session first. \nPress the button below to choose either exchange the username or directly exit."

dislike_str = "⛔ Exit"

like_str = "😊 Match and send username"

def m_all_like(x):
    return "Successfully matched!\n" + "The username of your buddy : @" + str(x) + "\nThe chat session is ended."
