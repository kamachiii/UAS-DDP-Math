from django.shortcuts import render
from django.http import HttpResponseRedirect
import math

def index(request):
    return render(request, 'views/index.html')

#* Aritmatika
def aritmatikaIndex(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operator = request.POST.get('operator')
        if operator == '+':
            hasil = int(num1) + int(num2)
        elif operator == '-':
            hasil = int(num1) - int(num2)
        elif operator == 'x':
            hasil = int(num1) * int(num2)
        elif operator == ':':
            hasil = int(num1) / int(num2)
        return render(request, 'views/aritmatika/index.html', {"num1" : num1, "num2" : num2, "operator" : operator, "hasil" : hasil})
    return render(request, 'views/aritmatika/index.html')

#* Bangun Datar
def bangunDatarIndex(request):
    return render(request, 'views/bangun-datar/index.html')

def bangunDatarPersegi(request):
    if request.method == 'POST':
        if 'sisi' in request.POST and request.POST['sisi'] != '':
            sisi = int(request.POST['sisi'])
            luas = luas_persegi(sisi)
            keliling = keliling_persegi(sisi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-datar/persegi?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-datar/persegi.html')
    return render(request, 'views/bangun-datar/persegi.html', {
        'sisi': sisi,
        'luas': luas,
        'keliling': keliling
    })

def luas_persegi(sisi):
    return sisi * sisi
def keliling_persegi(sisi):
    return 4 * sisi

def bangunDatarPersegiPanjang(request):
    if request.method == 'POST':
        if 'panjang' in request.POST and request.POST['panjang'] != '' and 'lebar' in request.POST and request.POST['lebar'] != '':
            panjang = int(request.POST['panjang'])
            lebar = int(request.POST['lebar'])
            luas = luas_persegi_panjang(panjang, lebar)
            keliling = keliling_persegi_panjang(panjang, lebar)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-datar/persegi-panjang?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-datar/persegiPanjang.html')
    return render(request, 'views/bangun-datar/persegiPanjang.html', {
        'panjang': panjang,
        'lebar': lebar,
        'luas': luas,
        'keliling': keliling
    })

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar
def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def bangunDatarSegitiga(request):
    if request.method == 'POST':
        if 'alas' in request.POST and request.POST['alas'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '' and 'sisi1' in request.POST and request.POST['sisi1'] != '' and 'sisi2' in request.POST and request.POST['sisi2'] != '' and 'sisi3' in request.POST and request.POST['sisi3'] != '':
            alas = int(request.POST['alas'])
            tinggi = int(request.POST['tinggi'])
            sisi1 = int(request.POST['sisi1'])
            sisi2 = int(request.POST['sisi2'])
            sisi3 = int(request.POST['sisi3'])
            luas = luas_segitiga(alas, tinggi)
            keliling = keliling_segitiga(sisi1, sisi2, sisi3)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-datar/segitiga?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-datar/segitiga.html')
    return render(request, 'views/bangun-datar/segitiga.html', {
        'alas': alas,
        'tinggi': tinggi,
        'sisi1': sisi1,
        'sisi2': sisi2,
        'sisi3': sisi3,
        'luas': luas,
        'keliling': keliling
    })

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def bangunDatarLingkaran(request):
    if request.method == 'POST':
        if 'jari_jari' in request.POST and request.POST['jari_jari'] != '':
            jari_jari = int(request.POST['jari_jari'])
            luas = luas_lingkaran(jari_jari)
            keliling = keliling_lingkaran(jari_jari)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-datar/lingkaran?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-datar/lingkaran.html')
    return render(request, 'views/bangun-datar/lingkaran.html', {
        'jari_jari': jari_jari,
        'luas': luas,
        'keliling': keliling
    })
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari ** 2
def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

def bangunDatarJajarGenjang(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            if rumus == '1':
                alas = int(request.POST['alas'])
                tinggi = int(request.POST['tinggi'])
                hasil = luas_jajar_genjang(alas, tinggi)
                return render(request, 'views/bangun-datar/jajarGenjang.html', {
                    'alas': alas,
                    'tinggi': tinggi,
                    'hasil': hasil
                })
            elif rumus == '2':
                sisi1 = int(request.POST['sisi1'])
                sisi2 = int(request.POST['sisi2'])
                hasil = keliling_jajar_genjang(sisi1, sisi2)
                return render(request, 'views/bangun-datar/jajarGenjang.html', {
                    'sisi1': sisi1,
                    'sisi2': sisi2,
                    'hasil': hasil
                })
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-datar/jajar-genjang?message=Please fill the form'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-datar/jajar-genjang?message=Please fill the form'))
    return render(request, 'views/bangun-datar/jajarGenjang.html')

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi
def keliling_jajar_genjang(sisi1, sisi2):
    return 2 * (sisi1 + sisi2)

def bangunDatarTrapesium(request):
    if request.method == 'POST':
        if 'alas1' in request.POST and request.POST['alas1'] != '' and 'alas2' in request.POST and request.POST['alas2'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '' and 'sisi1' in request.POST and request.POST['sisi1'] != '' and 'sisi2' in request.POST and request.POST['sisi2'] != '':
            alas1 = int(request.POST['alas1'])
            alas2 = int(request.POST['alas2'])
            tinggi = int(request.POST['tinggi'])
            sisi1 = int(request.POST['sisi1'])
            sisi2 = int(request.POST['sisi2'])
            luas = luas_trapesium(alas1, alas2, tinggi)
            keliling = keliling_trapesium(sisi1, sisi2, alas1, alas2)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-datar/trapesium?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-datar/trapesium.html')
    return render(request, 'views/bangun-datar/trapesium.html', {
        'alas1': alas1,
        'alas2': alas2,
        'tinggi': tinggi,
        'sisi1': sisi1,
        'sisi2': sisi2,
        'luas': luas,
        'keliling': keliling
    })
def luas_trapesium(alas1, alas2, tinggi):
    return 0.5 * (alas1 + alas2) * tinggi
def keliling_trapesium(sisi1, sisi2, alas1, alas2):
    return sisi1 + sisi2 + alas1 + alas2

#* Bangun Ruang
def bangunRuangIndex(request):
    return render(request, 'views/bangun-ruang/index.html')

# 1 Rumus Bangun Ruang Kubus
def bangunRuangKubus(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            if rumus == '1':
                sisi = int(request.POST['sisiVolume'])
                hasil = volume_kubus(sisi)
            elif rumus == '2':
                sisi = int(request.POST['sisiLuasPermukaan'])
                hasil = luas_permukaan_kubus(sisi)
            return render(request, 'views/bangun-ruang/kubus.html', {"rumus" : rumus, "sisi" : sisi, "hasil" : hasil})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/kubus?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/kubus.html')
def volume_kubus(sisi):
    return sisi ** 3
def luas_permukaan_kubus(sisi):
    return 6 * sisi ** 2
# End of Rumus Bangun Ruang Kubus

# 2 Rumus Bangun Ruang Balok
def bangunRuangBalok(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            panjang = int(request.POST['panjang'])
            lebar = int(request.POST['lebar'])
            tinggi = int(request.POST['tinggi'])
            if rumus == '1':
                hasil = volume_balok(panjang, lebar, tinggi)
            elif rumus == '2':
                hasil = luas_permukaan_balok(panjang, lebar, tinggi)
            return render(request, 'views/bangun-ruang/balok.html', {"rumus" : rumus, "panjang" : panjang, "lebar" : lebar, "tinggi" : tinggi, "hasil" : hasil})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/balok?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/balok.html')
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi
def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
# End of Rumus Bangun Ruang Balok

# 3.1 Rumus Bangun Ruang Prisma Segitiga
def bangunRuangPrismaSegitiga(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            alasSegitiga = int(request.POST['alasSegitiga'])
            tinggiSegitiga = int(request.POST['tinggiSegitiga'])
            tinggiPrisma = int(request.POST['tinggiPrisma'])
            if rumus == '1':
                hasil = volume_prisma_segitiga(alasSegitiga, tinggiSegitiga, tinggiPrisma)
            elif rumus == '2':
                hasil = luas_permukaan_prisma_segitiga(alasSegitiga, tinggiSegitiga, tinggiPrisma)
            return render(request, 'views/bangun-ruang/prisma/prismaSegitiga.html', {"rumus" : rumus, "alasSegitiga" : alasSegitiga, "tinggiSegitiga" : tinggiSegitiga, "tinggiPrisma" : tinggiPrisma, "hasil" : hasil})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/prisma/segitiga?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/prisma/prismaSegitiga.html')
def volume_prisma_segitiga(alas, tinggi, tinggi_prisma):
    return (1/2) * alas * tinggi * tinggi_prisma
def luas_permukaan_prisma_segitiga(alas, tinggi, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi
    sisi_miring = math.sqrt(alas**2 + tinggi**2)
    keliling_alas = alas + tinggi + sisi_miring
    luas_selimut = keliling_alas * tinggi_prisma
    luas_permukaan = 2 * luas_alas + luas_selimut
    return luas_permukaan
# End of Rumus Bangun Ruang Prisma segitiga

# 3.2 Rumus Bangun Ruang Prisma Segiempat
def bangunRuangPrismaSegiempat(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            panjang_segiempat = int(request.POST['panjangSegiempat'])
            lebar_segiempat = int(request.POST['lebarSegiempat'])
            tinggi_prisma = int(request.POST['tinggiPrisma'])
            if rumus == '1':
                hasil = volume_prisma_segiempat(panjang_segiempat, lebar_segiempat, tinggi_prisma)
            elif rumus == '2':
                hasil = luas_permukaan_prisma_segiempat(panjang_segiempat, lebar_segiempat, tinggi_prisma)
            return render(request, 'views/bangun-ruang/prisma/prismaSegiempat.html', {"rumus" : rumus, "panjangSegiempat" : panjang_segiempat, "tinggiSegiempat" : lebar_segiempat, "tinggiPrisma" : tinggi_prisma, "hasil" : round(hasil,2)})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/prisma/segiempat?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/prisma/prismaSegiempat.html')
def volume_prisma_segiempat(panjang, lebar, tinggi_prisma):
    return panjang * lebar * tinggi_prisma
def luas_permukaan_prisma_segiempat(panjang, lebar, tinggi_prisma):
    luas_alas = panjang * lebar
    keliling_alas = 2 * (panjang + lebar)
    luas_selimut = keliling_alas * tinggi_prisma
    return 2 * luas_alas + luas_selimut
# End of Rumus Bangun Ruang Prisma segiempat

# 3.3 Rumus Bangun Ruang Prisma Segilima
# End of Rumus Bangun Ruang Prisma segilima

# 3.4 Rumus Bangun Ruang Prisma Segienam
def bangunRuangPrismaSegienam(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            sisiSegienam = int(request.POST['sisiSegienam'])
            tinggi_prisma = int(request.POST['tinggiPrisma'])
            if rumus == '1':
                hasil = volume_prisma_segienam(sisiSegienam, tinggi_prisma)
            elif rumus == '2':
                hasil = luas_permukaan_prisma_segienam(sisiSegienam, tinggi_prisma)
            return render(request, 'views/bangun-ruang/prisma/prismaSegienam.html', {"rumus" : rumus, "sisiSegienam" : sisiSegienam, "tinggiPrisma" : tinggi_prisma, "hasil" : round(hasil,2)})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/prisma/segienam?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/prisma/prismaSegienam.html')
def volume_prisma_segienam(sisiSegienam, tinggi_prisma):
    luas_alas = (3 * math.sqrt(3) / 2) * (sisiSegienam ** 2)
    return luas_alas * tinggi_prisma
def luas_permukaan_prisma_segienam(sisiSegienam, tinggi_prisma):
    luas_alas = (3 * math.sqrt(3) / 2) * (sisiSegienam ** 2)
    keliling_alas = 6 * sisiSegienam
    luas_sisi_tegak = keliling_alas * tinggi_prisma
    return (2 * luas_alas) + luas_sisi_tegak
# End of Rumus Bangun Ruang Prisma

# 4 Rumus Bangun Ruang Tabung
def bangunRuangTabung(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            jari_jari = int(request.POST['jari_jari'])
            tinggi = int(request.POST['tinggi'])
            if rumus == '1':
                hasil = volume_tabung(jari_jari, tinggi)
            elif rumus == '2':
                hasil = luas_permukaan_tabung(jari_jari, tinggi)
            return render(request, 'views/bangun-ruang/tabung.html', {"rumus" : rumus, "jari_jari" : jari_jari, "tinggi" : tinggi, "hasil" : round(hasil,2)})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/tabung?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/tabung.html')
def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi
def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)
# End of Rumus Bangun Ruang Tabung

# 5.1 Rumus Bangun Ruang Limas Segitiga
def bangunRuangLimasSegitiga(request):
    if request.method == 'POST':
        if 'alas' in request.POST and request.POST['alas'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '':
            alas = int(request.POST['alas'])
            tinggi = int(request.POST['tinggi'])
            volume = volume_limas_segitiga(alas, tinggi)
            luas_permukaan = luas_permukaan_limas_segitiga(alas, tinggi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/limas/segitiga?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/limas/limasSegitiga.html')
    return render(request, 'views/bangun-ruang/limas/limasSegitiga.html', {
        'alas': alas,
        'tinggi': tinggi,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
    })
def luas_permukaan_limas_segitiga(alas, tinggi_alas, sisi_miring, tinggi_limas):
    luas_alas = (1/2) * alas * tinggi_alas
    luas_selimut = 3 * (1/2) * sisi_miring * tinggi_limas
    return luas_alas + luas_selimut
def volume_limas_segitiga(alas, tinggi_alas, tinggi_limas):
    return (1/3) * (1/2) * alas * tinggi_alas * tinggi_limas
# End of Rumus Bangun Ruang Limas Segitiga

# 5.2 Rumus Bangun Ruang Limas Segiempat
def bangunRuangLimasSegiempat(request):
    if request.method == 'POST':
        if 'alas' in request.POST and request.POST['alas'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '':
            alas = int(request.POST['alas'])
            tinggi = int(request.POST['tinggi'])
            volume = volume_limas_segiempat(alas, tinggi)
            luas_permukaan = luas_permukaan_limas_segiempat(alas, tinggi)
            keliling = keliling_limas_segiempat(alas, tinggi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/limas/segiempat?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/limas/limasSegiempat.html')
    return render(request, 'views/bangun-ruang/limas/limasSegiempat.html', {
        'alas': alas,
        'tinggi': tinggi,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
def volume_limas_segiempat(alas, tinggi):
    return (1/3) * alas * tinggi
def luas_permukaan_limas_segiempat(alas, tinggi):
    return (alas + (2 * alas * tinggi))
def keliling_limas_segiempat(alas, tinggi):
    return 4 * (alas + tinggi)
# End of Rumus Bangun Ruang Limas Segiempat

# 5.3 Rumus Bangun Ruang Limas Segilima
def bangunRuangLimasSegilima(request):
    if request.method == 'POST':
        if 'alas' in request.POST and request.POST['alas'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '':
            alas = int(request.POST['alas'])
            tinggi = int(request.POST['tinggi'])
            volume = volume_limas_segilima(alas, tinggi)
            luas_permukaan = luas_permukaan_limas_segilima(alas, tinggi)
            keliling = keliling_limas_segilima(alas, tinggi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/limas/segilima?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/limas/limasSegilima.html')
    return render(request, 'views/bangun-ruang/limas/limasSegilima.html', {
        'alas': alas,
        'tinggi': tinggi,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
def volume_limas_segilima(alas, tinggi):
    return (1/3) * (5/2) * alas * tinggi
def luas_permukaan_limas_segilima(alas, tinggi):
    return (alas + (5 * alas * tinggi))
def keliling_limas_segilima(alas, tinggi):
    return 5 * (alas + tinggi)
# End of Rumus Bangun Ruang Limas Segilima

# 5.4 Rumus Bangun Ruang Limas Segienam
def bangunRuangLimasSegienam(request):
    if request.method == 'POST':
        if 'alas' in request.POST and request.POST['alas'] != '' and 'tinggi' in request.POST and request.POST['tinggi'] != '':
            alas = int(request.POST['alas'])
            tinggi = int(request.POST['tinggi'])
            volume = volume_limas_segienam(alas, tinggi)
            luas_permukaan = luas_permukaan_limas_segienam(alas, tinggi)
            keliling = keliling_limas_segienam(alas, tinggi)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/limas/segiempat?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/limas/limasSegienam.html')
    return render(request, 'views/bangun-ruang/limas/limasSegienam.html', {
        'alas': alas,
        'tinggi': tinggi,
        'volume': volume,
        'luas_permukaan': luas_permukaan,
        'keliling': keliling
    })
def volume_limas_segienam(alas, tinggi):
    return (1/3) * (3 * math.sqrt(3) / 2) * alas * tinggi
def luas_permukaan_limas_segienam(alas, tinggi):
    return (alas + (3 * math.sqrt(3) / 2) * alas * tinggi)
def keliling_limas_segienam(alas, tinggi):
    return 6 * (alas + tinggi)
# End of Rumus Bangun Ruang Limas

# 6 Rumus Bangun Ruang Kerucut
def bangunRuangKerucut(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            jari_jari = int(request.POST['jari_jari'])
            tinggi = int(request.POST['tinggi'])
            if rumus == '1':
                hasil = volume_kerucut(jari_jari, tinggi)
            elif rumus == '2':
                hasil = luas_permukaan_kerucut(jari_jari, tinggi)
            return render(request, 'views/bangun-ruang/kerucut.html', {"rumus" : rumus, "jari_jari" : jari_jari, "tinggi" : tinggi, "hasil" : round(hasil,2)})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/kerucut?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/kerucut.html')
def volume_kerucut(jari_jari, tinggi):
    return (1/3) * math.pi * jari_jari ** 2 * tinggi
def luas_permukaan_kerucut(jari_jari, tinggi):
    return math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari ** 2 + tinggi ** 2))
# End of Rumus Bangun Ruang Kerucut

# 7 Rumus Bangun Ruang Bola
def bangunRuangBola(request):
    if request.method == 'POST':
        if 'rumus' in request.POST and request.POST['rumus'] != '':
            rumus = request.POST['rumus']
            jari_jari = int(request.POST['jari_jari'])
            if rumus == '1':
                hasil = volume_bola(jari_jari)
            elif rumus == '2':
                hasil = luas_permukaan_bola(jari_jari)
            return render(request, 'views/bangun-ruang/bola.html', {"rumus" : rumus, "jari_jari" : jari_jari, "hasil" : round(hasil,2)})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/bangun-ruang/bola?message=Please fill the form'))
    else:
        return render(request, 'views/bangun-ruang/bola.html')
def volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3
def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari ** 2
# End of Rumus Bangun Ruang Bola

# End of Bangun Ruang

#* Konversi
def konversiIndex(request):
    return render(request, 'views/konversi/index.html')

def konversiSuhu(request):
    if request.method == 'POST':
        if 'suhu' in request.POST and request.POST['suhu'] != '' and 'from' in request.POST and request.POST['from'] != '' and 'to' in request.POST and request.POST['to'] != '':
            suhu = float(request.POST['suhu'])
            from_unit = request.POST['from']
            to_unit = request.POST['to']
            hasil = konversi_suhu(suhu, from_unit, to_unit)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/konversi/suhu?message=Please fill the form'))
    else:
        return render(request, 'views/konversi/suhu.html')
    return render(request, 'views/konversi/suhu.html', {
        'suhu': suhu,
        'from': from_unit,
        'to': to_unit,
        'hasil': hasil
    })

def konversiPanjang(request):
    if request.method == 'POST':
        if 'panjang' in request.POST and request.POST['panjang'] != '' and 'from' in request.POST and request.POST['from'] != '' and 'to' in request.POST and request.POST['to'] != '':
            panjang = float(request.POST['panjang'])
            from_unit = request.POST['from']
            to_unit = request.POST['to']
            hasil = konversi_panjang(panjang, from_unit, to_unit)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/konversi/panjang?message=Please fill the form'))
    else:
        return render(request, 'views/konversi/panjang.html')
    return render(request, 'views/konversi/panjang.html', {
        'panjang': panjang,
        'from': from_unit,
        'to': to_unit,
        'hasil': hasil
    })

def konversiBerat(request):
    if request.method == 'POST':
        if 'berat' in request.POST and request.POST['berat'] != '' and 'from' in request.POST and request.POST['from'] != '' and 'to' in request.POST and request.POST['to'] != '':
            berat = float(request.POST['berat'])
            from_unit = request.POST['from']
            to_unit = request.POST['to']
            hasil = konversi_berat(berat, from_unit, to_unit)
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/konversi/berat?message=Please fill the form'))
    else:
        return render(request, 'views/konversi/berat.html')
    return render(request, 'views/konversi/berat.html', {
        'berat': berat,
        'from': from_unit,
        'to': to_unit,
        'hasil': hasil
    })

#* Fungsi Konversi
def konversi_suhu(suhu, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (suhu * 9/5) + 32
        elif to_unit == 'kelvin':
            return suhu + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (suhu - 32) * 5/9
        elif to_unit == 'kelvin':
            return (suhu - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return suhu - 273.15
        elif to_unit == 'fahrenheit':
            return (suhu - 273.15) * 9/5 + 32
    return suhu

def konversi_panjang(panjang, from_unit, to_unit):
    conversion_factors = {
        'kilometer': 1000,
        'hektometer': 100,
        'dekameter': 10,
        'meter': 1,
        'desimeter': 0.1,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mil': 1609.34,
        'yard': 0.9144,
        'kaki': 0.3048,
        'inci': 0.0254
    }
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return panjang * conversion_factors[from_unit] / conversion_factors[to_unit]
    return panjang

def konversi_berat(berat, from_unit, to_unit):
    conversion_factors = {
        'ton': 1000,
        'kwintal': 100,
        'kilogram': 1,
        'hektogram': 0.1,
        'dekagram': 0.01,
        'gram': 0.001,
        'desigram': 0.0001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ons': 0.0283495
    }
    if from_unit in conversion_factors and to_unit in conversion_factors:
        return berat * conversion_factors[from_unit] / conversion_factors[to_unit]
    return berat


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
