from django.urls import path
from . import views

urlpatterns = [
    path('book-list/',views.bookList,name='bookList'),
    path('add-book/',views.addBook,name='addBook'),
]