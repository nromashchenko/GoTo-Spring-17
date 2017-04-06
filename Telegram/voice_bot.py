import uuid

import telebot
from pydub import AudioSegment

token = "TOKEN"

bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=["voice"])
def save(message):
    file_id = message.voice.file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)
    name = str(uuid.uuid4())
    cname = name + ".ogg"
    with open('files/' + cname, 'wb') as new_file:
        new_file.write(downloaded_file)
    try:
        sound = AudioSegment.from_ogg("files/" + cname)
        sound.export("converted/" + name + ".wav", format="wav")
    except Exception as e:
        print(e)


bot.polling(none_stop=True)
