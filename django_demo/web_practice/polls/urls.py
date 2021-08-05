
from django.urls import path
from django.urls import include

from django_demo.web_practice.polls import views

urlpatterns = [
    path('', views.index, name='index'),
]