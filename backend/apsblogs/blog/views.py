from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the index.")
    return render(request, 'index.html')
def about(request):
    # return HttpResponse("Hello, world. You're at the about.")
    return render(request, 'about.html')
def category(request):
    # return HttpResponse("Hello, world. You're at the c_blog.")
    return render(request, 'categories.html')
def c_blog(request):
    # return HttpResponse("Hello, world. You're at the c_blog.")
    return render(request, 'create_blog.html')
def blogHome(request):
    # return HttpResponse("Hello, world. You're at the BlogHome.")
    return render(request, 'blogHome.html')
def blogPost(request, slug):
    return HttpResponse(f"Hello, world. You're at the BlogPost.{slug}")
    # return render(request, 'create_blog.html')
