from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the index.")
    return render(request, 'index.html')
def about(request):
    # return HttpResponse("Hello, world. You're at the about.")
    return render(request, 'about.html')
def category(request):
    # return HttpResponse("Hello, world. You'rse at the c_blog.")
    return render(request, 'categories.html')
def c_blog(request):
    # return HttpResponse("Hello, world. You'rse at the c_blog.")
    return render(request, 'create_blog.html')
