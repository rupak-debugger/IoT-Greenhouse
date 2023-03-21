from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth

from accounts.models import Account

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            qdata = Account.objects.get(email=request.POST['email'])
            return HttpResponse("Hi! " + qdata.username)
        else:
            return HttpResponse("enter valid credentials")

    else:
        return HttpResponse("Please use POST method")
