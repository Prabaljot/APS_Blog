from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blogpost', views.blogpost, name='blogpost'),
    path('account/', include('account.urls')),
    path('createblog', views.c_blog, name='c_blog'),
]
