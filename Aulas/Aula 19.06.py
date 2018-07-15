#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 08:02:26 2018

@author: mariana.frasson
"""

"""
Problema
Faça um programa que leia uma matriz de 0s (posições livres) e -1s e imprime
a quantidade de minas ao redor de cada posição livre.
0 -1 0 -1 -1 0 -1
0 0 0 0 -1 0 -1
-1 0 -1 -1 -1 0 0
-1 0 -1 0 0 0 -1
0 0 -1 0 0 -1 -1
Posição livre num de minas
[0][0] 1
[0][2] 2
[0][5] 4
"""

def leia_matrix():
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

LIVRE = 0
def main():
    campo = leia_matrix()
    print(to_string(campo))
    nlin = len(campo)
    ncol = len(campo[0])
    print("Posição livre    num de minas")
    print("-----------------------------")
    for i in range(nlin):
        for j in range(ncol):
            if campo[i][j] == LIVRE:
                print("[%d][%d]   %d" %(i,j,conte_minas(campo,i,j)))

def conte_minas(campo,i,j):
    """(list,int,int) -> int"""
    count = 0
    nlin = len(campo)
    ncol = len(campo[0])
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if nlin > k >= 0 and ncol > l >= 0:
                if campo[k][l] == -1:
                    count += 1
    return count

MINA = -1
def cont_minas(mat,lin,col):
    """(list,int,int) -> int"""
    cont = 0
    nlin = len(mat)
    ncol = len(mat[0])
    for i in range(lin-1,lin+2):
        for j in range(col-1,col+2):
            if 0 <= i < nlin and 0 <= j < ncol:
                if mat[i][j] == MINA:
                    cont += 1
    return cont

"""
Problema
Escreva um programa que leia:
    Um par de inteiros positivos nlin e ncol representando a dimensão de um
    tabuleiro.
    Um inteiro n >= 0.
    N pares de posições de rainhas.
E determina todas as posições sob ataque de alguma rainha.
nlin = 7
ncol = 7
"""

import util.py

VAZIO = ''
RAINHA = 'R'
MARCA = 'X'

def main2():
    dim_str = input("Digite a dimensão do tabuleiro:")
    dim_list = dim_str.split()
    nlin = int(dim_list[0])
    ncol = int(dim_list[1])
    tab = crie_matrix(nlin,ncol,VAZIO)
    print(util.to_string(tab))
    n = int(input("Digite num de rainhas:"))        
    for i in range(n):
        pos_str = input("Digite pos:")
        pos_list = pos_str.split()
        lin = int(pos_list[0])
        col = int(pos_list[1])
        marque_tabuleiro(tab,lin,col)

def marque_tabuleiro(tab,lin,col):
    tab[lin][col] = RAINHA
    nlin = len(tab)
    ncol = len(tab[0])
    for di in range(-1,2):
        for dj in range(-1,2):
            if di != 0 or dj != 0:
                i = lin
                j = col
                while 0 <= i < nlin and 0 <= j < ncol:
                    if tab[i][j] == VAZIO:
                        tab[i][j] = MARCA
                    i += di
                    j += dj
                    
    tab[lin][col] = RAINHA
    return tab

                    
    
    
    
    
    
    
    
    
    
    