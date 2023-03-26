# Generated by Django 3.2.18 on 2023-03-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_manufacturer_name'),
        ('cart', '0003_alter_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(
                blank=True, related_name='cart', to='catalog.Product'
            ),
        ),
    ]
