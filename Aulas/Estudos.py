#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:15:04 2018

@author: mariana.frasson
"""

def calcula_derivada(p):
    '''list -> list
    Recebe uma lista p que representa um polinômio e devolve a lista que
    representa sua derivada.
    Exemplos:
        calcula_derivada([ 1 ]) devolve [ ].
        calcula_derivada([ 1, 2, 3 ]) devolve [ 2, 6 ]'''
    
    p2 = []
    for i in range(1,len(p),1):
        p2 += [p[i] * i]
    return p2



def calcula_polinomio(p, x):
    '''list, float -> float
    Recebe uma lista p que representa um polinômio e um número real x
    e devolve o valor do polinômio calculado em x.
    Exemplos:
        calcula_polinomio([ ], 5) devolve 0.
        calcula_polinomio([ 1, 2, 3 ], 2) devolve 17.
        '''
    valor = 0
    for i in range(0,len(p),1):
        valor += p[i] * (x ** i)
    return valor
    

"""
Seqüências de DNA são strings de caracteres A, C, G e T. Um alinhamento de duas seqüências de
DNA s e t é obtido adicionando-se gaps, representados pelo caractere ‘_’ (underscore), a s e t, de
modo que as strings resultantes tenham o mesmo tamanho. Por exemplo, se s = TCGTAC e t = ATCG,
então um alinhamento pode ser
s
0 = T_CGTAC
t
0 = ATCG___
Dados números inteiros não-negativos m, d e g, a pontuação de um alinhamento é calculada da
seguinte forma: duas letras iguais alinhadas contam m pontos, duas letras diferentes alinhadas
contam −d pontos e uma letra alinhada com um gap ou dois gaps alinhados contam −g pontos.
Assim, se m = 5, d = 5 e g = 3, a pontuação do alinhamento acima é
−5 − 3 + 5 + 5 − 3 − 3 − 3 = −7.
Uma tarefa importante em biologia computacional é calcular um alinhamento entre duas seqüências
de DNA que tenha pontuação máxima. Nesta questão você dará um primeiro passo para resolver
este problema, escrevendo uma função que, dados números inteiros não-negativos m, d e g e duas
strings de mesmo tamanho contendo apenas as letras A, C, G e T e o caractere underscore ‘_’, devolve
a pontuação do alinhamento.
def pontuacao(m, d, g, s, t):
'''int, int, int, str, str -> int
Recebe inteiros não-negativos m, d e g e duas strings s e t de
mesmo tamanho contendo apenas os caracteres A, C, G, T e _ e
devolve a pontuacao do alinhamento representado pelas strings.
Exemplos:
pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___') devolve -7.
'''
"""


# 2 letras iguais = m
# 2 letras diferentes = -d
# X + gap = -g

def pontuacao(m, d, g, s, t):
    conta = 0
    igual_comp(s,t)
    for i in range(0,len(t),1):
        for j in range(0,len(s),1):
            conta_temp = conta
            conta = 0
            if t[i] == s[j]:
                conta += m
                print(conta)
            elif t[i] == s[j]:
                conta -= d
                print(conta)
            else:
                conta -= g
                print(conta)
        if conta_temp >= conta:
            return conta_temp
        else:
            return conta
    
    
def igual_comp(s,t):
    dif = abs(len(s)-len(t))
    for i in range(0,dif,1):
        if len(s) > len(t):
            t += "_"
        else:
            s += "_"
    return s,t
            

    
    
        
    
    
    
