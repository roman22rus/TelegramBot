import requests
import json

from config import *
class ConvertioneExceptione(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertioneExceptione(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertioneExceptione(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertioneExceptione(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)

        except ValueError:
            raise ConvertioneExceptione(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])*float(amount)
        return total_base




