from django import forms

from .models import Cadastros, Inventario, Itens

SEXO = (('M','Masculino'), ('F', 'Feminino'))

'''class CadastroForms(forms.Form):
    nome = forms.CharField(label='nome',max_length=100)
    idade = forms.IntegerField(label='idade')
    sexo = forms.ChoiceField(label='sexo',choices=SEXO)
    latitude = forms.IntegerField(label='latitude')
    longitude = forms.IntegerField(label='latitude')'''

'''class Inventario(forms.Form):
    pass'''

class CadastroForms(forms.ModelForm):
    
    class Meta:

        model = Cadastros

        fields = ['nome', 'idade', 'sexo', 'latitude', 'longitude']

class ItemForm(forms.ModelForm):

    class Meta:
        model = Itens

        fields = ['nome']

class InventarioForm(forms.ModelForm):

    class Meta:

        model = Inventario

        fields = ['quantidade']

class Coordenadas(forms.ModelForm):

    class Meta:

        model = Cadastros

        fields = ['latitude', 'longitude']
