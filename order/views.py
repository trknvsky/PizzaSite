from django.shortcuts import render
from order.models import *
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import TemplateView, ListView, View, FormView
from order.forms import *
from dishes.models import *
from rest_framework import routers, serializers, viewsets
from order.serializers import OrderSerializer
from .tasks import *
from dishes.tasks import *


class AddDishView(FormView):
	template_name = "dish_list.html"
	form_class = DishForm
	success_url = '/dishes'

	def form_valid(self, form):
		dish_id = form.cleaned_data.get('dish_id')
		count = form.cleaned_data.get("count")
		order_add.delay(dish_id, count)
		parsing_pizzas.delay()
		return super().form_valid(form)


class OrderView(ListView) :
	model = Order
	template_name = 'order.html'


class InstanceUpdate(UpdateView):
	form_class = ChangeInstance
	model = InstanceDish
	template_name = 'send.html'
	success_url = '/order'

	def form_valid(self, form):
		instance = super().form_valid(form)
		order = Order.objects.get()
		order.calculate_price()
		return instance


class MakeOrderView(UpdateView):
	template_name = "make_order.html"
	model = Order
	form_class = OrderForm
	success_url = '/order_sucess/'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'order_sucess.html'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
