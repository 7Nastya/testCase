from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'number_order', 'price_in_usd', 'price_in_rub', 'date_supply',)
    list_filter = ('date_supply',)


admin.site.register(Order, OrderAdmin)
