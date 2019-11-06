"""pizzasite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dishes.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('drink/', AboutView.as_view()),
    path('home/', BaseView.as_view()),
    path('ingredientsedit/<int:pk>/', IngredientUpdate.as_view()),
    path('addingredient/', AddNewIngredient.as_view()),
    path('ingredients/', IngredientList.as_view()),
    path('dishedit/<int:pk>/', DishUpdate.as_view()),
    path('dishadd/', AddNewDish.as_view()),
    path('dishes/', DishList.as_view()),
    path('drinkedit/<int:pk>/', DrinkUpdate.as_view()),
    path('drinkadd/', AddNewDrink.as_view()),
    path('drinks/', DrinkList.as_view()),
]
