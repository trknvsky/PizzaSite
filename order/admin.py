from django.contrib import admin
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'place_delivery', 'user_profile']
    readonly_fields = ['price']


admin.site.register(Order, OrderAdmin)
