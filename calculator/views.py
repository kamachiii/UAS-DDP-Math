from django.shortcuts import render
from django.http import HttpResponseRedirect
import math

def index(request):
    return render(request, 'views/index.html')

#* Aritmatika
def aritmatikaIndex(request):
    return render(request, 'views/aritmatika/index.html')

#* Bangun Datar
def bangunDatarIndex(request):
    return render(request, 'views/bangunDatar/index.html')
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

#* Bangun Ruang
def bangunRuangIndex(request):
    return render(request, 'views/bangunRuang/index.html')
def bangunRuangKubus(request):
    if request.method == 'POST':
        if 'sisi' in request.POST and request.POST['sisi'] != '':
            sisi = int(request.POST['sisi'])
            volume = volume_kubus(sisi)
            luas_permukaan = luas_permukaan_kubus(sisi)
            keliling = keliling_kubus(sisi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/kubus?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/kubus.html')
    return render(request, 'views/bangunRuang/kubus.html', {
        'sisi': sisi,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
# 1 Rumus Bangun Ruang Kubus
def volume_kubus(sisi):
    return sisi ** 3
def luas_permukaan_kubus(sisi):
    return 6 * sisi ** 2
def keliling_kubus(sisi):
    return 12 * sisi
# End of Rumus Bangun Ruang Kubus

#* Konversi
def konversiIndex(request):
    return render(request, 'views/konversi/index.html')

#? Auth
def loginAction(request):
    if request.method == 'POST':
        if 'username' in request.POST and request.POST['username'] != '' and 'password' in request.POST and request.POST['password'] != '':
            username = request.POST['username']
            request.session['username'] = username
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/?message=Please fill the form'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/?message=Method Not Allowed'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def logoutAction(request):
    if 'username' in request.session:
        del request.session['username']
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/?message=Logout Success'))
