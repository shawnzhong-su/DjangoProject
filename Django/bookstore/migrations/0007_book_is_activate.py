# Generated by Django 4.2.9 on 2024-02-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_activate',
            field=models.BooleanField(default=True, verbose_name='is activate or not'),
        ),
    ]