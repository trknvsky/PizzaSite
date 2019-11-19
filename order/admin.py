from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_price', 'user_profile']


admin.site.register(Order, OrderAdmin)
