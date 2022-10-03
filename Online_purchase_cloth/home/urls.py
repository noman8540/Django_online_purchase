from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("men", views.men, name = 'men'),
    path("women", views.women, name = 'women'),
    path("login", views.login, name = 'login'),
    path("contact", views.contact, name = 'contact')
]