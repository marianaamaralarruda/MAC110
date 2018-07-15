#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:01:30 2018

@author: mariana.frasson
"""

"""
Problema
Escreva um programa que leia uma matriz de inteiros e determina o número de 
linhas nulas e colunas nulas.

0 0 0 0 1
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0

Linhas nulas = 2
Colunas nulas = 3
"""

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

def nula():
    matrix = leia_matrix2()
    print(to_string(matrix))
    lin_nul = linhas_nulas(matrix)
    col_nul = colunas_nulas(matrix)
    print("Linhas nulas = %d" %(lin_nul))
    print("Colunas nulas = %d" %(col_nul))
    
def linhas_nulas(matrix):
    """(list de list) -> int
    Retorna o número de linhas nulas.
    """
    count = 0
    for i in range(0,len(matrix),1):
        if matrix[i] == [0]*len(matrix[0]):
            count += 1
    return count

def colunas_nulas(matrix):
    """(list de list) -> int
    Retorna o número de linhas nulas.
    """
    count = 0
    for j in range(0,len(matrix[0]),1):
        coluna = []
        for i in range(0,len(matrix),1):
            coluna += [matrix[i][j]]
        if linhas_nulas(coluna):
            count += 1
    return count

"""
Problema
Escreva um programa que leia duas matrizes Amxn e Bmxp e calcula o seu produto.
1 2 -1
0 3 1

1 -1
2 0
3 2
"""
                
def main():
    a = leia_matrix2()
    print(to_string(a))
    b = leia_matrix2()
    print(to_string(b))
    c = mult_mat(a,b)
    print(to_string(c))

def mult_mat(ma,mb):
    """ (list,list) -> list
    Retorna o produto de ma por mb.
    """
    m = len(ma)
    n = len(ma[0]) #len(mb)
    p = len(mb[0])
    mc = crie_matrix(m,p,0)
    for s in range(m):
        for j in range(p):
            for k in range(n):
                mc[s][j] += ma[s][k]*mb[k][j]
    return mc
        





                
                
                