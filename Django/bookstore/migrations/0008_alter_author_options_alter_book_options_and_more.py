# Generated by Django 4.2.9 on 2024-02-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_book_is_activate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者名称', 'verbose_name_plural': '作者名称'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书名', 'verbose_name_plural': '书名'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
    ]
