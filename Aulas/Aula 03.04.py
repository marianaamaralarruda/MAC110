#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 08:01:33 2018

@author: mariana.frasson
"""

"""

Dados n pontos (x,y) para cada ponto, determinar se (x,y) pertence a
região H.

"""

def main1():
    n = int(input("Digite n:"))
    count = 0
    while count < n:
        x = float(input("Digite x:"))
        y = float(input("Digite y:"))
        if x*x + y*y < 1:
            if x > 0:
                if y > 0:
                    print("O ponto (", x, ",", y, ") pertence à região H.")
                else:
                    print("O ponto (", x, ",", y, ") não pertence à região H.")
            else:
                print("O ponto (", x, ",", y, ") não pertence à região H.")
        else:
            print("O ponto (", x, ",", y, ") não pertence à região H.")
        count += 1
        
def main2():
    n = int(input("Digite n:"))
    count = 0
    while count < n:
        x = float(input("Digite x:"))
        y = float(input("Digite y:"))
        if x*x + y*y < 1 and x > 0 and y < 0:
            print("O ponto (", x, ",", y, ") pertence à região H.")
        else:
            print("O ponto (", x, ",", y, ") não pertence à região H.")
        count += 1
        
"""

Operadores lógicos
Existem três operadores lógicos:
and, or, not

Exemplo
2 < 3 and -5 < 0: True
2 > 3 and -5 < 0: False
2 < 3 or -5 < 0: True

Prioridades
( )
**
* /
+ -
< > <= >=
not
and
or

"""

"""
Problema

Dado um inteiro n, n > 0 e uma sequência com n números inteiros,
verificar se a sequência é estritamente crescente.

Exemplo
7 -6 0 12 15 37 101 201 resp SIM
7 -6 0 17 15 37 101 201 resp NÃO

"""

def main3():
    n = int(input("Digite n:"))
    contador = 1
    anterior = int(input("Digite um inteiro: "))
    d = 1
    while contador < n:
        atual = int(input("Digite um inteiro: "))
        if anterior >= atual:
            d = 0
        anterior = atual
        contador += 1
    if d == 1:
        print("É crescente.")
    else:
        print("Não é crescente.")
        
        
"""

Problema
Dado um número n > 0 verificar se n contém dois dígitos adjacentes
iguais.
Exemplo
1 2 3 4 3 2 1 resposta NÃO
1 2 3 4 5 5 6 resposta SIM

"""

def main4():
    n = int(input("Digite n: "))
    tem = False
    dig_ant = n % 10
    n = n // 10
    while n > 0:
        dig_atual = n % 10
        if dig_ant <= dig_atual:
            tem = True
        dig_ant = dig_atual
    if tem == True:
        print("Tem dígitos adjacentes iguais.")
    else:
        print("Não tem dígitos adjacentes iguais.")
        
        