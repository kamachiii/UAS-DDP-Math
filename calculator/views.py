from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'views/index.html')

#* Aritmatika
def aritmatikaIndex(request):
    return render(request, 'views/aritmatika/index.html')

#* Bangun Datar
def bangunDatarIndex(request):
    return render(request, 'views/bangunDatar/index.html')

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
def bangunRuangBalok(request):
    if request.method == 'POST':
        if 'panjang' in request.POST and request.POST['panjang'] != '' and 'lebar' in request.POST and request.POST['lebar'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '':
            panjang = int(request.POST['panjang'])
            lebar = int(request.POST['lebar'])
            tinggi = int(request.POST['tinggi'])
            volume = volume_balok(panjang, lebar, tinggi)
            luas_permukaan = luas_permukaan_balok(panjang, lebar, tinggi)
            keliling = keliling_balok(panjang, lebar, tinggi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/balok?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/balok.html')
    return render(request, 'views/bangunRuang/balok.html', {
        'panjang': panjang,
        'lebar': lebar,
        'tinggi': tinggi,
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

# 2 Rumus Bangun Ruang Balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi
def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
def keliling_balok(panjang, lebar, tinggi):
    return 4 * (panjang + lebar + tinggi)
# End of Rumus Bangun Ruang Balok

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
