#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:04:32 2018

@author: mariana.frasson
"""

"""

Problema
Dados um inteiro n > 0 e uma sequência com n números reais, imprimi-los na
ordem inversa de leitura.
Para n = 4 e 3.14 2.71 1.44 1.71
A saída é 1.71 1.44 2.71 3.14

"""

def main():
    n = int(input("Digite n: "))
    count = 0
    lista = []
    while count < n:
        x = float(input("Digite um número: "))
        lista = lista + [x]
        count += 1
    count = n-1
    while count >= 0:
        print(lista[count])
        count -= 1
    

"""

Lista
Sequência em matemática
Uma lista em Python é uma sequência de objeto de qualquer tipo [10,20,30,40]

Criar uma lista
A maneira mais simples é envolver os elementos entre colchetes.
uma_lista = [10,20,30,40]
outra_lista = ["olá",2.1,5,True,None]

Função len()
A função len() retorna o comprimento da lista. (list -> int)
print(len(uma_lista)) -> imprime 4
print(len(outra_lista)) -> imprime 5

+ e *
O operador + concatena duas listas.
lista_nova = uma_lista + outra_lista
O operador * repete uma lista um dado número de vezes.
lista_zeros = 1000*[0]

Acessando os elementos
Para acessar os elementos de uma lista usamos []
a = [10,-2,True,6,3.14]
a[0] a[1] a[2] a[3] a[4]
Última posição válida
a[len(a)-1]

lista_vazia = []

"""

"""

Problema
Dados n > 0 números entre 0 e 36, imprimir o número de ocorrências de cada
valor.
n = 10
10 5 31 36 31 0 7 5 1 0
Saída
0 ocorreu 2 vezes
1 ocorreu 1 vezes
2 ocorreu 0 vezes
.
.
.

"""

def main2():
    n = int(input("Digite n: "))
    no_ocorr = 37*[0]
    count = 0
    while count < n:
        valor = int(input("Digite um valor: "))
        no_ocorr[valor] += 1
        count += 1
    count = 0
    while count <= 37:
        print("%d ocorreu %d vezes" %(count,no_ocorr[count]))
        count += 1
        

