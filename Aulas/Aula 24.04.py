#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:02:26 2018

@author: mariana.frasson
"""

"""

Problema
Dados x >= 0 e eps > 0, calcular uma aproximação da raiz quadrada de x
através da seguinte sequência.
ro = x
rn+1 = 1/2(rn+x/rn)
A aproximação será o primeiro valor rn+1 tal que |rn+1 - rn| < eps

"""



import math
    
def main(x,eps):
    x = float(input("Digite x: "))
    eps = float(input("Digite a precisão: "))
    print("raiz(%f) = %f" %(x, raiz(x,eps)))
    print("sqrt(%f) = %f" %(x, math.sqrt(x)))
    
def raiz(x,eps):
    """
    (float,float) -> float
    Retorna a raiz de x com aproximação eps.
    """
    rant = x
    ratual = (rant + 1)/2
    while ratual - rant < -eps or ratual - rant > eps:
        rant = ratual
        ratual = (rant + x/rant)/2
    return ratual


"""

Problema
Escreva uma função encaixa() que dados dois inteiros positivos a e b verifica
se b corresponde aos últimos dígitos de a.
a 67890 b 890 -> encaixa
a 1243 b 1243 -> encaixa
a 2457 b 245 -> não encaixa
a 457 b 2457 -> não encaixa

"""

def encaixa(a,b):
    """
    (int, int) -> bool
    Decide se b corresponde aos últimos dígitos de a.
    """
    while b > 0 and a % 10 == b % 10:
        a = a // 10
        b = b // 10
    return b == 0

"""
Escreva um programa que lê dois números positivos a e b e verifica se um é
pedaço do outro.
a 567890 b 678 b é pedaço
a 1243 b 2212435 a é pedaço
a 235 b 236 um não é pedaço do outro
Usando a função encaixa.
"""

def main2():
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    if a < b:
        a,b = b,a
    pedaco = False
    aa = a
    while a >= b and not pedaco:
        pedaco = encaixa(a,b)
        a //= 10
    if pedaco:
        print("%d é pedaço de %d" %(b,aa))
    else:
        print("Um não é pedaço do outro.")
        
"""

Problema
Dado um ponto origem (xo,yo), um inteiro n e uma sequência de n pontos,
determinar o ponto mais próximo da origem.

"""
import math

def dist(xo,yo,x1,y1):
    """
    (float,float,float,float) -> (float)
    Retorna a distância entre (xo,yo) e (x1,y1)
    """
    return math.sqrt((xo-x1)**2 + (yo-y1)**2)

def main3():
    n = int(input("Digite n: "))
    while n > 0:
        
        
            









