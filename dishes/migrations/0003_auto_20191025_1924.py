# Generated by Django 2.2.6 on 2019-10-25 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_auto_20191025_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.AlterModelOptions(
            name='drink',
            options={'verbose_name': 'Напиток', 'verbose_name_plural': 'Напитки'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингридиент', 'verbose_name_plural': 'Ингридиенты'},
        ),
    ]
