import os
import telebot

# BOT_TOKEN = os.environ.get('BOT_TOKEN')



token = input("Token> ")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? I'm your gym assistant and will be giving you your six day split!")

@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = "Here are the available commands:\n"
    help_text += "/start or /hello - Start a conversation\n"
    help_text += "/help - Display this help message\n"

    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
