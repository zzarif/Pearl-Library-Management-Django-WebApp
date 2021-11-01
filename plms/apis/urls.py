from django.urls import path
from . import views

urlpatterns = [
    path('register-user/',views.register_user,name="register_user"),
    path('user-info-all/',views.user_info_all,name="user_info_all"),
    path('user-info/<str:pk>/',views.user_info,name="user_info"),
    path('delete-user/<str:pk>/',views.delete_user,name="delete_user"),
    path('validate-user/',views.validate_user,name="validate_user"),
    path('add-feedback/',views.add_feedback,name="add_feedback"),
    path('feedback-all/',views.feedback_all,name="feedback_all"),
    path('feedback/<str:user_id>/',views.feedback,name="feedback"),

]