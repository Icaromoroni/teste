from django.shortcuts import render

from cadastrar.forms import CadastroForms,Itens

def home(request):
    return render(request, 'formularios/home.html')

def index(request):
    form = CadastroForms()
    itensForm = Itens()
    contexto = {'form': form, 'itensForm': itensForm}
    return render(request, 'formularios/index.html', contexto)