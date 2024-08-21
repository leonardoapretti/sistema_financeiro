from django.shortcuts import render
from django.http import HttpResponse
from .forms.lancamento_form import LancamentoForm
from .forms.forms_teste import FormTeste
from django.urls import reverse


# Create your views here.

from .models import Lancamento


def home(request):
    lancamentos = Lancamento.objects.all()

    form = LancamentoForm(request.POST or None, request.FILES or None)

    contexto = {
        'form': form,
        # 'usuario': request.user.username,
        'lancamentos': lancamentos,

    }
    return render(request, 'lancamentos/home.html', context=contexto)


def testes(request):
    if request.method == 'POST':
        form = FormTeste(request.POST)
        if form.is_valid():
            # após o formulário passar pela validação inicial (is_valid()) os dados são distribuidos no dicionário cleaned_data para serem manipulados na view e validados de maneira mais específica
            print(form.cleaned_data['nome'])
            return HttpResponse('Obrigado')

    else:
        form = FormTeste()

    contexto = {'form': form,
                'form_action': reverse('lancamentos:testes'),
                'form_errors': form.errors

                }
    return render(request, 'lancamentos/testes.html', contexto)
