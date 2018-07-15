#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:04:53 2018

@author: mariana.frasson
"""

"""
Problema
Dado um número inteiro n > 0, verificar se n é primo.
Um número inteiro maior que 1 é primo se...

Exemplo
1 não é primo
2 é primo
27644437...
214783647...
"""

def main():
    n = int(input("Digite n: "))
    d = 2
    dividiu = False
    # decida se n é primo
    while d < n and not dividiu:
        if n % d == 0:
            dividiu = True
        d += 1
    # imprima a resposta
    if not dividiu and n != 1:
        print("É primo")
    else:
        print("Não é primo")
        
        
def main2():
   n = int(input("Digite n: "))
   i = 1
   d = 0
   while i <= n:
       if n % i == 0:
           d += 1
           print(n, " = ", i, " * ", n // i)
       i += 1
   if d == 2:
       print(n, " é primo.")
   else:
       print(n, " não é primo.")
if __name__ == '__main2__':
   main2()
   
   
   
   
"""
Problema
Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores
primos. Por exemplo, para n = 600, a saída deve ser
fator 2 multiplicidade 3
fator 3 multiplicidade 1
fator 5 multiplicidade 2

"""
def main3():
    n = int(input("Digite um número (>1): "))
    fat = 2
    while n != 1:
        mult = 0
        while n % fat == 0:
            mult += 1
            n = n // fat
        if mult != 0:
            print("Fator ", fat, " multiplicidade ", mult)
        fat += 1
        
        
        
        
    
    
    
    
    
    
    
        
            
    
    
    
    
    
    
    