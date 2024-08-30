from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from lancamentos.forms.lancamento_form import LancamentoForm
from lancamentos.models import Entry

# finalizar essa alteração


class NewEntryView(FormView):
    template_name = 'lancamentos/pages/novo.html'
    context_object_name = 'form'
    success_url = reverse_lazy('bank_account:new_card')
    form_class = LancamentoForm

    def form_valid(self, form):

        return super().form_valid(form)


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
            lancamento.id_active_user = request.user
            # print(lancamento)
            lancamento.save()
            messages.success(
                request, f'{lancamento.id_type} cadastrada!')
            # TODO Provisório para evitar limpeza do form
            return render(request, 'lancamentos/pages/novo.html', context={'form': form})
            return redirect('lancamentos:novo')
        messages.error(request, 'Algo deu errado com a sua requisição!')
        return redirect('lancamentos:novo')
