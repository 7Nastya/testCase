from testCase import settings


class CurrencyClient(object):
    def __init__(self, currency='USD'):
        self.url = settings.BANK_URL
        self.currency = currency

    def get_currency(self):
        return 0