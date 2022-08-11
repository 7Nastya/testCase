from djmoney.models.fields import MoneyField
from django.utils import timezone
from moneyed import Money, RUB, USD
from django.db import models


class Order(models.Model):
    number = models.CharField(max_length=200, verbose_name="№", null=True)
    number_order = models.CharField(max_length=200, verbose_name="№ заказа", null=True)
    price_in_usd = MoneyField(max_digits=14, decimal_places=2, default_currency=USD, verbose_name="стоимость,$")
    price_in_rub = MoneyField(max_digits=14, decimal_places=2, default_currency=RUB, verbose_name="стоимость,руб.")
    date_supply = models.DateField(default=timezone.now, verbose_name="дата поставки")

    class Meta:
        verbose_name_plural = 'Заказ'
        verbose_name = 'Заказы'