import telebot
import time
from threading import Thread

token = "TOKEN"

bot = telebot.TeleBot(token=token)

users = set()

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет, это бот спамер, не добавляй его((")

@bot.message_handler(commands=["what"])
def start_handler(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=rdg4lkgsQ04")

@bot.message_handler(commands=["spam"])
def start_spam_handler(message):
    users.add(message.chat.id)
    bot.send_message(message.chat.id, "Берем сироп вишневый!")

@bot.message_handler(commands=["stop"])
def stop_spam_handler(message):
    users.remove(message.chat.id)
    bot.send_message(message.chat.id, "Все все.")


@bot.message_handler(content_types=["text"])
def process_message(message):
    try:
        answer = eval(message.text)
    except:
        answer = "Это не работает :("
    bot.send_message(message.chat.id, answer)

def polling():
    global bot
    global users
    bot.polling(none_stop=True)

def spam():
    while True:
        for user in users:
            bot.send_message(user, "Затем сироп вишневый!")
        time.sleep(2)

thread = Thread(target=spam)
thread.start()
thread1 = Thread(target=polling)
thread1.start()
