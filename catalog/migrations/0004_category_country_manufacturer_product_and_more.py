# Generated by Django 4.1.7 on 2023-03-19 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_products'),
        ('catalog', '0003_alter_author_photo_alter_book_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=50)),
                (
                    'image',
                    models.ImageField(
                        blank=True,
                        default='image-placeholder.jpeg',
                        upload_to='countries/',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                (
                    'photo',
                    models.ImageField(
                        blank=True,
                        default='photo-placeholder.jpeg',
                        upload_to='manufacturers/',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                (
                    'image',
                    models.ImageField(
                        blank=True,
                        default='product-placeholder.jpeg',
                        upload_to='product/',
                    ),
                ),
                (
                    'category',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='catalog.category',
                    ),
                ),
                (
                    'country',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='catalog.country',
                    ),
                ),
                (
                    'manufacturer',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='catalog.manufacturer',
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
