from django.contrib import admin
from .models import Ingridient, IngridientPerItem, Item, Order, InventoryOrder
# Register your models here.
admin.site.register(Ingridient)
admin.site.register(IngridientPerItem)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(InventoryOrder)
