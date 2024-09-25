from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.watch, name='watch'),
    path('about/', views.about, name='about'),
    path('new/', views.new, name='new'),
    path('service/', views.service, name='service'),
    path('sports/', views.sports, name='sports')
]