from django.db import models
from django.db.models.deletion import CASCADE


class User(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    role_is_borrower = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Book(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    number_of_copies_bought = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Borrowing_Log(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrowing_date = models.CharField(max_length=100)
    returning_date = models.CharField(max_length=100)
    book_returned = models.CharField(max_length=20)



class Feedback(models.Model):
    feedback = models.CharField(max_length=500)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')



class Message(models.Model):
    name = models.CharField(max_length=100)
    email_addresses = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
