from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from HOME.models import*
from USER.models import *

# Create your views here.
def home_page(request):
    if request.session.has_key('name'):
        N = Registration.objects.get(Name = request.session['name'])
        h = Service.objects.all()
        return render(request, 'HOME/index.html', {'hom' : h, 'NAAM' : N })
    else:
        obj = Service.objects.all()
        return render(request, 'HOME/index.html', {'hom' : obj})

    

def service_page(request):
    if request.session.has_key('name'):
        ser = Registration.objects.get(Name = request.session['name'])
        obj = Service.objects.all()
        print(obj)
        return render(request, 'HOME/service.html',{'obj' : obj, 'serv' : ser } )
    else:
        return render(request, 'HOME/service.html')


def bath_page(request,pk):
    if request.session.has_key('name'):
        single = Registration.objects.get(Name = request.session['name'])
        pro = get_object_or_404(Service, pk=pk)
        return render(request, 'HOME/bathroom.html', {'p': pro, 'sing' : single })
    else:
        pro = get_object_or_404(Service, pk=pk)
        return render(request, 'HOME/bathroom.html', {'p': pro})


