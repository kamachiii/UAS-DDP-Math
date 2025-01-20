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
    path('Bangun Ruang /', include([
        path('', bangunRuangIndex, name="bangunRuang-index"),
        path('Kubus', bangunRuangKubus, name="bangunRuang-kubus"),
        path('Balok', bangunRuangBalok, name="bangunRuang-balok"),
        path('Prisma Segitiga', bangunRuangPrismaSegitiga, name="bangunRuang-prisma-segitiga"),
        path('Prisma Segiempat', bangunRuangPrismaSegiempat, name="bangunRuang-prisma-segiempat"),
        path('Prisma Segilima', bangunRuangPrismaSegilima, name="bangunRuang-prisma-segilima"),
        path('Prisma Segienam', bangunRuangPrismaSegienam, name="bangunRuang-prisma-segienam"),
        path('Tabung', bangunRuangTabung, name="bangunRuang-tabung"),
        path('Limas Segitiga', bangunRuangLimasSegitiga, name="bangunRuang-limas-segitiga"),
        path('Limas Segiempat', bangunRuangLimasSegiempat, name="bangunRuang-limas-segiempat"),
        path('Limas Segilima', bangunRuangLimasSegilima, name="bangunRuang-limas-segilima"),
        path('Limas Segienam', bangunRuangLimasSegienam, name="bangunRuang-limas-segienam"),
        path('Kerucut', bangunRuangKerucut, name="bangunRuang-kerucut"),
        path('Bola', bangunRuangBola, name="bangunRuang-bola"),
    ])),

    #* Path Konversi
    path('konversi/', include([
        path('', konversiIndex, name="konversi-index"),
        path('suhu', konversiSuhu, name="konversi-suhu"),
        path('berat', konversiBerat, name="konversi-berat"),
        path('panjang', konversiPanjang, name="konversi-panjang"),
    ])),

    #? Auth
    path('login/', loginAction, name="login"),
    path('logout/', logoutAction, name="logout"),
]
