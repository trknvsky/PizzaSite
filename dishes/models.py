from django.db import models


class BaseItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    class Meta:
        abstract = True


class Ingredient(BaseItem):
    is_vegan = models.BooleanField(default=False)
    is_meat = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name


class Dish(BaseItem):
    ingredients = models.ManyToManyField(Ingredient, blank=True, null=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class Drink(BaseItem):

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'

    def __str__(self):
        return self.name


