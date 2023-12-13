from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    return render(request, 'index.html')

# this is view is suppposed to count the number of words in the forms
def counter(request):
    posts = [1, 2, 3, 4, 5, 'Tim', 'Tom', 'John']
    # text = request.POST['text'] in render {'number': amt_of_words}
    # amt_of_words = len(text.split()) at html the nuber of words is {{number}}
    return render(request, 'counter.html', {'posts': posts})

def register(request):
    # we want to collect and save the signup details
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # this checks if email already in use 
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password doesnot match")
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # if user has an account
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect ('/')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})