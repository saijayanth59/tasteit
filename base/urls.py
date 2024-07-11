from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-item', views.add_item, name='add-item'),
    path('add-ingredient', views.add_ingredient, name='add-ingredient'),
    path('process-order', views.process_order, name='process-order'),
    path('view-orders', views.view_orders, name='view-orders'),
    path('add-inventory-order', views.add_inventory_order,
         name='add-inventory-order')

]
