#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:06:35 2018

@author: mariana.frasson
"""

def main():
    i = 5
    n = 2
    bla = [1,2,3]
    dobre_numero(n)
    dobre_lista(bla)
    print("main: i =", i)
    print("main n =", n)
    print("main: bla =", bla)
    
def dobre_numero(k):
    """(int) -> None"""
    k = 2*k
    print("dobre_numero k =", k)

def dobre_lista(lista):
    """(list) -> None"""
    n = len(lista)
    i = 0
    while i < n:
        lista[i] = 2*lista[i]
        i += 1
    print("dobra_lista lista =", lista)
    
"""
Apelido versus clones
Nomes diferentes para o mesmo valor.

def clone(lista):
    copia = []
    for i in range(0, len(lista), 1)
        copia = copia + [lista[i]]
    return copia
"""

"""
Problema
Faça um programa que leia dois vetores do R3 e imprime o ângulo entre eles.
def leia_vetor3D(?)
def normalize(?)
"""

import math

def main2():
    u = leia_vetor3D()
    v = leia_vetor3D()
    print("vetor de entrada")
    print(u)
    print(v)
    normalize(u)
    normalize(v)
    coso = produto_escalar(u,v)
    print("cosseno =", coso)
    
def leia_vetor3D():
    """(None) -> list"""
    vetor = 3*[0]
    for i in range(0, 3, 1):
        vetor[i] += [float(input("Digite uma coordenada: "))]
    return vetor

def normalize(x):
    """(list) -> None
    Altera os componentes de vetor."""
    raiz = 0
    for i in range(0,len(x),1):
        raiz += x[i]**2
        norma = math.sqrt(raiz)
        i = 0
        while i < 3:
            x[i] /= norma
            i += 1

def produto_escalar(u,v):
    """(list,list) -> float ou int
    Geral"""
    n = len(u)
    valor = 0
    for i in range(0,n,1):
        valor += u[i]*v[i]
    return valor
    








