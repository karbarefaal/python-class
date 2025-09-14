# install pyTelegramBotAPI
# import pyTelegramBotAPI
import os
import telebot
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    print(message)
    
@bot.message_handler(commands=['salam'])
def send_welcome(message):
    bot.reply_to(message, "Siche alaki sedam mizani?")
    print(message)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()