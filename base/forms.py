from django.forms import ModelForm
from .models import Item, Ingridient, Order


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class IngredientForm(ModelForm):

    class Meta:
        model = Ingridient
        fields = '__all__'


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
