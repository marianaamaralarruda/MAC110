#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:03:02 2018

@author: mariana.frasson
"""

"""

Problema
Um número natural é triangular se ele é produto de três números naturais
consecutivos.
Exemplo: 120 é triangular pois 4x5x6 = 120.
Dado um inteiro não negativo n, imprimir True se n é triangular ou False em
caso contrário.

"""

def istriang():
    n = int(input("Digite um número: "))
    x = 0
    t = 0
    while t < n:
        t = x*(x+1)*(x+2)
        x += 1
    
    print(t == n)
    
if __name__ == "__istriang__":
    istriang()
    
    