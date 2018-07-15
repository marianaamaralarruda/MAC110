# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""

Problema
Dados um inteiro n > 0 e n notas, calcular a média das notas e contar quantas
estão acima da média.

"""

def main():
    notas = leia_notas()
    soma = soma_notas(notas)
    media = soma/len(notas)
    count = 0
    for j in range(0,len(notas),1):
        if notas[j] > media:
            count += 1
    print("Notas acima da média ", media, "são", count)
    
def soma_notas(valores):
    """
    (list) -> float | int
    """
    soma = 0
    for k in range(0,len(valores),1):
        soma += valores[k]
    return soma

def leia_notas():
    """ (None) -> list
    Cria e retorna uma lista de notas lidas.
    """
    n = int(input("Digite n: "))
    #cria uma lista 'notas'
    notas = n*[0] #[0,0,...,0]
    i = 0
    while i < n:
        notas[i] = float(input("Digite uma nota: "))
        i += 1
    return notas

def leia_notas2():
    """ (None) -> list
    Cria e retorna uma lista de notas lidas.
    """
    n = int(input("Digite n: "))
    #cria uma lista 'notas'
    notas = [] #[0,0,...,0]
    i = 0
    while i < n:
        valor = float(input("Digite uma nota: "))
        notas = notas + [valor]
        i += 1
    return notas

def leia_notas3():
    """ (None) -> list
    Cria e retorna uma lista de notas lidas.
    """
    n = int(input("Digite n: "))
    #cria uma lista 'notas'
    notas = [] #[0,0,...,0]
    i = 0
    for i in range(0,n,1):
        notas[i] = float(input("Digite uma nota: "))
    return notas

"""

Comando de repetição for

for var in range(início, fim, passo):
    comandos

- início é fechado
- fim é aberto
    
for i in range(5,14,2):
    print(i)
Imprime 5,7,9,11,13

Tem o mesmo efeito:
var = início
while var < fim:
    comandos
    var += passo
    
"""



"""

Problema
Dados n e uma sequência com n números inteiros conte e imprima o número de
vezes que cada número ocorre na sequência.

"""

def main2():
    n = int(input("Digite n: "))
    count = 0
    lista = []
    while count < n:
        numero = int(input("Digite um número: "))
        count += 1
        lista += [numero]
        
        

def indice(item, lista):
    """ (int,list) -> int ou None
    Retorna o índice onde item ocorre na lista ou None se item não está na
    lista.
    """
    n = len(lista)
    for i in range(0,n,1):
        if lista[i] == item:
            return i
    return None










