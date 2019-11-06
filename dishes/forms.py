from django import forms
from django.forms import ModelForm
from dishes.models import Ingredient, Dish, Drink


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'is_vegan', 'is_meat', 'price']


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'ingredients', 'price']


class DrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ['name', 'price']

