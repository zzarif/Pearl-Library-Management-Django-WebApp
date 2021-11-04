from django.contrib import admin
from .models import Book,User,Feedback,Borrowing_Log,Message

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(Borrowing_Log)
admin.site.register(Message)