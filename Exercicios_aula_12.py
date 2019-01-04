# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:33:50 2018

@author: thais
"""
#Exercicio1 (ERRADO)

def matrix(k,v):
    matriz={(0,3):1,(3,1):2,(4,3):3}
    if (k,v)!=((0,3),(3,1),(4,3)):
        matriz.get((k,v),0)
    #print(matriz)
    print(matriz.get((k,v)))

matrix(0,3)
matrix(2,1)
matrix(4,3)
matrix(2,2)

#Exercício 2 (ERRADO)

#ítem (a)
def letras(word):
    dic={}
    letra=word.strip.split()
    dic.keys=letra
    print(dic)
    
#letras(palavra)

#Exercício 3

def letras(string):
    dic={}
    letra=string.split()
    print(letra)
    #for letra in dic:
     #   print(dic)

letras("Este é um teste")
