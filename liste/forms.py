# -*- coding: utf-8 -*-

from django import forms
from .models import Comanda
import datetime

class HtmlForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

class ComandaForm(forms.ModelForm):
    name = forms.CharField(label='Numele',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder':'Introduceti numele clientului'}
                                ))
    phone = forms.CharField(label='Telefonul',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder':'Introduceti telefonul clientului'}
                                ))
    content = forms.CharField(label='Comanda',
                                widget=forms.Textarea(
                                    attrs={'class': 'form-control',
                                    'placeholder':'Introduceti comanda clientului'}
                                ))
    created_on = forms.DateField(initial=datetime.date.today)

    class Meta(object):
        model = Comanda
        fields = ('name','phone','content', 'created_on',)
