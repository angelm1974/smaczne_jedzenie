from django.shortcuts import render
from django.http import  Http404,HttpResponse
from .models import Producent, Surowiec, Produkt, Recenzja
# Create your views here.

def lista_producentow(request):

    
    producenci = Producent.objects.all()
    # lista=[p.nazwa for p in producenci]
    # return  HttpResponse(lista)
    return render(request, 'jedzonko/lista_producentow.html', {'producenci': producenci})

def pobierz_producenta(request, producent_id):
    try:
        producent = Producent.objects.get(pk=producent_id)
    except Producent.DoesNotExist:
        raise Http404("Producent nie istnieje")
    return render(request, 'jedzonko/producent.html', {'producent': producent})