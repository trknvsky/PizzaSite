from django.db import models
from dishes.models import Dish, Drink, InstanceDish
from accounts.models import User


class Order(models.Model):
    dishes = models.ManyToManyField(InstanceDish, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    user_profile = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{}'.format(self.id)

    def dishes_list(self):
        return ([dish.name for dish in self.dishes.all()])

    def calculate_price(self):
        self.full_price = 0
        for dish in self.dishes.all():
            self.full_price += dish.price * dish.count
        self.save()