from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Book, Feedback, User
from .serializers import UserSerializer


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
@api_view(['DELETE'])
def delete_user(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response(simple_response(1,"User deleted"))



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
