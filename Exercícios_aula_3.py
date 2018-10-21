#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      thais
#
# Created:     19/10/2018
# Copyright:   (c) thais 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Exercicio 1

def funcao_tipo(x):
    print(x)
    print(type(x))

funcao_tipo(2)

#Exercício 2

def velocidade_media(s,s0,t):
     v=(s-s0)/t
     print(v)

def velocidade_MRUA(v0,a,t):
    v=v0+a*t
    print(v)

#Exercício 3

def ang_zenital(h,s):
     theta=s/h
     print(theta)

#Exercício 4

def milhas_metros(milhas):
     x=(milhas)*(1.61)*10**(3)
     print(x)

def metros_milhas(metros):
    x=(metros)/(1.61)*10**(3)
    print(x)

def horas_segundos(horas):
    t=(horas)*3600
    print(t)

def segundos_horas(segundos):
    t=(segundos)/3600
    print(t)

metros_milhas(10000)
segundos_horas(2610)

def tempo_medio(metros_milhas,segundos_horas):
    tm=(metros_milhas)/(segundos_horas)
    print(tm)

tempo_medio(10000,2610)

def velocidade_media_mi(metros_milhas,segundos_horas):
    vm=(metros_milhas)/(segundos_horas)
    print(vm)

velocidade_media_mi(10000,2610)


milhas_metros(4)

def velocidade_media_m(milhas_metros,segundo_horas):
    vm=(milhas_metros)/(segundos_horas)
    print(vm)

velocidade_media_m(4,1800)

def tempo_medio_km(milhas_metros,segundos_horas):
    tm_km=(milhas_metros)*1000/(segundos_horas)
    print(tm_km)

tempo_medio_km(4,1800)

#Exercício 5

#IMC
def IMC(m,h):
    IMC=m/(h**2)
    print(IMC)

IMC(70,1.78)

#volume da esfera
def volume(pi,r):
    vol=(4*(pi)*(r**3))/3
    print(vol)

volume(3.14,5)

#difração
def delta_y(comp_onda,D,d):
    delta_y=(comp_onda*D)/d
    print(delta_y)

delta_y(6.328e-07,1.98,0.00025)
