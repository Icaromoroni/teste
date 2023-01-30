from django import forms

class CadastroForms(forms.Form):
    nome = forms.CharField(label='nome',max_length=100)
    idade = forms.IntegerField(label='idade')
    sexo = forms.CharField(label='sexo',max_length=9)
    latitude = forms.IntegerField(label='latitude')
    longitude = forms.IntegerField(label='latitude')

class Itens(forms.Form):
    agua = forms.IntegerField(label='agua')
    alimento = forms.IntegerField(label='alimento')
    medicamento = forms.IntegerField(label='medicamento')
    municao = forms.IntegerField(label='municao')