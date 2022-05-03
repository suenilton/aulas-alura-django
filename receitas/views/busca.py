from django.shortcuts import get_object_or_404, render, redirect
from receitas.models import Receita


def busca(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(status_receita=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados ={
        'receitas': lista_receitas
    }

    return render(request, 'receitas\\busca.html', dados)