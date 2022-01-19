import telebot

bot = telebot.TeleBot("5069674898:AAGdHYM4cn-ZqQqbhR2vke34ke8qMos1lTY", parse_mode=None)

WELCOME_MSG = "👋 Howdy, how are you doing? \
I can convert video to the following formats: *.avi, *.gif, *.mov! \
Just upload a short video for me, and then choose file type you want."

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, WELCOME_MSG)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()