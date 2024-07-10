from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-item', views.add_item, name='add-item'),
    path('add-ingredient', views.add_ingredient, name='add-ingredient'),
    path('place-order', views.place_order, name='place-order'),
]
