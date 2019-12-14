from django.db import models
from dishes.models import Dish, Drink, InstanceDish
from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    dishes = models.ManyToManyField(InstanceDish, blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    user_profile = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    phone_number = PhoneNumberField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True, blank=True)

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