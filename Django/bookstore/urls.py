from bookstore import views
from django.urls import path, include

post_url_pattern = {
    path('retrieve/', views.retrieveBooks, name="retrieve data from all books"),
    path('all_book', views.all_book),
    path('update_book/<int:book_id>', views.update_book),
    path('delete_book/', views.delete_book)
}
