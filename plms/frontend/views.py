from django.shortcuts import render

# landing page
def home(request):
    return render(request,'./main/index.html')


# login
def user_login(request):
    return render(request,'./user/userlogin.html')

def admin_login(request):
    return render(request,'./admin/adminlogin.html')

# register
def user_register(request):
    return render(request,'./user/userregisterition.html')

# profile
def user_profile(request):
    return render(request,'./user/userporfile.html')

def admin_profile(request):
    return render(request,'./admin/adminporfile.html')

# books (borrower)
def books_user(request):
    return render(request,'./user/books.html')

def book_requested(request):
    return render(request,'./user/bookRequsted.html')

def borrowed_books(request):
    return render(request,'./user/borrowdbooks.html')

def detail_book_user(request):
    return render(request,'./user/detailsbook.html')

# books (admin)
def books_admin(request):
    return render(request,'./admin/books.html')

def detail_book(request):
    return render(request,'./admin/detailsbook.html')

def add_book(request):
    return render(request,'./admin/addbook.html')

def borrowed_book_admin(request):
    return render(request,'./admin/borrowedbook.html')

def borrowers(request):
    return render(request,'./admin/borrowers.html')

def grant_book(request):
    return render(request,'./admin/grantbook.html')

def receive_book(request):
    return render(request,'./admin/receivebook.html')

def view_messages(request):
    return render(request,'./admin/viewmessages.html')

def expired_list_user(request):
    return render(request,'./admin/expiredlist-user.html')



# feedback (user)
def user_feedback(request):
    return render(request,'./user/feedback.html')

# feedback (admin)
def admin_feedback(request):
    return render(request,'./admin/feedback.html')



# contact
def contact(request):
    return render(request,'./main/contact.html')

# def addBook(request):
#     return render(request,'./admin/addbook.html')
