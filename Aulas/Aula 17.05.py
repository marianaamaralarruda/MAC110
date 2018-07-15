#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:06:19 2018

@author: mariana.frasson
"""

"""
Problema
Faça um programa que leia uma frase e determine a frequência relativa de vogais
no texto.
Exemplo
Como é bom estudar MAC0110!
Frequência relativa = 8/27 = 0.296296
"""

def main():
    texto = input("Digite um texto: ")
    n_vogais = conta_vogais(texto)
    n = len(texto)
    print("Frequencia relativa = %d/%d = %f" %(n_vogais,n,n_vogais/n))

def conta_vogais(s):
    """(str) -> int
    Retorna o número de vogais em s.
    """
    count = 0
    vogais = "aeiouAEIOUâêîôûÂÊÎÔÛáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙäëïöüÄËÏÖÜ"
    for i in range(0,len(s),1):
        car = s[i]
        for j in range(0,len(vogais),1):
            if car == vogais[j]:
                count += 1
    return count
    

"""
Tipos nativos: int, float, bool, str, Nonetype, list.
int, float, bool, Nonetype são primitivos.
Listas são compostas por partes menores (int, list, bool, ...).
Strings são compostos por partes menores, mas todas elas são caracteres (=strings
de comprimento 1).
"""


"""
Problema
Faça um programa que leia uma frase e imprime a mesma frase trocando as letras
maísculas por minúsculas.
"""

def main2():
    frase = input("Digite uma frase:")
    frase_min = para_minuscula(frase)
    print("Em minúsculas: ", frase_min)

"""
def para_minuscula(s):
    # (str) -> str
    maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxz"
    for i in range(0,len(s),1):
        car = s[i]
        for j in range(0,len(maiuscula),1):
            if car == maiuscula[j]:
                s[i] = minuscula[j]       DEU RUIM, COMPONENTES DE STRINGS NÃO PODEM SER ALTERADOS, IMUTÁVEIS (!= listas).
    return s
    
"""

def para_minuscula(s):
    """ (str) -> str
    """
    maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscula = "abcdefghijklmnopqrstuvwxz"
    nova_s = ""
    for i in range(0,len(s),1):
        car = s[i]
        achou = False
        j = 0
        while j < len(maiuscula) and not achou:
            if car == maiuscula[j]:
                achou = True
            else:
                j += 1
        if achou:
            nova_s += minuscula[j]
        else:
            nova_s += car
    return nova_s
    
    
    
    
    