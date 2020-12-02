from django.shortcuts import render
from django.http import HttpResponse
from random import randint


# Create your views here.

def home(request):
    jogos = []
    jogo = []
    repeticao = list()
    if request.POST:
        n = int(request.POST['variavel'])
        for j in range(n):
            cont = 0
            while cont < 6:
                num = randint(1, 61)
                if num not in jogo:
                    jogo.append(num)
                    cont += 1
            jogos.append(jogo[:])
            jogo.clear()

    """ 
        for i in range(1, 26):
            count = 0
            for j in jogos:
                if i in j:
                    count += 1
            repeticao.append(count)
    """
    contexto = {'jogos': jogos, 'repeticao': repeticao}
    return render(request, 'index.html', contexto)
