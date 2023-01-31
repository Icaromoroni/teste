from django.shortcuts import render, get_object_or_404

from cadastrar.forms import CadastroForms

from cadastrar.models import Cadastros

def home(request):
    return render(request, 'formularios/home.html')

def listaCadastro(request):
    cadastro = Cadastros.objects.all()
    return render(request, 'formularios/lista.html')

def sobreviventeViews(request, id):
    sobreviventeViews = get_object_or_404(Cadastros, pk=id)
    return render(request, 'formularios/sobreviventeViews.html', {'sobreviventeViews': sobreviventeViews})

def index(request):
    form = CadastroForms()
    contexto = {'form': form}
    return render(request, 'formularios/index.html', contexto)