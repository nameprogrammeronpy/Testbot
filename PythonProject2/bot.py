
import telebot

token = '1374966217:AAHd7GQAPMfoW8KBzKhy6tn6vzuRGioAwqQ'
bot = telebot.TeleBot('1374966217:AAHd7GQAPMfoW8KBzKhy6tn6vzuRGioAwqQ')


# Укажите токен вашего бота, полученный от BotFather


# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я ваш бот. Напишите /help, чтобы узнать, что я умею.")

# Функция для обработки команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Доступные команды:\n/start - Запустить бота\n/help - Показать это сообщение\n/echo - Повторить ваше сообщение.")

# Функция для обработки команды /echo
@bot.message_handler(commands=['echo'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

# Главная функция для запуска бота
if __name__ == "__main__":
    print("Бот запущен. Ожидание сообщений...")
    bot.infinity_polling()
