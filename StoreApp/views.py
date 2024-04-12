from django.shortcuts import render
from StoreApp.models import Departamento, Produto
from StoreApp.forms import CadastroForm
# Create your views here.

def index (request):
    produtos_destaques= Produto.objects.filter(destaque = True)
    context={
        'produtos': produtos_destaques
    }
    return render(request,'index.html', context)

def produto_lista(request):
    produtos_lista= Produto.objects.all()
    context={

        'produtos' : produtos_lista,
        'titulo' : 'Todos os produtos'
    }

    return render(request,'produtos.html',context)


def produto_lista_por_departamento(request, id):
    produtos_lista= Produto.objects.filter(departamento_id=id)
    departamento=Departamento.objects.get(id=id)
    context={

        'produtos' : produtos_lista,
        'titulo' : departamento.nome
    }

    return render(request,'produtos.html',context)


def produto_detalhe (request,id):
    produto=Produto.objects.get(id=id)
    produtos_relacionados= Produto.objects.filter(departamento_id=produto.departamento).exclude(id=id)[:4]
    context={
        
        'produto': produto,
        'produtos_relacionados': produtos_relacionados
    }

    return render (request, 'produto_detalhes.html',context)

def sobre_empresa(request):
    return render (request, 'sobre_empresa.html')

def cadastro (request):
    formulario=CadastroForm()
    
    context={
        'formulario_cadastro': formulario
    }
    return render(request, 'cadastro.html', context)

