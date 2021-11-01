from django.shortcuts import render

def bookList(request):
    return render(request,'./admin/books.html')

def addBook(request):
    return render(request,'./admin/addbook.html')
