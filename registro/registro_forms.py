# -*- coding: utf-8 -*-

__author__ = 'RubenMurga'

from django import forms
from registro.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'¿Cuál es tu nombre?'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'¿CUál es tu apellido?'}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    def __init__(self,*args,**kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
            self.fields[field].error_messages['required'] = 'Completa este campo'
    class Meta:
        model = User
        fields = ('first_name',)
class UserProfileForm(forms.ModelForm):
    Cafeteria = "Cafeteria"
    Libreria = "Libreria"
    Administrador = 'Administrador'
    opciones = (
        (Cafeteria, 'Cafeteria'),
        (Libreria, 'Libreria'),(Administrador, 'Administrador')
    )
    belongs_to = forms.ChoiceField(choices = opciones, label = 'Escoge', widget = forms.Select(attrs={'class':'form-control'}))
    codigo = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código para registro'}))
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].widget = forms.ClearableFileInput(attrs={
            'label': 'foto de perfil',
            'class': 'filestyle',
            'data-buttonName':'btn-primary',
        })
        self.fields['picture'].label = "imagen de perfil"

    class Meta:
        model = UserProfile
        fields = ('belongs_to', 'picture', 'codigo')

