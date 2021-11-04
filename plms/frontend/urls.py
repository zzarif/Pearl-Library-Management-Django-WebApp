from django.urls import path
from . import views

urlpatterns = [

    # home
    path('',views.home,name='home'),

    # login
    path('user-login/',views.user_login,name='user_login'),
    path('admin-login/',views.admin_login,name='admin_login'),

    # register
    path('user-register/',views.user_register,name='user_register'),

    # profile
    path('profile/',views.profile,name='profile'),



    # path('add-book/',views.addBook,name='addBook'),
]