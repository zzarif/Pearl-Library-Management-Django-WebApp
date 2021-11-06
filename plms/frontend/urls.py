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
    path('user-profile/',views.user_profile,name='user_profile'),
    path('admin-profile/',views.admin_profile,name='admin_profile'),

    # books (borrower)
    path('user-profile/books/',views.books_user,name='books_user'),
    path('user-profile/book-requested/',views.book_requested,name='book_requested'),
    path('user-profile/borrowed-books/',views.borrowed_books,name='borrowed_books'),
    path('user-profile/detail-book/',views.detail_book_user,name='detail_book_user'),


    # books (admin)
    path('admin-profile/books/',views.books_admin,name='books_admin'),
    path('admin-profile/detail-book/',views.detail_book,name='detail_book'),
    path('admin-profile/add-book/',views.add_book,name='add_book'),
    path('admin-profile/borrowed-book-admin/',views.borrowed_book_admin,name='borrowed_book_admin'),
    path('admin-profile/borrowers/',views.borrowers,name='borrowers'),
    path('admin-profile/grant-book/',views.grant_book,name='grant_book'),
    path('admin-profile/receive-book/',views.receive_book,name='receive_book'),
    path('admin-profile/view-messages/',views.view_messages,name='view_messages'),
    path('admin-profile/expired-list-user/',views.expired_list_user,name='expired_list_user'),
    

    # feedback (user)
    path('user-profile/feedback/',views.user_feedback,name='user_feedback'),
    # feedback (admin)
    path('admin-profile/feedback/',views.admin_feedback,name='admin_feedback'),


    # contact
    path('contact/',views.contact,name='contact'),
    # path('add-book/',views.addBook,name='addBook'),
]