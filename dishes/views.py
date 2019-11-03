from django.shortcuts import render
from dishes.models import Dish, Drink
from django.views.generic import TemplateView, ListView, View, FormView
from django.http import HttpResponse
from django import forms


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


class ContactForm(forms.Form):
    name = forms.CharField(max_length=256)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print('MESSAGE: ', self.cleaned_data)


class Send(FormView):
    template_name = 'send.html'
    form_class = ContactForm
    success_url = '/send'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
