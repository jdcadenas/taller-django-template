from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.index, name='login'),
    #path('', views.index, name='index'),
]
