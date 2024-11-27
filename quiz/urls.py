
from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import render

urlpatterns = [
    path('questions/', views.get_questions, name='get_questions'),
    path('', lambda request: render(request, 'quiz.html'), name='quiz')
]
  