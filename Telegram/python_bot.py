import telebot

token = "YOUR TOKEN HERE"

bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        answer = eval(message.text)
    except:
        answer = "Это не работает :("
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)