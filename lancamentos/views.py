from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.lancamento_form import LancamentoForm
from .forms.login_form import LoginForm
from .forms.forms_teste import FormTeste
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

from .models import Lancamento


def login(request):
    if (request.user.is_authenticated):
        return redirect('lancamentos:home')

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            usuario_autenticado = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', ''),
            )
            print(usuario_autenticado)
            if usuario_autenticado is not None:
                messages.success(request, 'Bem-vindo!')
                login(request)
                return redirect('lancamentos:home')
            else:
                messages.error(request, 'Usuário ou senha incorretos!')

    form = LoginForm()
    contexto = {
        'form': form,
        'titulo': 'Login'
    }
    return render(request, 'lancamentos/login.html', context=contexto)


def home(request):
    # lancamentos = Lancamento.objects.all()
    print(request.user)
    form = LancamentoForm(request.POST or None, request.FILES or None)

    contexto = {
        'form': form,
        'titulo': 'teste'
    }
    return render(request, 'lancamentos/home.html', context=contexto)


def novo(request):
    form = LancamentoForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        form = LancamentoForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            lancamento = form.cleaned_data
            print(lancamento)
            form.save()

    contexto = {
        'form': form,
        'titulo': 'teste'
    }

    return render(request, 'lancamentos/novo.html', context=contexto)


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
