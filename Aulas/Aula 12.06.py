#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:02:14 2018

@author: mariana.frasson
"""

"""
Problema
Escreva um programa que lê um inteiro n e uma matriz nxn e verifica se a matriz
é simétrica.

11 -3 4 8
-3 12 6 11
4 6 5 13
8 11 13 5

matrix = [[11,-3,4,8],[-3,12,6,11]...]
matrix[0]
matrix[1]
matrix[0][2]
"""

def crie_matrix(nlin, ncol, valor):
    """ (int,int,x) -> (list de list)
    Cria uma matriz nlin x ncol com valor em cada posição.
    
    matrix = [[ncol*[valor]]*nlin]
    return matrix
    NÃO FUNCIONA!
    """
    matrix = []
    for i in range(nlin):
        linha = ncol*[valor]
        matrix += [linha]
    return matrix

def leia_matrix():
    """ (None) -> (list de list)
    """
    m = int(input("Digite o número de linhas: "))
    n = int(input("Digite o número de colunas: "))
    matrix = crie_matrix(m, n, 0)
    for i in range(m):
        for j in range(m):
            print("Digite o elemento [%d][%d]" %(i,j))
            matrix[i][j] = int(input())
    return matrix

def leia_matrix2():
    """ (None) -> (list de list)
    """
    nome = input("Digite o nome de um arquivo: ")
    with open(nome, "r", encoding = "utf-8") as arq:
        arq_str = arq.read()
    arq_lst = arq_str.split()
    nlin = int(arq_lst[0])
    ncol = int(arq_lst[1])
    matrix = crie_matrix(nlin,ncol,0)
    k = 2
    for i in range(nlin):
        for j in range(ncol):
            matrix[i][j] = int(arq_lst[k])
            k += 1
    return matrix


def simetrica(matrix):
    """ (list de list) -> Bool
    Recebe uma matriz e verifica se é simétrica ou não.
    """
    check = True
    if len(matrix) != len(matrix[0]):
        return False
    for i in range(1,len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                check = False
    return check

def main():
    matrix = leia_matrix()
    print(to_string(matrix))
    if simetrica(matrix):
        print("Matriz é simétrica.")
    else:
        print("Matriz não é simétrica.")
        
def to_string(a):
    """ (list) -> string
    Retorna um string para ser impresso.
    """
    s = ""
    nlin = len(a)
    ncol = len(a[0])
    s += "Matriz %d x %d" %(nlin,ncol)
    s += "\n"
    for i in range(nlin):
        for j in range(ncol):
            s += "%6d " %(a[i][j])
        s += "\n"
    return s
        
    
    
    
    
    
    