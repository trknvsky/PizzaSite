from django.db import models
from dishes.models import Dish, Drink


class Order(models.Model):
    dishes = models.ManyToManyField(Dish, blank=True, null=True)
    drinks = models.ManyToManyField(Drink, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    place_delivery = models.CharField(max_length=512)
    user_profile = models.CharField(max_length=512)

    def update(self, *args, **kwargs):
        price_dishes = sum([dish.price for dish in self.dishes.all()])
        price_drinks = sum([drink.price for drink in self.drinks.all()])
        print('price_dishes', price_dishes)
        print('price_drinks', price_drinks)
        self.price = price_dishes + price_drinks
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



