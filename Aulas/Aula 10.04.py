#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 08:04:02 2018

@author: mariana.frasson
"""

"""

Problema
Escreva um programa que leia dois inteiros m > 0 e n >= 0 e calcula o
coeficiente binomial.
(m) = m!
(n)   n!(m-n)!

"""

def main():
    m = int(input("Digite m :"))
    n = int(input("Digite n :"))
    mfat = 1
    nfat = 1
    mnfat = 1
    count = 2
    while count <= m:
        mfat = mfat * count
        count += 1
    count = 2
    while count <= n:
        nfat = nfat * count
        count += 1
    count = 2
    while count <= (m-n):
        mnfat = mnfat * count
        count += 1
    bin = mfat // (nfat * mnfat)
    print("binomial(%d,%d) = %d" %(m, n, bin))        
    
"""

%d = marcador para um inteiro

"""

def main2():
    m = int(input("Digite m :"))
    n = int(input("Digite n :"))
    k = m
    kfat = 1
    count = 2
    while count <= k:
        kfat = kfat * count
        count += 1
    mfat = kfat
    k = n
    kfat = 1
    count = 2
    while count <= k:
        kfat = kfat * count
        count += 1
    nfat = kfat
    k = (m-n)
    kfat = 1
    count = 2
    while count <= k:
        kfat = kfat * count
        count += 1
    mnfat = kfat
    bin = mfat // (nfat * mnfat)
    print("binomial(%d,%d) = %d" %(m, n, bin))  
    
def fatorial(k):
    """(int) -> int
    Recebe um inteiro k e retorna o seu fatorial.
    """
    kfat = 1
    count = 2
    while count <= k:
        kfat = kfat * count
        count += 1
    return kfat
    
"""
Definição de funções
def "nome da funcão" ("parâmetros"):
    ""
    comentário
    ""
    lista de comandos/corpo da função
    
Variáveis criadas dentro de uma função são locais, ou seja, só existem
dentro da função.
Parâmetros são variáveis locais criadas na chamada da função.

Término da execução
Após a execução do comando return "expressão", a função é abandonada.
Uma função também termina a sua execução após realizar todos os
comandos.

Chamada da funçào
nfat = fatorial(100)
fat = fatorial(m-n)
main()

Anatomia de um programa em Python
def main():
    corpo do main()
def fatorial(12):
    corpo fatorial()
def g(x,y,z):
    corpo de g()
if __name__ == "__main__"
    main()
    
"""

"""

Problema
a) Escreva uma função que recebe dois números inteiros m e n e retorna
(m)
(n)

b)Escreva uma função main() que leia um inteiro n >=0 e imprime os 
valores de 
(n) (n) (n) ... ( n ) (n)
(0) (1) (2)     (n-1) (n)

"""

def fatorial2(k):
    """
    (int) -> int
    Recebe um inteiro k e retorna o seu fatorial.
    """
    kfat = 1
    count = 2
    while count <= k:
        kfat = kfat * count
        count += 1
    return kfat
def binomial(m,n):
    """
    Recebe dois inteiros m e n e retorna o seu coeficiente binomial.
    """      
    mfat = fatorial2(m)
    nfat = fatorial2(n)
    mnfat = fatorial2(m-n)
    bin = mfat // (nfat * mnfat)
    return bin

def main3():
    n = int(input("Digite n :"))
    i = 0
    while i <= n:
        binomial(n,i)
        print("binomial(%d,%d) = %d" %(n, i, binomial(n,i)))
        i += 1

    

    



    
    
    
    
    
    
    
    
    
    
    
    
    