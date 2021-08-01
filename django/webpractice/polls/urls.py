
from django.urls import path
from django.urls import include

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
]