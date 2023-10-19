import telebot
from BotToken import TokenHolder


bot = telebot.TeleBot(TokenHolder.token)

keys = {'доллар': 'USD',
        'рубль': 'RUB',
        'евро': 'EUR'}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы конвертировать валюту введите команду в следующем формате:\n \
<имя валюты> <в какую валюту перевести> <кол-во переводимой валюты>'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)
