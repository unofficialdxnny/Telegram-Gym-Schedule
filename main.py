import os
import telebot
from datetime import datetime

# Replace 'YOUR_TOKEN' with your actual bot token
token = input("Token> ")

bot = telebot.TeleBot(token)

# Define the gym plans for each day
gym_plans = {
    0: "Monday: Chest/Triceps/Shoulders",
    1: "Tuesday: Back/Biceps",
    2: "Wednesday: Legs/Abs",
    3: "Thursday: Back/Chest",
    4: "Friday: Shoulder/Arms",
    5: "Saturday: Abs/Legs",
    6: "Sunday: Rest Day"
}

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? I'm your gym assistant and will be giving you your six-day split!")

@bot.message_handler(commands=['help'])
def show_help(message):
    help_text = "Here are the available commands:\n"
    help_text += "/start or /hello - Start a conversation\n"
    help_text += "/help - Display this help message\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['gym'])
def send_daily_gym_plan(message):
    today = datetime.today().weekday()  # Get the current day of the week (0 = Monday, 1 = Tuesday, ...)
    plan = gym_plans.get(today, "No workout plan for today.")
    bot.send_message(message.chat.id, plan)

bot.infinity_polling()
