from django.urls import path
from . import views

urlpatterns = [
    # user info
    path('register-user/',views.register_user,name="register_user"),
    path('user-info-all/',views.user_info_all,name="user_info_all"),
    path('user-info/<str:pk>/',views.user_info,name="user_info"),
    # path('delete-user/<str:pk>/',views.delete_user,name="delete_user"),
    path('validate-user/',views.validate_user,name="validate_user"),

    # feedback
    path('add-feedback/',views.add_feedback,name="add_feedback"),
    path('feedback-all/',views.feedback_all,name="feedback_all"),
    path('feedback/<str:user_id>/',views.feedback,name="feedback"),


    # books (customer)
    path('book-list-short-info/',views.book_list_short_info,name="book_list_short_info"),
    path('book-list-detail-info/<str:book_id>/',views.book_list_detail_info,name="book_list_detail_info"),
    path('request-book/',views.request_book,name="request_book"),
    path('borrowed-books/<str:user_id>/',views.borrowed_books,name="borrowed_books"),

    # books (admin)
    path('add-book/',views.add_book,name="add_book"),
    path('book-info-all/',views.book_info_all,name="book_info_all"),
    path('borrowers-info-all/',views.borrowers_info_all,name="borrowers_info_all"),
    path('defaulted-book-info-all/',views.defaulted_book_info_all,name="defaulted_book_info_all"),
    path('grant-book/<int:trans_id>/',views.grant_book,name="grant_book"),
    path('receive-book/<int:trans_id>/',views.receive_book,name="receive_book"),


]