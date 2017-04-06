import uuid

import telebot

token = "TOKEN"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["photo"])
def save(message):
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    extn = '.' + str(path.file_path).split('.')[-1]
    downloaded_file = bot.download_file(path.file_path)
    cname = str(uuid.uuid4()) + extn
    with open('images/' + cname, 'wb') as new_file:
        new_file.write(downloaded_file)


bot.polling(none_stop=True)
