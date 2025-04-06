import telebot
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=['start']) #/start #/help #/go
def start_command(message):
    user_name = message.from_user.first_name
    text = (    
        f'Привет, {user_name}!\n\n'
        'Я - бот, который классифицирует картинку.\n'
        'Отправь картинку, чтобы узнать его класс'
    )

@bot.send_message(message.chat.id, text)
def handle_photo(message):
    #проверка наличия фото
    if not message.photo:
        return bot.send_message(message.chat.id, 'Вы забыли загрузить фото')
    #получени инфо о фото
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1] #something/somewhere/input.jpg
    #скачивание и сохранение фото
    downloaded_file = bot.download_file(file_info.file_path)
    with open('f"images"/{file_name}') as file:
        file.write(downloaded_file)

bot.infinity_polling()