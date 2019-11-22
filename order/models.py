from django.db import models
from dishes.models import Dish, Drink
from accounts.models import User


class Order(models.Model):
    dishes = models.ManyToManyField(Dish, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
