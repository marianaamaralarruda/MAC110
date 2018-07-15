#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:02:52 2018

@author: mariana.frasson
"""

"""
Problema
Dados n e dois números inteiros positivos i e j, imprimir os n primeiros
naturais que são múltiplos de i ou de j ou de ambos.
Para n = 8, i = 2 e j = 3, o programa deve imprimir
0 2 3 4 6 8 9 10
"""

def main():
    n = int(input("Digite n: "))
    i = int(input("Digite i: "))
    j = int(input("Digite j: "))
    mult = 0
    counter = 0
    while counter < n:
        if mult % i == 0 or mult % j == 0:
            print(mult)
            counter += 1
        mult += 1

def main2():
    n = int(input("Digite n: "))
    i = int(input("Digite i: "))
    j = int(input("Digite j: "))
    mult = 0
    counter = 0
    while counter < n:
        if mult % i == 0:
            print(mult)
            counter += 1
        elif mult % j == 0:
            print(mult)
            counter += 1
        mult += 1
        
def main3():
     n = int(input("Digite n: "))
     i = int(input("Digite i: "))
     j = int(input("Digite j: "))
     multi = 0
     multj = 0
     count = 0
     while count < n:
         if multi < multj:
             print(multi)
             multi += i
         elif multi > multj:
            print(multj)
            multj += j
         else: #multi == multj
            print(multi)
            multi += i
            multj += j
         count += 1

"""
Problema
Os pontos que pertencem a figura são tais que x > 0, y > 0 e
xˆ2+yˆ2 < 1. Dado um inteiro n > 0 e as coordenadas de n pontos,
para cada ponto indique se ele pertence ou não a figura.

"""

def main4():
    n = int(input("Digite n: "))
    i = 0
    while i < n:
        x = float(input("Digite x: "))
        y = float(input("Digite y: "))
        if x**2 + y**2 < 1:
            print("O ponto (", x, ",", y, ") pertence a figura.")
        else:
            print("O ponto (", x, ",", y, ") não pertence a figura.")
        i +=1

               