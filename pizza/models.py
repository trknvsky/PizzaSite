from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=256)


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    is_vegan = models.BooleanField(default=False)
    is_meat = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)


class Pizza(models.Model):
    name = models.CharField(max_length=256)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    ingredients = models.ManyToManyField(Ingredient)


class Staff(models.Model):
    name = models.CharField(max_length=256)


class Table(models.Model):
    number = models.IntegerField


class Order(models.Model):
    date = models.DateField
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    sum_order = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
