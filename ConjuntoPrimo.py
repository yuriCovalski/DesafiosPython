
"""Descrição do problema:
Faça com que a função MathChallenge(num) pegue num e retorne 1 se qualquer arranjo de num for um número primo,
caso contrário, retorne 0. Por exemplo: se num for 910, a saída deve ser 1 porque 910 pode ser organizado em
109 ou 019, ambos primos.

"""

"""Meus comentários sobre:
    O problema mais difícil que já resolvi até a de postagem deste arquivo no repositório, eu demorei mais ou menos 
    umas 9 horas para conclui-lo. Não há nada de novidade nele, com as ferramentas básicas do python e algumas 
    funções da biblioteca random é possível resolve-lo, o mais demorado foi construir uma lógica que funcione para
    qualquer quantia de casas decimais e qualquer número natural maior que zero.

"""
import random

def MathChallenge(num):
    listaNumerosRecortados = []
    contadorPossibilidades = 0
    listaCombinacoesPossiveis = []
    string = ""
    listaTeste = []
    contador = 1
    fatorial = 1
    multiplos = 0

    for caractere in str(num):
        listaNumerosRecortados.append(int(caractere))

    while contador <= len(str(num)):
        fatorial *= contador
        contador += 1

    while contadorPossibilidades < fatorial:
        combinacao = random.sample(listaNumerosRecortados, len(str(num)))
        if combinacao not in listaCombinacoesPossiveis:
            listaCombinacoesPossiveis.append(combinacao)
            contadorPossibilidades += 1

    for listaDeNumeros in listaCombinacoesPossiveis:
        for elemento in listaDeNumeros:
            string += str(elemento)
            if len(string) == len(str(num)):
                listaTeste.append(int(string))
                string = ""

    for numero in listaTeste:
        for i in range(2, numero):
            if numero % i == 0:
                multiplos += 1

    if multiplos == 0:
        return 0
    else:
        return 1