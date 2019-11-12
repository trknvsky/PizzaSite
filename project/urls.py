
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from dishes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
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
    path('dish/', DishView.as_view()),
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
