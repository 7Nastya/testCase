from testCase import settings
import requests
import json

class CurrencyClient(object):
    def __init__(self, currency='USD'):
        self.url = settings.BANK_URL
        self.currency = currency

    def get_currency(self):
        response = requests.get("https://cdn.cur.su/api/latest.json")
        dict_res = json.loads(response.text)
        rates = dict_res.get("rates")
        rub = rates.get("RUB")
        return rub