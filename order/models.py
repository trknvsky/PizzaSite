from django.db import models
from dishes.models import Dish, Drink, InstanceDish
from accounts.models import User


class Order(models.Model):
    dishes = models.ManyToManyField(InstanceDish, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        price_dishes = sum([dish.price for dish in self.dishes.all()])
        price_drinks = sum([drink.price for drink in self.drinks.all()])
        print('price_dishes', price_dishes)
        print('price_drinks', price_drinks)
        self.price = price_dishes + price_drinks
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



