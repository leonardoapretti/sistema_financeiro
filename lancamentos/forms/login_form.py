from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(
            attrs={'placeholder': 'Digite seu nome de usuário',
                   'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Digite sua senha',
                   'class': 'form-control'}
        )
    )
