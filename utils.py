import requests
import json

import config


class ConversionException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(currencies, base_currency, amount):


        try:
            base_ticker = config.keys[base_currency]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base_currency}')

        try:
            c_ticker = config.keys[currencies]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {currencies}')

        if currencies == base_currency:
            raise ConversionException('Нельзя конвертировать валюту саму в себя')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.freecurrencyapi.com/v1/latest?apikey={config.api_key}&currencies={c_ticker}\
        &base_currency={base_ticker}')

        total = str(float(json.loads(r.content)['data'][config.keys[currencies]]) * amount)
        return total
