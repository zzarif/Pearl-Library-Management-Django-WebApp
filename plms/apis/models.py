from django.db import models
from django.db.models.deletion import CASCADE


class User(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    role_is_borrower = models.BooleanField()
    phone_number = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Book(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    number_of_copies_bought = models.IntegerField()

    def __str__(self):
        return self.title


class Borrowing_Log(models.Model):
    trans_id = models.AutoField(primary_key=True,auto_created=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE,db_column='book_id')
    borrowing_date = models.DateField()
    returning_date = models.DateField()
    book_returned = models.BooleanField()



class Feedback(models.Model):
    feedback = models.CharField(max_length=500)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column='user_id')



class Message(models.Model):
    name = models.CharField(max_length=100)
    email_addresses = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
