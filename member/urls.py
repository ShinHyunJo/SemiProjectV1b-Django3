from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.list, name='join'),
    path('login/', views.view, name='login'),
    path('write/', views.write, name='write'),
]
