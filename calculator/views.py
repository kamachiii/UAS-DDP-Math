from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    return render(request, 'views/bangunDatar/index.html')

#* Bangun Ruang
def bangunRuangIndex(request):
    return render(request, 'views/bangunRuang/index.html')

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
