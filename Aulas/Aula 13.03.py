#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 08:31:25 2018

@author: mariana.frasson

Problema
Dado um inteiro positivo n, imprimir os n primeiros naturais ímpares.
Exemplo: para n = 4, o programa deve exibir 1 3 5 7.

"""

def main():
    n = int(input("Digite n: "))
    impar = 1
    while impar <= (2*n -1):
        print(impar)
        impar += 2
        
        
def main2():
    n = int(input("Digite n: "))
    impar = 1
    i = 0
    while i != n:
        print(impar)
        impar = impar + 2
        i = i +1
        
"""

Problema
Dados números inteiros n e k, k >= 0, determinar n**k. Por exemplo,
dados os números 3 e 4, o seu programa deve escrever 81.

"""

def func():
    n = int(input("Digite n: "))
    k = int(input("Digite expoente: "))
    if k >= 0:
        result = n**k
        print(result)


def funcProf():
    n = int(input("Digite n: "))
    k = int(input("Digite expoente: "))
    prod = 1
    i = 0
    while i < k:
        prod = prod * n
        i = i + 1
    print(n, " elevado a ", k, " = ", prod)
    
    
"""

Problema
Dado um inteiro n, n>=0, determinar n!.

"""

def func3():
    n = int(input("Digite um inteiro: "))
    result = 1
    nsaldo = n
    while n > 0:
        result *= n
        n -= 1
    print(nsaldo, "fatorial= ", result)
if __name__ == "__func3__":
    func3()
    



