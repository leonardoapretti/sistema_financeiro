from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from lancamentos.models import *


class GenericForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input'
    }))
