from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def lerDoBanco(nome):
    lista_nomes = [
        {
            'nome':'Ana',
            'idade':20
        },
        {
            'nome': 'Pedro',
            'idade': 25
        },
        {
            'nome': 'Joaquim',
            'idade': 27
        }
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Não encontrado', 'idade': 0}

def articles(request, year):
    return HttpResponse("Ano: " + str(year))

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})