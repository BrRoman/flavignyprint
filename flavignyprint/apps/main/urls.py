""" apps/main/urls.py """

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
]
