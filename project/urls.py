
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from dishes.views import *
from order.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('drink/', AboutView.as_view()),
    path('home/', BaseView.as_view()),
    path('ingredientsedit/<int:pk>/', IngredientUpdateView.as_view()),
    path('addingredient/', AddNewIngredientView.as_view()),
    path('ingredients/', IngredientListView.as_view()),
    path('dishedit/<int:pk>/', DishUpdateView.as_view()),
    path('dishadd/', AddNewDishView.as_view()),
    path('dishes/', DishListView.as_view()),
    path('drinkedit/<int:pk>/', DrinkUpdateView.as_view()),
    path('drinkadd/', AddNewDrinkView.as_view()),
    path('drinks/', DrinkListView.as_view()),
    path('dish/', DishView.as_view()),
    path('changepricedish/', ChangePriceDishView.as_view()),
    path('dishes/addpizza/', AddDishView.as_view()),
    path('order', OrderView.as_view()),
    path('changeinstance/<int:pk>/', InstanceUpdateView.as_view()),
    path('makeorder/<int:pk>/', MakeOrderView.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += staticfiles_urlpatterns()
