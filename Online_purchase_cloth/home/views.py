from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def men(request):
    return HttpResponse("This is Men's clothing webpage.")

def women(request):
    return HttpResponse("This is Women's clothing webpage.")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credential
        user = authenticate(username= username, password= password)
        
        if user is not None:
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")