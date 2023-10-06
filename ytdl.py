#API_TOKEN = 'tokenumba'
import telebot
from pytube import YouTube
import os
os.mkdir('videos')
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def hellothere(message):
    f = open('hello.gif', 'rb')
    bot.send_animation(message.chat.id, f)
    f.close()
    bot.send_message(message.chat.id, 'я могу качать видосы с ютуба но не присылай видосы более 10 минут иначе захлебнусь в говне(слабая хостмашина)')
@bot.message_handler()
def dlvid(message):
    try:
        yt = YouTube(message.text)
        bot.send_message(message.chat.id, 'загружаю')
        yt.streams.get_highest_resolution().download('./videos')
        for filename in os.listdir('./videos'):
            ff = open('./videos/'+filename, 'rb')
            bot.send_message(message.chat.id, 'присылаю')
            bot.send_video(message.chat.id, ff)
            ff.close()
            os.remove('./videos/' + filename)
    except:
        for filename in os.listdir('./videos'):
            os.remove('./videos/' + filename)
        bot.send_message(message.chat.id, 'некорректная ссылка или слишком большое видео')
if __name__ == '__main__':
    bot.infinity_polling()
