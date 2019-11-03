from django.shortcuts import render
from dishes.models import Dish, Drink
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponse


class PizzaList(ListView):
    model = Dish
    template_name = 'dish_list.html'


class AboutView(TemplateView):
    model = Drink
    template_name = 'drink.html'


class BaseView(View):
    greeting = 'W E L C O M E ! ! !'

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.greeting)
