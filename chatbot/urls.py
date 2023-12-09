from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    path('chatbot_view/', views.chatbot_view, name='chatbot_view'),
    path('get_answer/', views.get_answer, name='get_answer'),
    
]