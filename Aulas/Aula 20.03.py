#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:11:58 2018

@author: mariana.frasson
"""

"""
Problema
Dados um número inteiro n, n>0 é uma sequência com n números inteiros,
determinar quantos números de sequência são pares.
Por exemplo, para
6 -2 7 0 -5 8 4
o programa deve escrever 4 são pares.
"""

def main():
    n = int(input("Digite n: "))
    count = 0
    num = 0
    par = 0
    while count < n:
        num = int(input("Digite um inteiro: "))
        count += 1
        if num % 2 == 0:
            par = par + 1
    print(par, "são pares")
if __name__ == "__main__":
    main()
    
"""

Execução condicional: if
if condição:
    comando1
    comando2
    comandok

Significado: executa os comandos tabulados se a condição é verdadeira.

"""

def main2():
    n = int(input("Digite n: "))
    count = 0
    num = 0
    impar = 0
    while count < n:
        num = int(input("Digite um inteiro: "))
        count += 1
        impar = impar + num % 2
    print(n-impar, "são pares")
if __name__ == "__main2__":
    main2()
    
    
"""
a = (a // b) * b + a % b
"""


def main3():
    n = int(input("Digite n: "))
    count = 0
    num = 0
    par = 0
    while count < n:
        num = int(input("Digite um inteiro: "))
        count += 1
        if num % 2 == 0:
            par = par + 1
    print(par, "são pares e", n-par, "são ímpares")
if __name__ == "__main3__":
    main3()


"""
Problema
Dados um inteiro n, n>0, e as notas finais de n alunos, determinar:
    1. número de aprovados
    2. número de alunos de rec
    3. número de reprovados
    4. número de alunos bam-bam-bam  
"""

"""
Tipo float
Usamos ponto decimal.
Funções
int():
    str -> int
float():
    str -> float
    
"""

def main5():
    n = int(input("Digite n: "))
    count = 0
    nota = 0
    aprovado = 0
    rec = 0
    reprovado = 0
    bbb = 0
    while count < n:
        nota = float(input("Digite uma nota: "))
        count += 1
        if nota < 3:
            reprovado += 1
        if 3 <= nota < 5:
            rec += 1
        if nota >= 5:
            aprovado += 1
            if nota >= 9:
                bbb += 1
    print(reprovado, "reprovados")
    print(rec, "recuperação")
    print(aprovado, "aprovados")
    print(bbb, "bam-bam-bam")
if __name__ == "__main5__":
    main5()
    
    
def main6():
    n = int(input("Digite n: "))
    count = 0
    nota = 0
    aprovado = 0
    rec = 0
    reprovado = 0
    bbb = 0
    while count < n:
        nota = float(input("Digite uma nota: "))
        count += 1
        if nota >= 5:
            aprovado += 1
            if nota > 9:
                bbb += 1
        else: # nf < 5
            if nota < 3:
                reprovado += 1
            else:
                rec += 1
    print(reprovado, "reprovados")
    print(rec, "recuperação")
    print(aprovado, "aprovados")
    print(bbb, "bam-bam-bam")
if __name__ == "__main6__":
    main6()
    
"""
Execução alternativa: if-else
if condição:
    executa se condição True
else:
    executa se condição False
"""

"""
Problema
Dados um número inteiro n, n>0 e um dígito d (0<=d<=9), determinar
quantas vezes d ocorre em n.
Por exemplo, 3 ocorre 2 vezes em 63453
"""

def main7():
    n = int(input("Digite n: "))
    d = int(input("Digite d: "))
    count = 0
    while n < 0:
       dig = n % 10
       if dig % 10 == d:
           count += 1
           n = n // 10
    print(d, "ocorre", count, "vezes")
if __name__ == "__main7__":
    main7()

    


