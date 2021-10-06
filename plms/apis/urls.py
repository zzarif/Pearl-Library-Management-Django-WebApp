from django.urls import path
from . import views

urlpatterns = [
    path('',views.api,name="api_overview"),
    path('bookList/',views.bookList,name="bookList"),
    path('book/<str:pk>/',views.book,name="book"),
    path('addBook/',views.addBook,name="addBook"),
    path('updateBook/<str:pk>/',views.updateBook,name="updateBook"),
    path('deleteBook/<str:pk>/',views.deleteBook,name="deleteBook"),
]