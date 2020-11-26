from django.shortcuts import render
from django.http import HttpResponse
from random import randint


# Create your views here.

def home(request):
    a = randint(1, 10)
    b = randint(1, 100)
    nome = 'Wilson'
    lista = []
    cont = 0
    while True:
        num = randint(1, 26)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 5:
            break
    contexto = {'valor1': a, 'valor2': b, 'nome': nome, 'aleatorios': lista}
    return render(request, 'index.html', contexto)
