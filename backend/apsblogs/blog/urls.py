from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('account/', include('account.urls')),
    path('categories', views.category, name='categories'),
    path('createblog', views.c_blog, name='c_blog'),
]
