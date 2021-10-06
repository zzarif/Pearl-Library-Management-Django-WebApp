from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def api(request):
    api_urls = {
        'bookList':'bookList/',
        'book': 'book/<str:pk>',
        'addBook': 'addBook/',
        'updateBook': 'updateBook/<str:pk>/',
        'deleteBook': 'deleteBook/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book(request,pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBook(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response("Book successfully deleted.")
