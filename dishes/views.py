from django.shortcuts import render
from dishes.models import Dish, Drink
from django.views.generic import TemplateView, ListView, View, FormView
from django.http import HttpResponse
from django import forms
from django.views.generic.edit import UpdateView, FormView
from dishes.models import Ingredient
from dishes.forms import IngredientForm, DishForm, DrinkForm


class AboutView(TemplateView):
    model = Drink
    template_name = 'drink.html'


class BaseView(View):
    greeting = 'W E L C O M E ! ! !'

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.greeting)


class DrinkList(ListView):
    model = Drink
    template_name = 'drink_list.html'


class AddNewDrink(FormView):
    form_class = DrinkForm
    template_name = 'send.html'
    success_url = '/drinks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DrinkUpdate(UpdateView):
    form_class = DrinkForm
    model = Drink
    template_name = 'send.html'
    success_url = '/drinks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DishList(ListView):
    model = Dish
    template_name = 'dish_list.html'


class AddNewDish(FormView):
    form_class = DishForm
    template_name = 'send.html'
    success_url = '/dishes'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DishUpdate(UpdateView):
    form_class = DishForm
    model = Dish
    template_name = 'send.html'
    success_url = '/dishes'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IngredientList(ListView):
    model = Ingredient
    template_name = 'ingredients_list.html'


class AddNewIngredient(FormView):
    form_class = IngredientForm
    template_name = 'send.html'
    success_url = '/ingredients'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IngredientUpdate(UpdateView):
    form_class = IngredientForm
    model = Ingredient
    template_name = 'send.html'
    success_url = '/ingredients'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
