from django.shortcuts import render, redirect
from .models import Item, Ingridient, IngridientPerItem
from .forms import ItemForm, IngredientForm, OrderForm
# Create your views here.

# Home page


def home(req):
    items = Item.objects.all()
    context = {'items': items}
    return render(req, 'base/home.html', context)

# Adding new Recipe


def add_item(req):
    form = ItemForm()
    ingredients = Ingridient.objects.all()
    if req.method == 'POST':
        veg = req.POST.get('veg')
        item = Item.objects.create(
            code=req.POST.get('code'),
            name=req.POST.get('name'),
            price=req.POST.get('price'),
            veg=(True if veg == 'on' else False)
        )
        required = req.POST.getlist('ingredients')
        for name in required:
            quantity = req.POST.get(name)
            ingredient = Ingridient.objects.get(name=name)
            IngridientPerItem.objects.create(
                ingridient=ingredient,
                item=item,
                quantity=quantity
            )

        return redirect('home')
    context = {'form': form, 'ingredients': ingredients}
    return render(req, 'base/add_item.html', context)


def add_ingredient(req):
    form = IngredientForm()
    ingredients = Ingridient.objects.all()
    if req.method == 'POST':
        ingredient = Ingridient.objects.create(
            name=req.POST.get('name'),
            price=req.POST.get('price'),
            quantity=req.POST.get('quantity')
        )
        # return redirect()
    context = {'form': form, 'ingredients': ingredients}
    return render(req, 'base/add_ingredients.html', context)


def place_order(req):
    form = OrderForm()
    if req.method == 'POST':
        print(req.POST)
    context = {'form': form}
    return render(req, 'base/place_order.html', context)
