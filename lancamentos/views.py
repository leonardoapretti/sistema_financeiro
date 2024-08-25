import pprint
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.lancamento_form import LancamentoForm
from .forms.login_form import LoginForm
from .forms.forms_teste import FormTeste
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from utils.print_c import print_c
# Create your views here.

from .models import Lancamento


def login_user(request):
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
                login(request, usuario_autenticado)
                messages.success(request, 'Bem-vindo!')
                return redirect('lancamentos:home')
            else:
                messages.error(request, 'Usuário ou senha incorretos!')

    form = LoginForm()
    contexto = {
        'form': form,
        'titulo': 'Login'
    }
    return render(request, 'lancamentos/login.html', context=contexto)

# redirect_field_name recebe a página que o usuário tentou acessar antes de estar logado, assim, ele será redirecionado para a página diretamente
# esse atributo é passado para a url


@login_required(login_url='lancamentos:login_user', redirect_field_name='next')
def logout_user(request):
    if request.user.username != request.user.username:
        messages.error(request, 'Resquisição inválida!')
        return redirect('lancamentos:login_user')
    logout(request)
    messages.success(request, 'Até mais!')
    return redirect('lancamentos:login_user')


@login_required(login_url='lancamentos:login_user', redirect_field_name='next')
def home(request):
    # lancamentos = Lancamento.objects.all()
    print(request.user)
    form = LancamentoForm(request.POST or None, request.FILES or None)

    contexto = {
        'form': form,
        'titulo': 'teste'
    }
    return render(request, 'lancamentos/pages/home.html', context=contexto)


@login_required(login_url='lancamentos:login_user', redirect_field_name='next')
def novo(request):
    if request.method == 'POST':
        POST = request.POST or None
        form = LancamentoForm(POST)
        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.id_usuario_ativo = request.user
            # print(lancamento)
            lancamento.save()

    form = LancamentoForm(request.POST or None)
    contexto = {
        'form': form,
        'titulo': 'teste'
    }

    return render(request, 'lancamentos/pages/novo.html', context=contexto)


@login_required(login_url='lancamentos:login_user', redirect_field_name='next')
def extrato(request):
    lancamentos = Lancamento.objects.all()

    totalizadores = {
        'valor_milena_pessoal': 0,
        'valor_leonardo_pessoal': 0,
        'valor_compartilhado': 0,
    }

    for lancamento in lancamentos:
        print(lancamento)
        valor = lancamento.valor_total
        print(lancamento.id_usuario_titular)
        print(lancamento.compartilhado)

        # if lancamento.id_usuario_titular.username == 'leonardoapretti':
        #     print('entrou no nome')
        #     if lancamento.compartilhado == False:
        #         totalizadores['valor_leonardo_pessoal'] += valor

        # elif lancamento.id_usuario_titular == 2:
        #     print('entrou no nome')
        #     if lancamento.compartilhado == False:
        #         totalizadores['valor_milena_pessoal'] += valor

        match lancamento.id_usuario_titular.username:
            case 'basmore':
                if lancamento.compartilhado == False:
                    totalizadores['valor_milena_pessoal'] += valor
                    continue
            case 'leonardoapretti':
                if lancamento.compartilhado == False:
                    totalizadores['valor_leonardo_pessoal'] += valor
                    continue
        totalizadores['valor_compartilhado'] += valor
        totalizadores['valor_dividido'] = totalizadores['valor_compartilhado'] / 2

    print(totalizadores)
    contexto = {
        'lancamentos': lancamentos,
        'titulo': 'Extrato',
        'totalizadores': totalizadores
    }

    return render(request, 'lancamentos/pages/extrato.html', context=contexto)


def detalhes(request, id_lancamento):
    contexto = {
        'id_lancamento': id_lancamento
    }
    return render(request, 'lancamentos/pages/detalhes.html', contexto)


@login_required(login_url='lancamentos:login_user', redirect_field_name='next')
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
    return render(request, 'lancamentos/pages/testes.html', contexto)
