# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:48:13 2018

@author: thais
"""

#Exercício 1
#Ítem (a)
def dobrar_elementos(uma_lista):
    """ Reescreve os elementos de uma_lista com o dobro de seus valores originais sem 
    alterar os valores originais de uma_lista.
    """
    clone_lista = uma_lista[:]

    for (i, valor) in enumerate(clone_lista):
        novo_elem = 2 * valor
        clone_lista[i] = novo_elem
    print(clone_lista)
    return clone_lista
    

minha_lista = [2, 4, 6]
print(minha_lista)
dobrar_elementos(minha_lista)

#Ítem (b)
help(dobrar_elementos)

#Exercício 2
lista=[]
for i in range(1,1001):
    lista.append(i)
print(lista)
    
#Exercício 3
def find(n):
    for i in range(101,n):
        if i>0:
            if i%21==0:
               print(i)
find(121)

#Exercício 4
def mat():
    lista=[-1,0,0,0]
    lista2=[0,1,0,0]
    lista3=[0,0,1,0]
    lista4=[0,0,0,1]
    list=[lista,lista2,lista3,lista4]
    print(list)
    print(lista3[2])
mat()
