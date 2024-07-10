from django.db import models


class Ingridient(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()  # current storage of ingrident

    class Meta:
        ordering = ('quantity', )

    def __str__(self):
        return self.name


class Item(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    # img = URL
    veg = models.BooleanField(default=None)

    def __str__(self):
        return self.name


class IngridientPerItem(models.Model):
    ingridient = models.ForeignKey(
        Ingridient, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,  null=True)
    # quantity means how much it required of ingrident
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.ingridient}: {self.quantity}"


class Order(models.Model):
    # Need to think of on_delete
    item = models.ForeignKey(Item, on_delete=models.CASCADE,  null=True)
    quantites = models.PositiveIntegerField()  # how many there are willing to buy
    bill = models.FloatField()
    ordered_start_time = models.DateTimeField(auto_now_add=True)
    ordered_end_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    def __str__(self) -> str:
        return self.item
