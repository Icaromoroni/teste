from django.shortcuts import render, get_object_or_404, redirect

from cadastrar.forms import CadastroForms, ItemForm, InventarioForm, Coordenadas

from cadastrar.models import Cadastros, Itens
from django.contrib import messages


# tela de inicio
def home(request):
    return render(request, 'formularios/home.html')

# tela do formulario de cadastro
def index(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            form.save()
            sobrevivente = form.instance
            #messages.info(request, 'Cadastro realizado com sucesso.' + sobrevivente.nome)
            return redirect('/sobreviventeViews/'+str(sobrevivente.id))
    else:
        form = CadastroForms()
        contexto = {'form': form}
        return render(request, 'formularios/index.html', contexto)

# tela de informacoes do sobrevivente
def sobreviventeViews(request, id):
    sobreviventeViews = get_object_or_404(Cadastros, pk=id)
    return render(request, 'formularios/sobreviventeViews.html', {'sobrevivente': sobreviventeViews})

def inventarioViews(request, id):
    id_S = get_object_or_404(Cadastros, pk=id)
    nome_item = ItemForm()
    qtd_item = InventarioForm()

    return render(request, 'formulario/inventarioForm.html',{'id': id_S, 'nome_item': nome_item, 'quantidade': qtd_item})

def atualizarViews(request, id):
    coordenadas = get_object_or_404(Cadastros, pk=id)
    form = Coordenadas(instance=Cadastros)    
    if request.method == 'POST':
        return False

    else:
        return render(request, 'formularios/atualizarLocal.html', {'form': form, 'coordenadas': coordenadas})

        if form.is_valid:
            cadastros.save()
    return cadastros



    