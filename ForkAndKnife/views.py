from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm

from .models import Menu, SubCategory
# Create your views here.

# def index(request:
    # menus = Menu.objects.all)
    # return render(request, "ForkAndKnife/index.html", {'menuss': menus)

# Define a view function to display the home page
def index(request):
    # Get all the Menu objects from the database
    menus = Menu.objects.all()
    
    # Render the index.html template with the menus as context
    return render(request, "ForkAndKnife/index.html", {'menuss': menus})

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('homePage')
        else:
            messages.error(request, 'Login failed. Please try again.')
            #error_message = 'Invalid username or password.'
            #return render(request, "ForkAndKnife/signin.html", {'error_message': error_message})
    #else:
     #   return render(request, 'ForkAndKnife/signin.html')
    return render(request, "ForkAndKnife/signin.html")

# def signup(request):
    # if request.method == 'POST':
        # form = CustomUserCreationForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return redirect('loginPage')
    # else:
        # form = CustomUserCreationForm()
    # return render(request, 'ForkAndKnife/joinnow.html', {'form': form})
# 
    #return render(request, "ForkAndKnife/joinnow.html")

# Define a view function to handle user registration
def signup(request):
    
    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Create a new instance of the CustomUserCreationForm using the form data
        form = CustomUserCreationForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the user to the database
            form.save()
            
            # Redirect to the login page
            return redirect('loginPage')
    
    # If the request method is not POST, display an empty form
    else:
        form = CustomUserCreationForm()
    
    # Render the joinnow.html template with the form
    return render(request, 'ForkAndKnife/joinnow.html', {'form': form})


def logoutview(request):
    logout(request)
    return redirect('indexPage')

'''
#@login_required
def home(request):
    if request.user.is_authenticated:
        menus = Menu.objects.all()
        return render(request, 'ForkAndKnife/home.html',{'menuss': menus})
    else:
        return redirect('loginPage') '''

def home(request):
    menus = Menu.objects.all()
    return render(request, 'ForkAndKnife/home.html',{'menuss': menus})


def menu(request):
    return render(request, "ForkAndKnife/menu.html")

def about(request):
    return render(request, 'ForkAndKnife/about.html')

# def profile(request,username):
    # user = get_object_or_404(User, username=username)
    # profile = get_object_or_404(User, user=user)
    # context = {'user': user, 'profile': profile}
    # return render(request, "ForkAndKnife/profile.html",context)

def profile(request):
    return render(request, 'ForkAndKnife/profile.html')


def menuList(request):
    obj = SubCategory.objects.all()
    menus = Menu.objects.all()

    return render(request, "ForkAndKnife/menulist.html", {'objj': obj , 'menuss': menus})


def order(request):
    return render(request, "ForkAndKnife/orderMenu.html")