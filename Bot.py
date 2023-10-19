import telebot


import config
import utils

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы конвертировать валюту введите команду в следующем формате:\n \
<имя валюты> <в какую валюту перевести> <кол-во переводимой валюты>\n \
Чтобы увидеть доступные для конвертации валюты введите /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in config.keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        if len(message.text.split(' ')) > 3:
            raise utils.ConversionException('Слижком много параметров')
        elif len(message.text.split(' ')) < 3:
            raise utils.ConversionException('Не достаточно параметров')

        currencies, base_currency, amount = message.text.split(' ')
        total = utils.Converter.convert(currencies, base_currency, amount)
    except utils.ConversionException as e:
        bot.send_message(message.chat.id, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base_currency} в {currencies} равна: {total}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
