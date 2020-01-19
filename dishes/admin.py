from django.contrib import admin
from dishes.models import *


class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    filter_horizontal = ['ingredients']


admin.site.register(Dish, DishAdmin)
admin.site.register(Drink)
admin.site.register(Ingredient)
admin.site.register(InstanceDish)



