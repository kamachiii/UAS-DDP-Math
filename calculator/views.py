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

def bangunRuangPrismaSegitiga(request):
    if request.method == 'POST':
        if ' alas_segitiga' in request.POST and request.POST[' alas_segitiga'] != '' and 'tinggi_segitiga' in request.POST and request.POST['tinggi_segitiga'] != '' and 'tinggi_prisma' in request.POST and request.POST['tinggi_prisma'] != '':
            alas_segitiga = int(request.POST[' alas_segitiga'])
            tinggi_segitiga = int(request.POST['tinggi_segitiga'])
            tinggi_prisma = int(request.POST['tinggi_prisma'])
            volume = volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)
            luas_permukaan = luas_permukaan_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)
            keliling = keliling_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/prisma/segitiga?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/prisma/prismaSegitiga.html')
    return render(request, 'views/bangunRuang/prisma/prismaSegitiga.html', {
        'alas_segitiga': alas_segitiga,
        'tinggi_segitiga': tinggi_segitiga,
        'tinggi_prisma': tinggi_prisma,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
    
def bangunRuangPrismaSegiempat(request):
    if request.method == 'POST':
        if ' alas_segiempat' in request.POST and request.POST[' alas_segiempat'] != '' and 'tinggi_segiempat' in request.POST and request.POST['tinggi_segiempat'] != '' and 'tinggi_prisma' in request.POST and request.POST['tinggi_prisma'] != '':
            alas_segiempat = int(request.POST[' alas_segiempat'])
            tinggi_segiempat = int(request.POST['tinggi_segiempat'])
            tinggi_prisma = int(request.POST['tinggi_prisma'])
            volume = volume_prisma_segiempat(alas_segiempat, tinggi_segiempat, tinggi_prisma)
            luas_permukaan = luas_permukaan_prisma_segiempat(alas_segiempat, tinggi_segiempat, tinggi_prisma)
            keliling = keliling_prisma_segiempat(alas_segiempat, tinggi_segiempat, tinggi_prisma)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/prisma/segiempat?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/prisma/prismaSegiempat.html')
    return render(request, 'views/bangunRuang/prisma/prismaSegiempat.html', {
        'alas_segiempat': alas_segiempat,
        'tinggi_segiempat': tinggi_segiempat,
        'tinggi_prisma': tinggi_prisma,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
    
def bangunRuangPrismaSegilima(request):
    if request.method == 'POST':
        if ' alas_segilima' in request.POST and request.POST[' alas_segilima'] != '' and 'tinggi_segilima' in request.POST and request.POST['tinggi_segilima'] != '' and 'tinggi_prisma' in request.POST and request.POST['tinggi_prisma'] != '':
            alas_segilima = int(request.POST[' alas_segilima'])
            tinggi_segilima = int(request.POST['tinggi_segilima'])
            tinggi_prisma = int(request.POST['tinggi_prisma'])
            volume = volume_prisma_segilima(alas_segilima, tinggi_segilima, tinggi_prisma)
            luas_permukaan = luas_permukaan_prisma_segilima(alas_segilima, tinggi_segilima, tinggi_prisma)
            keliling = keliling_prisma_segilima(alas_segilima, tinggi_segilima, tinggi_prisma)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/prisma/segilima?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/prisma/prismaSegilima.html')
    return render(request, 'views/bangunRuang/prisma/prismaSegilima.html', {
        'alas_segilima': alas_segilima,
        'tinggi_segilima': tinggi_segilima,
        'tinggi_prisma': tinggi_prisma,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
    
def bangunRuangPrismaSegienam(request):
    if request.method == 'POST':
        if ' alas_segienam' in request.POST and request.POST[' alas_segienam'] != '' and 'tinggi_segienam' in request.POST and request.POST['tinggi_segienam'] != '' and 'tinggi_prisma' in request.POST and request.POST['tinggi_prisma'] != '':
            alas_segienam = int(request.POST[' alas_segienam'])
            tinggi_segienam = int(request.POST['tinggi_segienam'])
            tinggi_prisma = int(request.POST['tinggi_prisma'])
            volume = volume_prisma_segienam(alas_segienam, tinggi_segienam, tinggi_prisma)
            luas_permukaan = luas_permukaan_prisma_segienam(alas_segienam, tinggi_segienam, tinggi_prisma)
            keliling = keliling_prisma_segienam(alas_segienam, tinggi_segienam, tinggi_prisma)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/prisma/segienam?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/prisma/prismaSegienam.html')
    return render(request, 'views/bangunRuang/prisma/prismaSegienam.html', {
        'alas_segienam': alas_segienam,
        'tinggi_segienam': tinggi_segienam,
        'tinggi_prisma': tinggi_prisma,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
    
def bangunRuangTabung(request):
    if request.method == 'POST':
        if 'jari_jari' in request.POST and request.POST['jari_jari'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '':
            jari_jari = int(request.POST['jari_jari'])
            tinggi = int(request.POST['tinggi'])
            volume = volume_tabung(jari_jari, tinggi)
            luas_permukaan = luas_permukaan_tabung(jari_jari, tinggi)
            keliling = keliling_tabung(jari_jari, tinggi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/tabung?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/tabung.html')
    return render(request, 'views/bangunRuang/tabung.html', {
        'jari_jari': jari_jari,
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

# 3 Rumus Bangun Ruang Prisma
# 3.1 Prisma Segitiga
def volume_prisma_segitiga(alas, tinggi, tinggi_prisma):
    return (1/2) * alas * tinggi * tinggi_prisma
def luas_permukaan_prisma_segitiga(alas, tinggi, tinggi_prisma):
    return (alas * tinggi) + (3 * alas * tinggi_prisma)
def keliling_prisma_segitiga(alas, tinggi, tinggi_prisma):
    return 3 * (alas + tinggi + tinggi_prisma)

# 3.2 Prisma Segiempat
def volume_prisma_segiempat(alas, tinggi, tinggi_prisma):
    return (1/2) * alas * tinggi * tinggi_prisma
def luas_permukaan_prisma_segiempat(alas, tinggi, tinggi_prisma):
    return (2 * alas * tinggi) + (2 * alas * tinggi_prisma) + (2 * tinggi * tinggi_prisma)
def keliling_prisma_segiempat(alas, tinggi, tinggi_prisma):
    return 4 * (alas + tinggi + tinggi_prisma)

# 3.3 Prisma Segilima
def volume_prisma_segilima(alas, tinggi, tinggi_prisma):
    return (5/2) * alas * tinggi * tinggi_prisma
def luas_permukaan_prisma_segilima(alas, tinggi, tinggi_prisma):
    return (5 * alas * tinggi) + (5 * alas * tinggi_prisma)
def keliling_prisma_segilima(alas, tinggi, tinggi_prisma):
    return 5 * (alas + tinggi + tinggi_prisma)

# 3.4 Prisma Segienam
def volume_prisma_segienam(alas, tinggi, tinggi_prisma):
    return (3 * math.sqrt(3) / 2) * alas * tinggi * tinggi_prisma
def luas_permukaan_prisma_segienam(alas, tinggi, tinggi_prisma):
    return (3 * math.sqrt(3) / 2) * alas * tinggi + (6 * alas * tinggi_prisma)
def keliling_prisma_segienam(alas, tinggi, tinggi_prisma):
    return 6 * (alas + tinggi + tinggi_prisma)
# End of Rumus Bangun Ruang Prisma

# 4 Rumus Bangun Ruang Tabung
def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi
def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)
def keliling_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari
# End of Rumus Bangun Ruang Tabung

# 5 Rumus Bangun Ruang Limas
# 5.1 Limas Segitiga
def volume_limas_segitiga(alas, tinggi):
    return (1/3) * (1/2) * alas * tinggi
def luas_permukaan_limas_segitiga(alas, tinggi):
    return (alas + (3 * alas * tinggi))
def keliling_limas_segitiga(alas, tinggi):
    return 3 * (alas + tinggi)

# 5.2 Limas Segiempat
def volume_limas_segiempat(alas, tinggi):
    return (1/3) * alas * tinggi
def luas_permukaan_limas_segiempat(alas, tinggi):
    return (alas + (2 * alas * tinggi))
def keliling_limas_segiempat(alas, tinggi):
    return 4 * (alas + tinggi)

# 5.3 Limas Segilima
def volume_limas_segilima(alas, tinggi):
    return (1/3) * (5/2) * alas * tinggi
def luas_permukaan_limas_segilima(alas, tinggi):
    return (alas + (5 * alas * tinggi))
def keliling_limas_segilima(alas, tinggi):
    return 5 * (alas + tinggi)

# 5.4 Limas Segienam
def volume_limas_segienam(alas, tinggi):
    return (1/3) * (3 * math.sqrt(3) / 2) * alas * tinggi
def luas_permukaan_limas_segienam(alas, tinggi):
    return (alas + (3 * math.sqrt(3) / 2) * alas * tinggi)
def keliling_limas_segienam(alas, tinggi):
    return 6 * (alas + tinggi)
# End of Rumus Bangun Ruang Limas

# 6 Rumus Bangun Ruang Kerucut
def volume_kerucut(jari_jari, tinggi):
    return (1/3) * math.pi * jari_jari ** 2 * tinggi
def luas_permukaan_kerucut(jari_jari, tinggi):
    return math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari ** 2 + tinggi ** 2))
def keliling_kerucut(jari_jari, tinggi):
    return math.pi * jari_jari
# End of Rumus Bangun Ruang Kerucut

# 7 Rumus Bangun Ruang Bola
def volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3
def luas_permukaan_bola(jari_jari): 
    return 4 * math.pi * jari_jari ** 2
def keliling_bola(jari_jari):
    return 2 * math.pi * jari_jari
# End of Rumus Bangun Ruang Bola

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
