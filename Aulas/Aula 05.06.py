#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 08:08:24 2018

@author: mariana.frasson
"""

def palavras(texto):
    """(str) -> list
    Recebe um texto e retorna uma lista com as palavras do texto sem repetição.
    Exemplo:
    texto = "primavera, verao, outono"
    saida = ["primavera", "verao", "outono"]
    """
    alf = "abcdefghijklmnopqrstuvwxyz"
    lista = []
    palavra = ""
    texto += " "
    for i in range(0,len(texto),1): #for c in texto
        if texto[i] in alf:
            palavra += texto[i]
        elif palavra != "":
            if palavra not in lista: #!!!
                lista += [palavra]
            palavra = ""
    return lista

def main():
    nome = input("Digite o nome do arquivo:")
    with open(nome, "r", encode = "utf-8") as arq_entrada:
        texto = arq_entrada.read()
    print("Conteúdo arquivo:")
    print(texto)
    lista = palavras(texto)
    for i in range(0,len(lista),1):
        print("Paravra %d: %s" %(i,lista[i]))
    saida = nome + ".qtd"
    with open(saida, "w", encode = "utf-8") as arq_saida:
        for i in range(0,len(lista),1):
            arq_saida.write("%s \n" %(lista[i]))

            
            
def palavras2(texto):
    """(str) -> list
    Recebe um texto e retorna uma lista com as palavras do texto sem repetição.
    Exemplo:
    texto = "primavera, verao, outono"
    saida = ["primavera", "verao", "outono"]
    """
    alf = "abcdefghijklmnopqrstuvwxyz"
    lista = []
    lcount = []
    palavra = ""
    texto += " "
    for i in range(0,len(texto),1): #for c in texto
        if texto[i] in alf:
            palavra += texto[i]
        elif palavra != "":
            i = indice(palavra,lista)
            if i == None:
                lista += [palavra]
                lcount += 1 #coloca 1 no final de lcount
            else:
                lcount += 1
            palavra = ""
    return lista, lcount


def indice(palavra,lista):
    """(str,list) -> None ou int
    Retorna None se palavra not in lista, caso contrário retorna i tal que
    lista[i] = palavra.
    """
    for i in range(0,len(lista),1):
        if palavra == lista[i]:
            return i
    return None
        

def main2():
    nome = input("Digite o nome do arquivo:")
    with open(nome, "r", encode = "utf-8") as arq_entrada:
        texto = arq_entrada.read()
    print("Conteúdo arquivo:")
    print(texto)
    lista, lcount = palavras2(texto)
    for i in range(0,len(lista),1):
        print("Paravra %d: %s :%d" %(i,lista[i],lcount[i]))
    saida = nome + ".qtd"
    with open(saida, "w", encode = "utf-8") as arq_saida:
        for i in range(0,len(lista),1):
            arq_saida.write("%s :%d \n" %(lista[i]),lcount[i])
            
