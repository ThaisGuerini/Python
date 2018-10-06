#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      thais
#
# Created:     06/10/2018
# Copyright:   (c) thais 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Exercício 1
largura=17
altura=12.0
delimitador="."

largura/2
8.5
type(largura/2)
<class 'float'>

largura/2.0
8.5
type(largura/2.0)
<class 'float'>

altura/3
4.0
type(altura/3)
<class 'float'>

1+2*5
11
type(1+2*5)
<class 'int'>

delimitador*5
'.....'
type(delimitador*5)
<class 'str'>

#Exercício 2
r=5
V=(4/3)*3.14*r**3
V
523.3333333333334

#Exercício 3
preço=24.95
preço_real=0.6*preço
preço_real
14.969999999999999
preço_total=preço_real+3+59*(preço_real+0.75)
preço_total
945.4499999999999

#Exercício 4
comprimento_de_onda=632.8
D=1.98
d=0.250
comprimento_de_onda_em_metros=632.8*10**-9
comprimento_de_onda_em_metros
6.328e-07
d=0.250*10**-3
d
0.00025
delta_y=comprimento_de_onda_em_metros*D/d
delta_y
0.005011776