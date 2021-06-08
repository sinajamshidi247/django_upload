from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        data = request.POST
        username = data["username"]
        password = data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "login successfully", "success")
        else:
            print("user not exist")
            messages.error(request, 'wrong username or password', 'warning')
            return redirect('accounts:home')
    else:
        None

    return render(request, "accounts/home.html")
