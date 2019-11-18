from django.shortcuts import render
from orders.models import *
from django.views.generic import FormView
from django.views.generic.edit import UpdateView, FormView
from order.forms import *


class OrderFormView(FormView):
    form_class = AddOrderForm
    template_name = 'send.html'
    success_url = '/dishes'

    def form_valid(self, form):
        dish = form.cleaned_data.get('name', 'count', 'price')
        print('name', name)
        return super().form_valid(form)