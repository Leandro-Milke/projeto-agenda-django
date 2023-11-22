from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from . import models


class ContactForms(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )
        
    
    def clean(self):        

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC:':
            self.add_error(
                'first_name',
                ValidationError(
                    'Nome Inválido',
                    code='invaid'
                )
            )

        return first_name