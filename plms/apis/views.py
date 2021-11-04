from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Book, Feedback, User
from .serializers import BookSerializer, UserSerializer


def simple_response(code,message):
    return {
        "response_code": code,
        "response_message": message
    }


### Function that receives
### new user info in JSON
### format and creates new
### user/throws error
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(simple_response(1,"User created successfully"))
    else:
        return Response(simple_response(0,"Something went wrong"))

        

### fetch all users 
@api_view(['GET'])
def user_info_all(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)


### fetch particular user
### by user_id
@api_view(['GET'])
def user_info(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)



### delete a user
# @api_view(['DELETE'])
# def delete_user(request,pk):
#     user = User.objects.get(id=pk)
#     user.delete()
#     return Response(simple_response(1,"User deleted"))



### Function that receives
### user_id,password in JSON
### format, verifies the user
### and sends appropriate response
@api_view(['POST'])
def validate_user(request):
    str_request = json.dumps(request.data)
    dict_request = json.loads(str_request)
    received_id = dict_request['id']
    received_pwd = dict_request['password']
    try:
        with connection.cursor() as c:
            row = c.execute(
                "SELECT id,password FROM apis_user WHERE id=%s",
                [received_id]
            ).fetchone()
            if received_id==row[0] and received_pwd==row[1]:
                return Response(simple_response(1,"Login successful"))
            elif received_pwd!=row[1]:
                return Response(simple_response(0,"Invalid password"))  
    except:
        return Response(simple_response(0,"User doesn't exist"))




### function to add
### feedback, takes JSON
### data, inserts to db
@api_view(['POST'])
def add_feedback(request):
    str_request = json.dumps(request.data)
    dict_request = json.loads(str_request)
    rcvd_feedback = dict_request['feedback']
    rcvd_user_id = dict_request['user_id']
    try:
        with connection.cursor() as c:
            c.execute(
                "INSERT INTO apis_feedback(feedback,user_id) VALUES(%s,%s)",
                [rcvd_feedback,rcvd_user_id]
            )
            return Response(simple_response(1,"Feedback added"))
    except:
        return Response(simple_response(0,"Something went wrong"))




### fetch all feedbacks
@api_view(['GET'])
def feedback_all(request):
    with connection.cursor() as c:
        rows = c.execute(
            "SELECT user_id,feedback FROM apis_feedback"
        ).fetchall()
        str_response = json.dumps([{
            "user_id": row[0],
            "feedback": row[1]
        }for row in rows])
        dict_response = json.loads(str_response)
        return Response(dict_response)



### fetch feedback for
### a particular user
@api_view(['GET'])
def feedback(request,user_id):
    with connection.cursor() as c:
        rows = c.execute(
            """SELECT u.name,f.feedback 
            FROM apis_user u,apis_feedback f 
            WHERE u.id=f.user_id AND u.id=%s""",
            [user_id]
        ).fetchall()
        str_response = json.dumps([{
            "name": row[0],
            "feedback": row[1]
        }for row in rows])
        dict_response = json.loads(str_response)
        return Response(dict_response)




### Add Book, receives
### JSON request body and
### inserts into book table
@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(simple_response(1,"Book added successfully"))
    else:
        return Response(simple_response(0,"Something went wrong"))



### fetch all books 
@api_view(['GET'])
def book_info_all(request):
    users = Book.objects.all()
    serializer = BookSerializer(users,many=True)
    return Response(serializer.data)


### fetch SHORT info
### for book list with
### AVAILABILITY STATUS
@api_view(['GET'])
def book_list_short_info(request):
    with connection.cursor() as c:
        rows = c.execute(
            """WITH BooksInformation AS (WITH NumberOFBorrowedCopiesPerBook 
            AS (SELECT book_id,COUNT(trans_id) AS NumberOfBorrowedCopies FROM 
            apis_borrowing_log WHERE book_returned=false GROUP BY book_id) SELECT 
            apis_book.*,ifnull(apis_book.number_of_copies_bought-NumberOFBorrowedCopies,
            apis_book.number_of_copies_bought) AS NumberOfAvailableCopies,CASE 
            apis_book.number_of_copies_bought-NumberOFBorrowedCopies WHEN 0 THEN 
            false ELSE true END AS AvailabilityStatus FROM apis_book LEFT OUTER 
            JOIN NumberOFBorrowedCopiesPerBook ON book_id=apis_book.id)
            
            SELECT title,author,category,CASE AvailabilityStatus WHEN true 
            THEN 'Available' WHEN false THEN 'Not Available' END as 
            Availability from BooksInformation"""
        ).fetchall()
        str_response = json.dumps([{
            "title": row[0],
            "author": row[1],
            "category": row[2],
            "availability_status": row[3]
        }for row in rows])
        dict_response = json.loads(str_response)
        return Response(dict_response)





### fetch DETAIL info
### for book list with
### AVAILABILITY STATUS
@api_view(['GET'])
def book_list_detail_info(request,book_id):
    with connection.cursor() as c:
        row = c.execute(
            """WITH BooksInformation AS (WITH NumberOFBorrowedCopiesPerBook 
            AS (SELECT book_id,COUNT(trans_id) AS NumberOfBorrowedCopies FROM 
            apis_borrowing_log WHERE book_returned=false GROUP BY book_id) SELECT 
            apis_book.*,ifnull(apis_book.number_of_copies_bought-NumberOFBorrowedCopies,
            apis_book.number_of_copies_bought) AS NumberOfAvailableCopies,CASE 
            apis_book.number_of_copies_bought-NumberOFBorrowedCopies WHEN 0 THEN 
            false ELSE true END AS AvailabilityStatus FROM apis_book LEFT OUTER 
            JOIN NumberOFBorrowedCopiesPerBook ON book_id=apis_book.id)
            
            SELECT id,title,author,publisher,category,description,number_of_copies_bought,
            CASE AvailabilityStatus WHEN true THEN 'Available' WHEN false THEN 'Not Available' 
            END AS Available FROM BooksInformation WHERE id=%s""", [book_id]
        ).fetchone()
        return Response({
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "publisher": row[3],
            "category": row[4],
            "description": row[5],
            "number_of_copies_bought": row[6],
            "availability_status": row[7]
        })



### Request a book
@api_view(['POST'])
def request_book(request):
    str_request = json.dumps(request.data)
    dict_request = json.loads(str_request)
    rcvd_book_id = dict_request['book_id']
    rcvd_user_id = dict_request['user_id']
    with connection.cursor() as c:
        # check if user is allowed
        row = c.execute(
            """with BorrowersInformation AS(with NumberofBooksTakenPerBorrower 
            as (select user_id,count(trans_id) as NumberOfBooksTaken from 
            apis_borrowing_log where book_returned=false group by user_id)
            Select apis_user.*,ifnull(NumberOfBooksTaken,0) as NumberOfBooksTaken,
            CASE NumberOfBooksTaken WHEN 1 THEN false ELSE true END as CanBorrowMoreBooks  
            from apis_user LEFT OUTER JOIN NumberofBooksTakenPerBorrower ON apis_user.id
            =NumberofBooksTakenPerBorrower.user_id WHERE role_is_borrower=true)
            
            select CanBorrowMoreBooks from BorrowersInformation 
            where id=%s""",[rcvd_user_id]
        ).fetchone()
        if not row[0]:
            return Response(simple_response(0,"You cannot avail more books"))

        # check if book is available
        row = c.execute(
            """WITH BooksInformation AS (WITH NumberOFBorrowedCopiesPerBook 
            AS (SELECT book_id,COUNT(trans_id) AS NumberOfBorrowedCopies FROM 
            apis_borrowing_log WHERE book_returned=false GROUP BY book_id) SELECT 
            apis_book.*,ifnull(apis_book.number_of_copies_bought-NumberOFBorrowedCopies,
            apis_book.number_of_copies_bought) AS NumberOfAvailableCopies,CASE 
            apis_book.number_of_copies_bought-NumberOFBorrowedCopies WHEN 0 THEN 
            false ELSE true END AS AvailabilityStatus FROM apis_book LEFT OUTER 
            JOIN NumberOFBorrowedCopiesPerBook ON book_id=apis_book.id)

            select AvailabilityStatus from BooksInformation 
            where id=%s""",[rcvd_book_id]
        ).fetchone()
        if not row[0]:
            return Response(simple_response(0,"Book not available"))

        # request book
        c.execute(
            """INSERT INTO apis_borrowing_log(user_id,book_id,borrowing_date,
            returning_date,book_returned) VALUES(%s,%s,date('now'),date('now',
            '+3 month'),false)""", [rcvd_user_id,rcvd_book_id]
        )
        return Response(simple_response(1,"Book requested successfully"))


### list of borrowed books
@api_view(['GET'])
def borrowed_books(request,user_id):
    with connection.cursor() as c:
        rows = c.execute(
            """select apis_book.title,apis_book.author,
            apis_borrowing_log.returning_date from apis_borrowing_log,
            apis_user,apis_book where apis_user.id=apis_borrowing_log.user_id 
            AND apis_book.ID=apis_borrowing_log.book_id AND apis_user.ID=%s""",[user_id]
        ).fetchall()
        str_response = json.dumps([{
            "title": row[0],
            "author": row[1],
            "returning_date": row[2],
        }for row in rows],default=str)
        dict_response = json.loads(str_response)
        return Response(dict_response)



### borrowers info
@api_view(['GET'])
def borrowers_info_all(request):
    with connection.cursor() as c:
        rows = c.execute(
            """select apis_book.title,apis_book.author,apis_user.name,
            apis_borrowing_log.returning_date from apis_borrowing_log,
            apis_user,apis_book where apis_user.id=apis_borrowing_log.user_id 
            AND apis_book.id=apis_borrowing_log.book_id AND 
            apis_borrowing_log.book_returned=false"""
        ).fetchall()
        str_response = json.dumps([{
            "title": row[0],
            "author": row[1],
            "name": row[2],
            "returning_date": row[3],
        }for row in rows],default=str)
        dict_response = json.loads(str_response)
        return Response(dict_response)




### defaulted book info
@api_view(['GET'])
def defaulted_book_info_all(request):
    with connection.cursor() as c:
        rows = c.execute(
            """select apis_book.title,apis_book.author,apis_user.name,apis_user.phone_number,
            apis_borrowing_log.returning_date from apis_user,apis_borrowing_log,apis_book where 
            apis_user.id=apis_borrowing_log.user_id AND apis_book.id=apis_borrowing_log.book_id AND 
            julianday('now')-julianday(returning_date)>=0 
            AND apis_borrowing_log.book_returned=false"""
        ).fetchall()
        str_response = json.dumps([{
            "title": row[0],
            "author": row[1],
            "name": row[2],
            "phone_number": row[3],
            "returning_date": row[4],
        }for row in rows],default=str)
        dict_response = json.loads(str_response)
        return Response(dict_response)




### grant_book
@api_view(['GET'])
def grant_book(request,trans_id):
    with connection.cursor() as c:
        row = c.execute(
            """select apis_user.name,apis_book.title,apis_book.author,
            borrowing_date,returning_date from apis_borrowing_log,apis_user,
            apis_book where apis_user.ID=apis_borrowing_log.user_id AND 
            apis_book.ID=apis_borrowing_log.book_id AND trans_id=%s""",
            [trans_id]
        ).fetchone()
        return Response({
            "name": row[0],
            "title": row[1],
            "author": row[2],
            "borrowing_date": row[3],
            "returning_date": row[4]
        })



### receive_book
@api_view(['GET'])
def receive_book(request,trans_id):
    with connection.cursor() as c:
        c.execute(
            """Update apis_borrowing_log
            set book_returned=true
            where trans_id=%s""",
            [trans_id]
        )
        return Response(simple_response(1,"Book Received"))


# @api_view(['GET'])
# def bookList(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def book(request,pk):
#     books = Book.objects.get(id=pk)
#     serializer = BookSerializer(books,many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addBook(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response("Book added successfully.")

# @api_view(['POST'])
# def updateBook(request,pk):
#     book = Book.objects.get(id=pk)
#     serializer = BookSerializer(instance=book,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response("Book updated successfully.")

# @api_view(['DELETE'])
# def deleteBook(request,pk):
#     book = Book.objects.get(id=pk)
#     book.delete()
#     return Response("Book deleted successfully.")
