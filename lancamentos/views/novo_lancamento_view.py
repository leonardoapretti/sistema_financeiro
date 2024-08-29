from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from lancamentos.forms.lancamento_form import LancamentoForm


class NovoLancamentoView(View):
    def get(self, request):
        form = LancamentoForm()
        contexto = {
            'form': form,
            'titulo': 'teste'
        }

        return render(request, 'lancamentos/pages/novo.html', context=contexto)

    def post(self, request):
        POST = request.POST or None
        form = LancamentoForm(POST)
        if form.is_valid():
            lancamento = form.save(commit=False)
            lancamento.id_usuario_ativo = request.user
            # print(lancamento)
            lancamento.save()
            messages.success(
                request, f'{lancamento.id_tipo} cadastrada com sucesso!')
            # TODO Provisório para evitar limpeza do form
            return render(request, 'lancamentos/pages/novo.html', context={'form': form})
            return redirect('lancamentos:novo')
        messages.error(request, 'Algo deu errado com a sua requisição!')
        return redirect('lancamentos:novo')
