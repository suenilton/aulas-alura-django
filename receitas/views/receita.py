from django.shortcuts import get_object_or_404, render, redirect
from receitas.models import Receita
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(status_receita=True)

    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }

    return render(request,'receitas\index.html', dados)
    
def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id,)

    receita_a_exibir = {
        'receita': receita
    }
    return render(request,'receitas\\receita.html', receita_a_exibir)

def criar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        nova_receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, 
        modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)

        nova_receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'receitas\criar_receita.html')

def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    dados = {
        'receita': receita
    }

    return render(request, 'receitas\editar_receita.html', dados)

def atualizar_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        receita_para_atualizar = Receita.objects.get(pk=receita_id)
        receita_para_atualizar.nome_receita = request.POST['nome_receita']
        receita_para_atualizar.ingredientes = request.POST['ingredientes']
        receita_para_atualizar.modo_preparo = request.POST['modo_preparo']
        receita_para_atualizar.tempo_preparo = request.POST['tempo_preparo']
        receita_para_atualizar.rendimento = request.POST['rendimento']
        receita_para_atualizar.categoria = request.POST['categoria']
        
        if 'foto_receita' in request.FILES:
            receita_para_atualizar.foto_receita = request.FILES['foto_receita']

        receita_para_atualizar.save()

        return redirect('dashboard')
    else:
        return redirect('editar_receita')

def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')