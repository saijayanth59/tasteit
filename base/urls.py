from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-item', views.add_item, name='add-item'),
    path('add-ingredient', views.add_ingredient, name='add-ingredient'),
    path('item-order', views.item_order, name='item-order'),
    path('ingredient_order', views.ingredient_order, name='ingredient-order'),
    path('view-orders', views.view_orders, name='view-orders'),
    path('add-inventory-order', views.add_inventory_order,
         name='add-inventory-order'),
    path('view-inventory-orders', views.view_inventory_orders,
         name='view-inventory-orders'),
    path('inventory-order/<str:pk>', views.inventory_order, name='inventory-order')

]
