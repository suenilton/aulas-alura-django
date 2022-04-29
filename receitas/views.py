from django.shortcuts import get_object_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(status_receita=True)

    dados = {
        'receitas': receitas
    }

    return render(request,'index.html', dados)
    
def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id,)

    receita_a_exibir = {
        'receita': receita
    }
    return render(request,'receita.html', receita_a_exibir)

def busca(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(status_receita=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if busca:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados ={
        'receitas': lista_receitas
    }

    return render(request, 'busca.html', dados)
