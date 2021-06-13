from django.urls import path

from . import  views

urlpatterns =[

    path('',views.Home , name=''),
    path('LoginForm',views.Login , name='Login')
]