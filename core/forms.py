from django import forms
from django.core.mail import EmailMessage
from .models import Contato


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }),
            'assunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Assunto',
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Mensagem',
                'rows': 7,
            }),
        }

    def save_and_send_email(self):
        contato = self.save()

        conteudo = (
            f'Nome: {contato.nome}\n'
            f'Email: {contato.email}\n'
            f'Assunto: {contato.assunto}\n'
            f'Mensagem:\n{contato.mensagem}'
        )

        mail = EmailMessage(
            subject=contato.assunto,
            body=conteudo,
            from_email='contato_david@hotmail.com',
            to=['contato_david@hotmail.com'],
            headers={'Reply-To': contato.email},
        )

        mail.send()
        return contato