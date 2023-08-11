from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    # return HttpResponse("Hello, world. You're at the account.")
    return render(request, 'account.html')

def register(request):
    # return HttpResponse("Hello, world. You're at the account.")
    return render(request, 'account.html#register')
