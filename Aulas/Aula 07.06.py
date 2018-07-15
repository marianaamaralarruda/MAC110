#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:54:31 2018

@author: mariana.frasson
"""

"""
Dicionários
Um dicionário é um conjunto de objetos ou itens, cada um dotado de uma chave e
um valor.
As chaves podem ser números ou strings ou... O mesmo para valores.
Um dicionário está sujeito a dois tipos de operações: inserção (colocar no
dicionário um novo item) e busca (consiste em encontrar um item com uma
determinada chave).

Dicionários em Python
dicio = {} #dicionário vazio
dicio[chave] = valor #inserção de um item
dicio['fracassei'] = 10
dicio['Fracassei'] = 20
dicio['FrAcASSEI'] = 30
dicio[5] = 'oi!'
{'fracassei':10, 'Fracassei':20, 'FrAcASSEI':30, 5:'oi!'}
"""

def palavras(texto):
    """(str) -> dict
    Cria e retorna um dicionário onde as chaves são palavras e os valores são
    número de ocorrências.
    """
    alf = "abcdefghijklmnopqrstuvwxyz"
    palavra = ""
    texto += " "
    dic = {}
    for i in texto: #busca
        if i in alf:
            palavra += i
        elif palavra != "":
            if palavra in dic:
                dic[palavra] += 1 #atualização
            else:
                dic[palavra] = 1 #inserção
            palavra = ""
    return dic

def palavras2(texto):
    palavra = ""
    texto += " "
    dicio = {}
    for i in texto: #busca
        if palavra != "":
            dicio[palavra] += 1
        else:
            dicio[palavra] = 1
"""
valor = dicio.get(palavra)
if valor != None:
    dicio[palavra] = valor + 1
else:
    dicio[palavra] = 1
"""


def main():
    PROMPT = "consulta >>>"
    QUIT = "QUIT"
    LEN = 'len'
    CHAVES = 'chaves'
    nome = input("Digite o nome do arquivo:")
    with open(nome, "r", encoding = "utf-8") as arq_entrada:
        texto = arq_entrada.read()
    print("Conteúdo arquivo:")
    print(texto)
    dicio = palavras(texto)
    palavra = input(PROMPT)
    while palavra != QUIT:
        if palavra == LEN:
            print(len(dicio))
        elif palavra == CHAVES:
            print(dicio.keys())
        else:
            if palavra in dicio:
                print(dicio(palavra))
            else:
                print("None")
        palavra = input(PROMPT)
            
