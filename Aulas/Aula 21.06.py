#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:09:15 2018

@author: mariana.frasson
"""

""""
Problema
Escreva uma função que recebe uma lista de valores (int ou str) ordenadas
crescentemente e um valor x e retorna um índica k tal que x está na posição k.
Se x não está na lista, a função retorna None.
10 20 25 35 38 40 44 50 55 65 99
0 1 2 3 4 56 7 8 9 10
"""
"""
Não usa ordenação.
"""
def indice(lista, x):
    """(list,obj) -> int ou None"""
    k = None
    n = len(lista)
    for i in range(n):
        if lista[i] == x:
            k = i
        return k

"""
Número de iterações é n.
"""

def indice2(lista,x):
    i = 0
    n = len(lista)
    while i < n and x > lista[i]:
        i += 1
    if i < n:
        if lista [i] == x:
            return i
    return None

def indice3(lista,x):
    """Busca com sentinela"""
    n = len(lista)
    i = 0
    lista += [x]
    while x != lista[i]:        
        i += 1
    if i < n:
        return i
    return None

"""
Número de iterações pode ser n.
"""

def indice4(lista,x):
    ini = 0
    n = len(lista)
    fim = n - 1
    while ini <= fim: 
        meio = (fim+ini) // 2
        if lista[meio] == x:
            return meio
        if lista[meio] < x:
            ini = meio + 1
        else:
            fim = meio - 1
    return None
        

"""
50 35 99 38 55 20 44 10 40 65 25 35
"""
def ordenada(lista):
    """(list) -> None
    Ordenação por seleção"""
    n = len(lista)
    for j in range(n-1):
        imin = 0
        for i in range(1,n):
            if lista[i] < lista[imin]:
                imin = i
        lista[0], lista[imin] = lista[imin], lista[0]
    
    

