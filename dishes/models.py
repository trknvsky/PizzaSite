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

    @staticmethod
    def change_price(price):
        dishes = Dish.objects.all()
        for dish in dishes:
            dish.price += price
            dish.save()

    def create_order(self, count):
        return InstanceDish.objects.create(
                name=self.name,
                price=self.price,
                dish=self,
                count=count
            )


class Drink(BaseItem):

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'

    def __str__(self):
        return self.name


class InstanceDish(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    count = models.PositiveIntegerField(default=1)
    dish = models.ForeignKey(
        Dish, related_name='dishes',
        null=True, blank=True, on_delete=models.SET_NULL
        )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return 'Блюдо: {}, цена: {}, количество: {}, сумма: {}'.format(
            self.name,
            str(self.price),
            str(self.count),
            str(self.price * self.count)
            )
