"""
URL configuration for math_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from calculator.views import *

urlpatterns = [
    path('admin/', admin.site.urls), #* Path Admin

    path('', index, name="index"), #* Path Index

    #* Path Aritmatika
    path('aritmatika/', aritmatikaIndex, name="aritmatika-index"),

    #* Path Bangun Datar
    path('bangun-datar/', include([
        path('', bangunDatarIndex, name="bangunDatar-index"),
    ])),

    #* Path Bangun Ruang
    path('bangun-ruang/', include([
        path('', bangunRuangIndex, name="bangunRuang-index"),
        path('kubus', bangunRuangKubus, name="bangunRuang-kubus"),
        path('balok', bangunRuangBalok, name="bangunRuang-balok"),
    ])),

    #* Path Konversi
    path('konversi/', include([
        path('', konversiIndex, name="konversi-index"),
    ])),

    #? Auth
    path('login/', loginAction, name="login"),
    path('logout/', logoutAction, name="logout"),
]
