from django.contrib import admin
from .models import Book,User,Feedback

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Feedback)