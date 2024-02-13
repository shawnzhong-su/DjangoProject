from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Author


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', "market_price"]

    list_display_links = ['title']

    list_filter = ["price"]

    search_fields = ['title']

    list_editable = ['price', 'market_price']


admin.site.register(Book, BookManager)


class AuthorManager(admin.ModelAdmin):
    list_display = ['name', "age", 'id']

    list_display_links = ["name"]

    list_filter = ["age"]

    search_fields = ["name"]

    list_editable = ["age"]


admin.site.register(Author, AuthorManager)
