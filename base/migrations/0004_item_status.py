# Generated by Django 5.0.3 on 2024-07-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_item_ingridients_ingridientperitem_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
