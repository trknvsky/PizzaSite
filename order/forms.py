from django import forms
from django.forms import ModelForm
from order.models import Order
from dishes.models import *


class DishForm(forms.Form):
	dish_id = forms.IntegerField()
	count = forms.IntegerField()


class ChangeInstance(ModelForm):
	class Meta:
		model = InstanceDish
		fields = ['count']