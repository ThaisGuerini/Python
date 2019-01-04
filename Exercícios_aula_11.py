# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:38:33 2018

@author: thais
"""
"""para integração numerica primeiro det a funçao e o intervalo de integração"""

#Exercício 1
import math
def int_num():
    x=range(0,10)
    y=[math.exp(-xi) for xi in x]
    s=0
    for xi in x:
        s=s+math.exp(-xi)*0.01
    print("Soma 1000 caixinhas é", s)
int_num()

#Exercício 2
def int_num_dir():
    x=range(1,11)
    y=[math.exp(-xi) for xi in x]
    s=0
    for xi in x:
        s=s+math.exp(-xi)*0.01
    print("Soma 1000 caixinhas é", s)
int_num_dir()

#Exercício 3
def int_trap():
    x=range(0,10)
    s=0
    for xi in x:
        s=(int_num()+int_num_dir())/2*0.01
    print("Soma 1000 caixinhas é", s)
int_trap()    
    
    
    x=range(0,10)
    y=[math.exp(-xi) for xi in x]
    s=0
    for xi in x:
        s= (s+)/2*0.01