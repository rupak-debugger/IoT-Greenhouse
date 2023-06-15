from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def form(request):
    return render(request, 'form.html')


def logout_user(request):
    logout(request)

    return redirect('/')


def login_user(request):
    if request.method == 'POST':
        user = authenticate(request,
                            email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Enter Valid Credentials')
            return redirect("form")

    else:
        messages.error(request, 'Use Post Request')
        return redirect("form")
