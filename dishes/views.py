from django.shortcuts import render
from dishes.models import Dish, Drink
from django.views.generic import TemplateView, ListView, View, FormView
from django.http import HttpResponse
from django import forms
from django.views.generic.edit import UpdateView, FormView
from dishes.models import Ingredient
from dishes.forms import *


class AboutView(TemplateView):
    model = Drink
    template_name = 'drink.html'


class BaseView(View):
    greeting = 'W E L C O M E ! ! !'

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.greeting)


class DrinkListView(ListView):
    model = Drink
    template_name = 'drink_list.html'


class AddNewDrink(FormView):
    form_class = DrinkForm
    template_name = 'send.html'
    success_url = '/drinks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DrinkUpdateView(UpdateView):
    form_class = DrinkForm
    model = Drink
    template_name = 'send.html'
    success_url = '/drinks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    sorting_fields = ['name', 'price', '-price']

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'name')
        if ordering not in self.sorting_fields:
            ordering = 'name'
        queryset = Dish.objects.all().order_by(ordering)
        return queryset


class DishView(ListView):
    model = Dish
    template_name = 'dishes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_count'] = Dish.objects.count()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Dish.objects.values_list('name', flat=True).order_by('price')
        return queryset


class AddNewDishView(FormView):
    form_class = DishForm
    template_name = 'send.html'
    success_url = '/dishes'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DishUpdateView(UpdateView):
    form_class = DishForm
    model = Dish
    template_name = 'send.html'
    success_url = '/dishes'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ChangePriceDishView(FormView):
    form_class = ChangePriceForm
    template_name = 'change_price_form.html'
    success_url = '/dishes'

    def form_valid(self, form):
        price = form.cleaned_data.get('price')
        Dish.change_price(price)
        return super().form_valid(form)


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredients_list.html'


class AddNewIngredientView(FormView):
    form_class = IngredientForm
    template_name = 'send.html'
    success_url = '/ingredients'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IngredientUpdateView(UpdateView):
    form_class = IngredientForm
    model = Ingredient
    template_name = 'send.html'
    success_url = '/ingredients'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
