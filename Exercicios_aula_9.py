# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:51:08 2018

@author: thais
"""

#Exercício 1
dfin=5 #distancias em km
v=12 #Velocidade em km/h
lista=[]
delta_t=1/60
def distancia(dfin):
    t=0
    d=0
    tfin=dfin*v
    while t<tfin:
        t=t+delta_t
        d=d+v*delta_t
        lista.append(d)
               
    print(lista)
    return lista

distancia(dfin)

#Exercício 2
#ERRADO
d1=0.2 #distancia em km
v1=15 #velocidade em km/h
delta_d_cte=5 #distancia em km
lista=[]
def dist_1(d_MUV):
    v0=0
    d1=v0*t+a+t**2/2
    v1=v0+a*t

def dist_2(df):
    t=0
    d=d1
    tfin=df*v1
    while t<tf:
        t=t+delta_t
        d=d+v1*delta_t
        lista.append(d)
    print(lista)
    return lista

#Exercício 3
#Utilizando a aproximação de ângulos pequenos, em que cos(theta)~1.
def dist_x(tfin):
    lista=[]
    x=0
    g=9.8 #g em m/s^2
    delta_t=1/60
    t=0
    while t<tfin:
        t=t+delta_t
        x=x+g*t**2/2
        lista.append(x)
    print(lista)
    
dist_x(10)
    