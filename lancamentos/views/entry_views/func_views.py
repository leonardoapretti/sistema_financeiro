
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from lancamentos.forms.entry_form import EntryForm
from lancamentos.forms.login_form import LoginForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_not_required

# Create your views here.


@login_not_required
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
    return render(request, 'entries/pages/login.html', context=contexto)

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
    form = EntryForm(request.POST or None, request.FILES or None)

    contexto = {
        'form': form,
        'titulo': 'teste'
    }
    return render(request, 'entries/pages/home.html', context=contexto)


# @login_required(login_url='lancamentos:login_user', redirect_field_name='next')
# def novo(request):
#     if request.method == 'POST':
#         POST = request.POST or None
#         form = LancamentoForm(POST)
#         if form.is_valid():
#             lancamento = form.save(commit=False)
#             lancamento.id_usuario_ativo = request.user
#             lancamento.save()

#     form = LancamentoForm(request.POST or None)
#     contexto = {
#         'form': form,
#         'titulo': 'teste'
#     }

#     return render(request, 'lancamentos/pages/novo.html', context=contexto)


# @login_required(login_url='lancamentos:login_user', redirect_field_name='next')
# def extrato(request):
#     lancamentos = Entry.objects.all()

#     totalizadores = {
#         'valor_milena_pessoal': 0,
#         'valor_leonardo_pessoal': 0,
#         'valor_compartilhado': 0,
#     }

#     for lancamento in lancamentos:
#         valor = lancamento.valor_total

#         match lancamento.id_usuario_titular.username:
#             case 'basmore':
#                 if lancamento.compartilhado == False:
#                     totalizadores['valor_milena_pessoal'] += valor
#                     continue
#             case 'leonardoapretti':
#                 if lancamento.compartilhado == False:
#                     totalizadores['valor_leonardo_pessoal'] += valor
#                     continue
#         totalizadores['valor_compartilhado'] += valor
#         totalizadores['valor_dividido'] = totalizadores['valor_compartilhado'] / 2

#     contexto = {
#         'lancamentos': lancamentos,
#         'titulo': 'Extrato',
#         'totalizadores': totalizadores
#     }

#     return render(request, 'lancamentos/pages/extrato.html', context=contexto)


# def detalhes(request, id_lancamento):
#     contexto = {
#         'id_lancamento': id_lancamento
#     }
#     return render(request, 'lancamentos/pages/detalhes.html', contexto)


@login_required(login_url='lancamentos:login_user', redirect_field_name='next')
def testes(request):

    context = {}
    return render(request, 'entries/pages/testes.html', context)
