from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import include
from .import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('First',views.First,name='First'),
    path('team',views.team,name='team'),
    path('gallery',views.gallery,name='gallery'),
    path('startups',views.startups,name='startups'),
    path('join',views.join,name='join'),
    path('house',views.house,name='house'),
    path('contact',views.contact,name='contact'),
    path('ingenuity',views.ingenuity,name='ingenuity'),
]