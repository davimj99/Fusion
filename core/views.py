from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Recurso
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()

        return context

    def form_valid(self, form):
        form.save_and_send_email()
        messages.success(self.request, 'Mensagem enviada com sucesso!, Agradecemos o seu contato e retornaremos em breve.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Erro ao enviar a mensagem. Verifique os campos e tente novamente.'
        )
        return super().form_invalid(form)


class TestView(TemplateView):
    template_name = 'teste.html'