from django.urls import path, include
from Django_learn import views

posturlpatterns = [
    path('test_post/', views.test_static, name="Test_for_static")

]
