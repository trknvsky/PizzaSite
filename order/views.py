from django.shortcuts import render
from order.models import *
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import TemplateView, ListView, View, FormView
from order.forms import *
from dishes.models import *

class AddDishView(FormView):
	template_name = "dish_list.html"
	form_class = DishForm
	success_url = '/dishes'

	def form_valid(self, form):
		dish = Dish.objects.get(id=form.cleaned_data.get('dish_id'))
		count = form.cleaned_data.get("count")
		instance = Dish.create_order(dish, count)
		order, created = Order.objects.get_or_create(user_profile=self.request.user)
		order.dishes.add(instance)
		order.calculate_price()
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
		order = Order.objects.get(user_profile=self.request.user)
		order.calculate_price()
		return instance
