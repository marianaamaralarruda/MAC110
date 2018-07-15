#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 08:02:18 2018

@author: mariana.frasson
"""

"""

Problema
Escreva um programa que leia dois inteiros n e k e os k+1 coeficientes de um
polinômio de grau k e outros n números reais. O programa deve imprimir o valor
do polinômio e de suas derivadas primeira e segunda para cada um dos n números
reais.


Polinômios podem ser representados por listas
p(x) = 5 + x + 2xˆ2 + 3xˆ4
p = [5,1,2,0,3]
5 = p[0]
1 = p[1]
2 = p[2]
0 = p[3]
3 = p[4]
Número na posição m é o coeficiente xˆm.

"""

def valor_polinomio(p,x):
    """(list,float) -> (float)
    Recebe uma lista p representando um polinômio e um valor x e retorna p(x).
    """ 
    valor = 0
    for i in range(0,len(p),1):
        valor += (x**i)*p[i]
        return valor
    
def leia_polinomio():
    """
    (None) -> list
    Lê os coeficientes de um polinômio e retorna uma lista que o representa.
    """
    p = []
    grau = int(input("Digite o grau: "))
    for i in range(0, grau+1, 1):
        coef = float(input("Digite o valor de x%d" %i))
        p += [coef]
    return p

def derivada(p):
    """ (list) -> list
    Retorna a alista que representa a derivada de p.
    """
    dp = []
    for i in range(1, len(p),1):
        dp += [p[i]*i]
    return dp

def imprima_polinomio(p):
    """(list) -> None
    """
    for i in range(0,len(p),1):
        print("%f*xˆ%f" %(p[i],i), end='' )
        
def main():
    #leia polinômio
    p = leia_polinomio()
    imprima_polinomio(p)
    dp = derivada(p)
    imprima_polinomio(dp)
    ddp = derivada(dp)
    imprima_polinomio(ddp)
    n = int(input("Digite n :"))
    for i in range(0,n,1):
        x = float(input("Digite x :"))
        print("valor p(%f) = %f"%(x,valor_polinomio(p,x)))
        print("valor dp (%f) = %f" %(x,valor_polinomio(dp,x)))
        print("valor ddp(%f)=%f" %(x, valor_polinomio(ddp,x)))
    


        
    
    
    
    
    
    
    