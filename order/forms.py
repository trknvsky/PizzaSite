from django import forms
from django.forms import ModelForm
from order.models import Order
from dishes.models import InstanceDish


class AddOrderForm(forms.Form):
	dish_name = forms.CharField(max_length=50)
	dish_price = forms.DecimalField(max_digits=9, decimal_places=2)
	count = forms.IntegerField(max_length=10)