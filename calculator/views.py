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
