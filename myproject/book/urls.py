from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listbook/', views.list_books, name='list_books'),
]
