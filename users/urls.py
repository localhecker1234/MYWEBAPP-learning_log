
'''Defines the url pattern for the users'''
from django.urls import path, include
from . import views
app_name = 'users'

urlpatterns=[
    path('', include('django.contrib.auth.urls')),
    #Regestration page
    path('register', views.register, name= 'register'),
    path('c_logout/', views.custom_logout, name='c_logout')
]