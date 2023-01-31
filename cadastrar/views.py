from django.shortcuts import render, get_object_or_404, redirect

from cadastrar.forms import CadastroForms

from cadastrar.models import Cadastros
from django.contrib import messages

def home(request):
    return render(request, 'formularios/home.html')

def listaCadastro(request):
    cadastro = Cadastros.objects.all()
    return render(request, 'formularios/lista.html')

def index(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Cadastro realizado com sucesso.')
            return redirect("/")

    else:
        form = CadastroForms()
        contexto = {'form': form}
        return render(request, 'formularios/index.html', contexto)


def sobreviventeViews(request, id):
    sobreviventeViews = get_object_or_404(Cadastros, pk=id)
    return render(request, 'formularios/sobreviventeViews.html', {'sobreviventeViews': sobreviventeViews})


    