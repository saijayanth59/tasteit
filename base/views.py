from django.shortcuts import render, redirect
from .models import Item, Ingridient, IngridientPerItem, Order, InventoryOrder
from .forms import ItemForm, IngredientForm
from django.contrib import messages
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


def process_order(req):
    items = Item.objects.all()
    if req.method == 'POST':
        try:
            item = Item.objects.get(code=req.POST.get('code'))
            quantity = int(req.POST.get('quantity'))
            price = item.price
            order = Order.objects.create(
                item=item,
                quantites=quantity,
                bill=(quantity * price),
                status=True
            )
            return redirect('view-orders')
        except:
            messages.error(req, "Item code doesn't exit")

    context = {'items': items}
    return render(req, 'base/place_order.html', context)


def view_orders(req):
    orders = Order.objects.all().order_by('-ordered_start_time')
    context = {'orders': orders}
    print(orders)
    return render(req, 'base/view_orders.html', context)


# inventory
def add_inventory_order(req):
    ingredients = Ingridient.objects.all()
    if req.method == 'POST':
        order = InventoryOrder.objects.create(
            interval=req.POST.get('interval')
        )
        ingredients = req.POST.getlist('ingredients')
        for name in ingredients:
            ingredient = Ingridient.objects.get(name=name)
            order.ingredients.add(ingredient)
        print(order)
    context = {'ingredients': ingredients}
    return render(req, 'base/add_inventory_order.html', context)
