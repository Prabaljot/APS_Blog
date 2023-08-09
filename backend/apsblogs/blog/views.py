from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")
def about(request):
    return HttpResponse("Hello, world. You're at the about.")
def account(request):
    return HttpResponse("Hello, world. You're at the account.")
def c_blog(request):
    return HttpResponse("Hello, world. You're at the c_blog.")
def blogpost(request):
    return HttpResponse("Hello, world. You're at the blogpost.")
