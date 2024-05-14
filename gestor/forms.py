from django import forms
from .models import Livro, CustomUser

class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = "__all__"
        labels = {'Titulo' : '' , 'Autor': '', 'Editora' : '', 'Ano de publicação' : '','Quantidade total' : '', 'Imagem' : ''}


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
        labels = {'Nome' : '' , 'Email': '', 'Senha' : '', 'cpf' : ''}


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        return cleaned_data