import telebot
import webbrowser

bot = telebot.TeleBot('6870736874:AAGNFS6UxAnblpOL8efyQm-oNWf6Qo1_234')


# Отправка сообщения от бота к пользователю
@bot.message_handler(commands=['start', 'hello'])  # Команды, на которые бот отвечает
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')  # Ответ бота на наши команды

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<u><a href="https://youtube.com">INFO</a></u>',
                     parse_mode='html')  # Параметр parse_mode позволяет выводить сообщения в тегах


@bot.message_handler()  # Декоратор без параметров отвечает на простые сообщения без комманд, по типу /start, /help
def info(message):
    if message.text.lower() == 'id':
        bot.send_message(message.chat.id, f'ID: {message.from_user.id}')


@bot.message_handler(commands=['website'])
def main(message):
    webbrowser.open('https://youtube.com')

bot.polling(none_stop=True)
