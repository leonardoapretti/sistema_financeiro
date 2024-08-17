from django.shortcuts import render
from django.http import HttpResponse
from .forms.lancamento_form import LancamentoForm

# Create your views here.

from .models import Lancamento


def home(request):
    lancamentos = Lancamento.objects.all()

    form = LancamentoForm(request.POST or None, request.FILES or None)

    contexto = {
        'form': form
    }
    return render(request, 'lancamentos/home.html', context=contexto)
