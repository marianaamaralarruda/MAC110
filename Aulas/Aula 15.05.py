#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:04:03 2018

@author: mariana.frasson
"""

"""
Problema
Escreva um programa que leia um inteiro n e uma sequência de n números inteiros e
imprima a maior soma de um segmento.
12 5 2 -2 -7 3 14 10 -3 9 -6 4 1
maior soma = 33
início = 4
fim = 9
"""

def main():
    seq = leia_sequencia()
    ini,fim,soma = soma_max(seq)
    print("soma maxima =", soma)
    print("inicio =", ini)
    print("fim =", fim)
    
def leia_sequencia():
    """(None) -> list"""
    n = int(input("Digite um inteiro: "))
    lista = n*[0]
    for i in range(0, n+1, 1):
        lista[i] += [float(input("Digite uma número: "))]
    return lista    

def soma_max(lista):
    """(list) -> int,int,int
    Recebe uma lista e retorna o início, fim e valor de um segmento de soma máxima.
    """
    a, b, s = 0, 0, 0
    n = len(lista)
    for i in range(0, n, 1):
        for j in range(i+1, n+1, 1):
            sf = soma_fatia(lista,i,j)
            if sf > s:
                s = sf
                a = i
                b = j
        return a, b, s

def soma_fatia(lista,ini,fim):
    """(list,int,int) -> número
    Retorna a soma lista[ini] + lista[ini+1] + ... + lista[fim-1]
    """
    soma_fatia = 0
    for i in range(ini,fim,1):
        soma_fatia += lista[i]
    return soma_fatia

def tabuada():
    for i in range(1,11,1):
        for j in range(1,11,1):
            print("%d x %d = %d" %(i,j,i*j))
            
            
"""
Fatia de uma lista (slice)
Uma fatia de uma lista é um clone de uma sublista. A fatia é especificada pelos
índices de início e fim(aberto).
a[6:10]

Especificação de uma fatia
lista[ini:fim]

"""

def main2():
    seq = leia_sequencia2()
    ini,fim,soma = soma_max2(seq)
    print("soma maxima =", soma)
    print("inicio =", ini)
    print("fim =", fim)
    
def leia_sequencia2():
    """(None) -> list"""
    n = int(input("Digite um inteiro: "))
    lista = n*[0]
    for i in range(0, n+1, 1):
        lista[i] += [float(input("Digite uma número: "))]
    return lista    

def soma_max2(lista):
    """(list) -> int,int,int
    Recebe uma lista e retorna o início, fim e valor de um segmento de soma máxima.
    """
    a, b, s = 0, 0, 0
    n = len(lista)
    for i in range(0, n, 1):
        for j in range(i+1, n+1, 1):
            sf = sum(lista[i:j])
            if sf > s:
                s = sf
                a = i
                b = j
        return a, b, s

def soma_fatia2(lista,ini,fim):
    """(list,int,int) -> número
    Retorna a soma lista[ini] + lista[ini+1] + ... + lista[fim-1]
    """
    soma_fatia = 0
    for i in range(0,len(lista),1):
        soma_fatia += lista[i]
    return soma_fatia

"""
Atribuição múltipla
a,b,c = c,27,"oi"
Imprimir uma tabuada
for i in range(...)
    for j in range(...)
Fatia
lista[ini:fim]
É clone
"""



            
        