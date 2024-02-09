from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('Book_name', max_length=50, default=" ")
    price = models.DecimalField("price", max_digits=8, decimal_places=3)
