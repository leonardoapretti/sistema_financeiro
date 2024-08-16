from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'lancamentos/home.html', context={
        'nome': 'Leonardo dos Anjos Pretti'
    })
