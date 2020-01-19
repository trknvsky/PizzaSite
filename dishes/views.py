from django.shortcuts import render
from dishes.models import Dish, Drink
from django.views.generic import TemplateView, ListView, View, FormView
from django.http import HttpResponse
from django import forms
from django.views.generic.edit import UpdateView, FormView
from dishes.models import Ingredient
from dishes.forms import *
from rest_framework import routers, serializers, viewsets
from dishes.serializers import DishSerializer, IngregientSerializer, InstanceDishSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


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
    sorting_fields = ['name', 'price', '-price']

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'name')
        if ordering not in self.sorting_fields:
            ordering = 'name'
        queryset = Dish.objects.all().order_by(ordering)
        return queryset

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(DishListView, self).dispatch(request, *args, **kwargs)


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


class ChangePriceDish(FormView):
    form_class = ChangePriceForm
    template_name = 'change_price_form.html'
    success_url = '/dishes'


    def form_valid(self, form):
        price = form.cleaned_data.get('price')
        Dish.change_price(price)
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


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngregientSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all().order_by('name')
    serializer_class = DishSerializer


class InstanceDishViewSet(viewsets.ModelViewSet):
    queryset = InstanceDish.objects.all()
    serializer_class = InstanceDishSerializer
