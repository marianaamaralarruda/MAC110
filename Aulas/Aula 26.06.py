#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 08:05:59 2018

@author: mariana.frasson
"""

"""
Problema
Os elementos aij de uma matriz de números reais Anxn representam os custos de
transporte de uma cidade i para uma cidade j.
14.8 2.9 7.5 8.9
5.3 8.4 18.0 14.8
2.3 21.7 3.9 8.7
7.3 12.1 43.7 57.8

O itinerário
c = [0,3,1,3,3,2,1,0,2]
tem custo
8.9 + 12.1 + 14.8 + 57.8 + 43.7 + 21.7 + 5.3 + 7.5 = 171.8
"""

def custo(A,C):
    """(matriz,list) -> float
    Retorna o custo do itinerário C.
    """
    nc = len(C)
    sum = 0
    for i in range(nc-1):
        sum += A[C[i]][C[i+1]]
    return sum

"""
Problema
Dizemos que uma lista é um pico se tem apenas um elemento maior que seus vizinhos.
[2,5,10,46,25,12,7] é um pico.
[13,5,4,2,3,0,-3,14] não é um pico.
[7,6] é um pico.
[6,7,8,9,10] é um pico.
"""
def pico(lista):
    """(list) -> bool
    Retorna True se lista é um pico.
    """
    pico = True
    subindo = True
    n = len(lista)
    i = 0
    while subindo and i < n-1:
        if lista[i] <= lista[i+1]:
            i+=1
        else:
            subindo=False
    while not subindo and i<n-1:
        if lista[i]>=lista[i+1]:
            i+=1
        else:
            subindo=True
            pico=False
    return pico

def troca(valor,notaA,notaB):
    """(int,int,int) -> int,int ou None
    Retorna inteiros não negativos na e nb tais que
    naxnotaA + nbxnotaB = valor
    """
    na = 0
    nb = 0
    conta = 0
    while conta < valor:
        conta = na*notaA + nb*notaB
        if conta == valor:
            return na,nb
        while conta < valor:
            conta = na*notaA + nb*notaB
            if conta == valor:
                return na,nb
            nb += 1
        na += 1
    return None

        
            
            
        