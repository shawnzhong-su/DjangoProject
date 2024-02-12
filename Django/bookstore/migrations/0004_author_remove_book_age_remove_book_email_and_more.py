# Generated by Django 4.2.9 on 2024-02-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_book_age_book_email_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=11, verbose_name='Name')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('email', models.EmailField(default=0, max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='age',
        ),
        migrations.RemoveField(
            model_name='book',
            name='email',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
    ]
