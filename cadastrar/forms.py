from django import forms

SEXO = (('M','Masculino'), ('F', 'Feminino'))

class CadastroForms(forms.Form):
    nome = forms.CharField(label='nome',max_length=100)
    idade = forms.IntegerField(label='idade')
    sexo = forms.ChoiceField(label='sexo',choices=SEXO)
    latitude = forms.IntegerField(label='latitude')
    longitude = forms.IntegerField(label='latitude')

