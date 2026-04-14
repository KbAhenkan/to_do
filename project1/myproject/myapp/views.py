from django.shortcuts import render, redirect
# This is to import the List Form
from .forms import List, RegisterForm
# This is to import the ListModel
from .models import ListModel

# I am now About to import the stuff that will be needed for the Authentication part of the website

# For logins, logouts, and authentication
from django.contrib.auth import authenticate, login, logout
# The login_required decorator to protect views
from django.contrib.auth.decorators import login_required
# Importing User Class(model)
from django.contrib.auth.models import User

# Create your views here.

# The Register_view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           username = form.cleaned_data.get("username")
           password = form.cleaned_data.get("password")
           user = User.objects.create_user(username=username, password=password)
           login(request, user) 
           return redirect('home')
        else:
           return render(request, 'auth/register.html', {'form':form})
    else:
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form':form})

# The Login_view
def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'auth/login.html', {'error': error_message})

# The Logout_view
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

# Home View
# Using the decorator
@login_required
def home_view(request):
    return render(request, 'static/home.html')

# Create List View
def create_list(request):
    form = List()
    if request.method == "POST":
        form =  List(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'static/create_list.html', {'form':form})

# Show list View
def show_list(request):
    lists = ListModel.objects.all()
    return render(request, 'static/show_list.html', {'lists':lists})
    

# Delete View
def delete_view(request, Title):
    title = ListModel.objects.get(Title=Title)
    if request.method == 'POST':
        title.delete()
        return redirect('show_list')
    return render(request, 'static/confirm_delete.html', {'title':title})
