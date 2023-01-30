from django.shortcuts import render

from cadastrar.forms import CadastroForms

def home(request):
    return render(request, 'formularios/home.html')

def index(request):
    form = CadastroForms()
    contexto = {'form': form}
    return render(request, 'formularios/index.html', contexto)