from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import DeleteView


class DeleteBaseView(DeleteView):

    def get_success_url(self):
        messages.success(self.request, 'Lançamento apagado!')
        return reverse(self.success_url)
