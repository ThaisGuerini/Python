# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:05:21 2018

@author: thais
"""

#Exercício 1
def maximo(x,y,z):
    if(x>y>z):
        print("O máximo é",x)
    if(y>z>x):
        print("O máximo é",y)
    if(z>x>y):
        print("O máximo é",z)
    if(z>y>x):
        print("O máximo é",z)
    if(x>z>y):
        print("O máximo é",x)
    if(y>x>z):
        print("O máximo é",y)  
        
maximo(1,2,8)
maximo(12,15,20)

#Exercício 2
soma=1
def soma(x,y,z,w):
    lista=[x,y,z,w]
    soma= x+y+z+w
    print(lista)
    print(soma)

soma(1,2,3,4)
soma(10,20,30,40)

#Exercício 3
multiplicacao=1
def multiplicar(x,y,z,w):
    lista=[x,y,z,w]
    multiplicacao= x*y*z*w
    print(lista)
    print(multiplicacao)

multiplicar(1,2,3,4)

#Exercício 4
def intervalo(x,xi,xf):
    if (xi<x<xf):
        print("O número",x," pertence ao intervalo",[xi,xf])
    else:
        print("O número",x," não pertence ao intervalo",[xi,xf])
        
intervalo(5,1,10)
intervalo(8,1,3)

#Exercício 5
def pares(x,y,z,w,t):
    lista=[x,y,z,w,t]
    for i in lista:
        if i % 2==0:
            print("O número",i, "é par.")

pares(10,5,8,3,1)
pares(15,20,14,3,19)

#Exercício 6
#ERRADO
def divisores(x):
    i=1
    while i<=x:
        if x%i==0:
            print(i,"é divisor de ",x)
        i=i+1
        
divisores(6)

def n_perfeito(x):
    y=divisores(x)
    print(y)
    #if x==(y)/2:
        #print(x,"é um número perfeito.")
        
n_perfeito(6)
        
        