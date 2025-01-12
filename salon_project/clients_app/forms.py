from django import forms
from .models import *

# class ClientForm(forms.Form):
#     name = forms.CharField(required=True, max_length=50, label='Имя')
#     telephone = forms.CharField(required=True, max_length=12, label='Телефон')
#     last_visit = forms.DateField(
#         required=False,
#         label='Дата последнего визита',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#     )

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'telephone', 'last_visit_date']
        widgets={
            'last_visit_date': forms.DateInput(attrs={'type': 'date'})
        }
        # last_visit_date = forms.DateField(
        #     label='Дата последнего визита',
        #     widget=forms.DateInput(attrs={'type': 'date'}),
        # )
