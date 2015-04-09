from django.contrib import auth
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from main.models import Message


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if User.objects.filter(username=username):
            return render(request, 'main/register.html',
                    {'errors': 'This username is already taken'})

        elif len(username) < 3:
            return render(request, 'main/register.html',
                    {'errors': 'User name should contain at least'
                        ' 3 characters'})

        elif len(password) < 3:
            return render(request, 'main/register.html',
                    {'errors': 'Password should contain at least'
                        ' 3 characters'})

        user = User.objects.create_user(username=username, password=password)

        if user:
            user = auth.authenticate(username=username, password=password)
            auth.login(request,user)
            return HttpResponseRedirect("/forum")

        return render(request, str(user))
    else:
        return render(request, 'main/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/forum")
        else:
            return render(request, 'main/login.html',
                    {'errors': 'Wrong user name or password'})
    else:
        return render(request, 'main/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def forum(request):
    if request.method == 'POST':
        message = Message(
                text=request.POST['message'],
                author=request.user,
                date=timezone.now())
        message.save()
        return HttpResponseRedirect("/forum") # Helps refreshing
    messages = Message.objects.all()
    return render(request, 'main/forum.html', {'messages': messages})

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/forum")
    else:
        return HttpResponseRedirect("/login")
