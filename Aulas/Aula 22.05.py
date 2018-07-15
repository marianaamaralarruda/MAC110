#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:02:07 2018

@author: mariana.frasson
"""

"""
Problema
Escreva uma função limpe que recebe uma string e retorna uma cópia dessa string
sem brancos no início e no fim.
"""

ESPACOS = " \n\t"
def limpe(s):
    """(str) -> str
    """
    n = len(s)
    ini = 0
    while ini < n and pertence(s[ini],ESPACOS):
        ini += 1
    fim = n
    while fim > ini and pertence(s[fim-1],ESPACOS):
        fim -= 1
    return s[ini:fim]
        
def pertence(c,s):
    """ (st,str) -> bool
    Retorna True se c está na string s
    """
    achou = False
    n = len(s)
    for i in range(0,n,1):
        if c == s[i]:
            achou = True
    return achou

ESPACOS = " \n\t"
def limpe2(s):
    """(str) -> str
    """
    n = len(s)
    ini = 0
    while ini < n and s[ini] in ESPACOS:
        ini += 1
    fim = n
    while fim > ini and s[fim-1] in ESPACOS:
        fim -=1
    return s[ini:fim]
        
"""
Problema
Fazer uma função separe() que recebe uma string s e um caractere separador
sep e retorna uma lista contendo as "palavras" do texto usando sep como delimitador.
"""


def separe(s,sep):
    lista = []
    # percorra s e pegue as palavras
    s += sep
    n = len(s)
    palavra = ""
    for i in range(0, n, 1):
        car = s[i]
        if car != sep:
            palavra += car
        elif palavra != "":
            lista += [palavra]
            palavra = "" #string vazio
    return lista


"""
Problema
Fazer um programa que leia uma sequencia de inteiros e calcule a sua soma.
"""

def main():
    texto = input("Digite uma sequencia de números: ")
    #2. pegue lista de números com srt
    lst_str = separe(texto," ")
    #3. converte a lista para uma lista de inteiros
    lst_int = str_para_int(lst_str)
    #4. calcule a soma e imprime
    print("soma =", sum(lst_int))
    
def str_para_int(lista):
    """(list de str) -> list de int
    """
    lista2 = []
    for i in range(0,len(lista),1):
        lista2 += [int(lista[i])]
    return lista2
        




