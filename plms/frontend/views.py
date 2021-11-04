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
def profile(request):
    return render(request,'./user/userporfile.html')



# def addBook(request):
#     return render(request,'./admin/addbook.html')
