# Generated by Django 4.0.3 on 2022-06-23 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ('name',), 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created'], 'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
    ]