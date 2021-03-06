# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:28:52 2018

@author: Thais Guerini
"""
"""
O programa tem como objetivo resolver os pêndulos simples e com mola, mostrando como 
resultado listas de valores obtidos através de uma integração numérica das equações de 
movimento em cada caso. Caso o usuário deseje também é possível analisar por meio de listas
a conservação de energia.
O ângulo inicial é medido com relação a vertical a direita e a origem do sistema
é dada no ponto (0,0).
Algumas condições iniciais, estão declaradas com valores arbitrários, caso deseje elas
devem ser alteradas na declaração das variáveis; as demais podem ser alteradas nas funções."""
import math
import matplotlib.pyplot as plot

"""Pêndulo simples"""

#Declaração de varíaveis 
g = 9.8                 # módulo da aceleração local padrão da gravidade
l = 1.0                 # comprimento do fio

# Declaração de listas vazias para incrementação de variáveis
t_list = []
theta_list = []
ax_list = []
az_list = []
a_list = []
vx_list = []
vz_list = []
v_list = []
x_list = []
z_list = []

#Atualização das listas de variáveis do problema
def update(tf):
    t=0                           #instante inicial
    theta = math.radians(60.0)   # ângulo inicial
    vx = 0                  # velocidade inicial no eixo x
    vz = 0                  # velocidade inicial no eixo z
    v = 0                   # velocidade inicial em módulo
    w = 0                   # velocidade inicial angular
    dt = 0.1                # intervalo de tempo
    x = l*math.sin(theta)        # calcula posição inicial no eixo x
    z = -l*math.cos(theta)       # calcula posição inicial no eixo z
    
    while(t < tf):
        t_list.append(t)
        theta_list.append(math.degrees(theta))
        vx_list.append(vx)
        vz_list.append(vz)
        v_list.append(v)
        x_list.append(x)
        z_list.append(z)

        ax = -g*math.cos(theta)*math.sin(theta) - l*(w**2)*math.sin(theta)  
        az = g*(math.cos(theta)**2) - g + l*(w**2)*math.cos(theta)     
        a = (ax**2 + az**2)**(1/2)                            
        vx = l*w*math.cos(theta)                                   
        vz = -l*w*math.sin(theta)                                  
        v = l*w                                               
        x = l*math.sin(theta)                                      
        z = -l*math.cos(theta)                                     

        ax_list.append(ax)
        az_list.append(az)
        a_list.append(a)

        w = w -(g/l)*math.sin(theta)*dt                            
        theta = theta + w*dt                                  
        t = t + dt                                            

update(10)

#Valores de saída do pêndulo simples
def tabela():
    resposta1 = int(input('\n Gostaria de visualisar a lista de instantes para o pêndulo simples? [True == 1] '))
    if resposta1 == 1:
        print(t_list)
    resposta2 = int(input('\n Gostaria de visualisar a lista de ângulos para o pêndulo simples? [True == 1] '))
    if resposta2 == 1:
        print(theta_list)   
    resposta3 = int(input('\n Gostaria de visualisar a lista de aceleração para o pêndulo simples? [True == 1] '))
    if resposta3 == 1:
        print(a_list)    
    resposta4 = int(input('\n Gostaria de visualisar a lista de velocidade para o pêndulo simples? [True == 1] '))
    if resposta4 == 1:
        print(v_list)   
    resposta5 = int(input('\n Gostaria de visualisar a lista de valores de x para o pêndulo simples? [True == 1] '))
    if resposta5 == 1:
        print(x_list)   
    resposta6 = int(input('\n Gostaria de visualisar a lista de valores de z para o pêndulo simples? [True == 1] '))
    if resposta6 == 1:
        print(z_list)    
        
tabela()        
        
#Gráficos relativos ao pêndulo simples
fig = plot.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlabel('X axis')
ax.set_ylabel('-Z axis')

resposta7 = int(input('\n Gostaria de visualisar o gráfico de x vs z para o pêndulo simples? [True == 1] '))
if resposta7 == 1:
	plot.plot(x_list, z_list)
	plot.axis([(-l-0.25), (l+0.25), (-l-0.25), 0])
	plot.show()

resposta8 = int(input('Gostaria de visualisar o gráfico de a vs t para o pêndulo simples? [True == 1] '))
if resposta8 == 1:
	plot.plot(t_list, a_list)
	plot.show()

resposta9 = int(input('Gostaria de visualisar o gráfico de v vs t para o pêndulo simples? [True == 1] '))
if resposta9 == 1:
	plot.plot(t_list, v_list)
	plot.show()

resposta10 = int(input('Gostaria de visualisar o gráfico de vx vs x para o pêndulo simples? [True == 1] '))
if resposta10 == 1:
	plot.plot(x_list, vx_list)
	plot.show()

resposta11 = int(input('Gostaria de visualisar o gráfico de vz vs z para o pêndulo simples? [True == 1] '))
if resposta11 == 1:
	plot.plot(z_list, vz_list)
	plot.show()
    
#Conservação da energia
energia_list1=[]                 #declaração de lista vazia para a energia

tf=10                            #instante final
dt=0.1                           #variação entre os instantes
m=2                              #massa do objeto preso ao fio
def calcula_energia1(r,z,v):
    t=0
    while(t<tf):
        cinética = (1/2)*m*v**2                                           # energia cinética (J)
        potencial_grav = m*g*(-z)                                         # energia potencial gravitacional (J)
        energia = cinética + potencial_grav 
        energia = cinética + potencial_grav                               # energia mecânica
        energia_list1.append(energia)       # acrescenta a lista energia_lista o valor de energia
        t=t+dt

    resposta23 = int(input('Gostaria de visualisar os valores de energia para o pêndulo simples? [True == 1] '))
    if resposta23 == 1:
        print(energia_list1)
        
calcula_energia1(3,-1.41,1.41)

"""Com base na função calcula_energia podemos ver que a energia é conservada, uma vez
que não consideramos dissipação de energia pelo ar."""
    
"""Pêndulo com mola"""

#Declaração de varíaveis 
k=8                      # constante da mola
m=2                        # massa do corpo preso à extremidade inferior da mola
l0=2                     # comprimento inicial da mola
g=9.8                      # módulo da aceleração local padrão da gravidade

#Declaração das listas correspondentes às variáveis do problema
t_list2 = []
theta_list2 = []
ax_list2 = []
az_list2 = []
a_list2 = []
vx_list2 = []
vz_list2 = []
v_list2 = []
x_list2 = []
z_list2 = []

#Atualização das listas relativas às variáveis do problema

def update_mola(tf,x2,z2):
    w2 = 0                     # velocidade angular inicial
    vx2 = 0                    # velocidade inicial no eixo x
    vz2 = 0                    # velocidade inicial no eixo z
    v2 = 0                     # velocidade inicial em módulo
    
    t = 0                      # instante inicial
    dt2= 0.001                     # variação temporal
    r=3                      # comprimento distendido da mola
    #theta = math.radians(5.7)   #ângulo inicial
    theta=0.1                    #ângulo inicial em radianos
    x2 = r*math.sin(theta)        # calcula a posição inicial no eixo x
    z2 = -r*math.cos(theta)       # calcula a posição inicial no eixo z
    ax2 = -(k/m)*(r-l0)*math.sin(theta)   # calcula a aceleração inicial no eixo x
    
    while(t < tf):
        ax2 = -(k/m)*(r-l0)*math.sin(theta)
        az2 = -g+(k/m)*(r-l0)*math.cos(theta)
        a2 = (ax2**2 + az2**2)**(1/2)
        t_list2.append(t)
        theta_list2.append(math.degrees(theta))
        vx2 = vx2+(ax2)*dt2
        vz2 = vz2+(az2)*dt2
        v2 = (vx2**2 + vz2**2)**(1/2)
        vx_list2.append(vx2)
        vz_list2.append(vz2)
        v_list2.append(v2)
        x_list2.append(x2)
        z_list2.append(z2)
        r = math.sqrt( x2**2 + z2**2 )
                                                    
        x2 =r*math.sin(theta)                                    
        z2 = -r*math.cos(theta)                                     
        ax_list2.append(ax2)
        az_list2.append(az2)
        a_list2.append(a2)
        w2 = w2 -(g/(r-l0))*math.sin(theta)*dt2
        theta = theta + w2*dt2 
                                              
        t = t + dt2
   
update_mola(30,1.41,-1.41)     

#Valores de saída 
def tabela():
    resposta12 = int(input('\n Gostaria de visualisar a lista de instantes para o pêndulo com mola? [True == 1] '))
    if resposta12 == 1:
        print(t_list2)
    resposta13 = int(input('\n Gostaria de visualisar a lista de ângulos para o pêndulo com mola? [True == 1] '))
    if resposta13 == 1:
        print(theta_list2)   
    resposta14 = int(input('\n Gostaria de visualisar a lista de aceleração para o pêndulo com mola? [True == 1] '))
    if resposta14 == 1:
        print(a_list2)    
    resposta15 = int(input('\n Gostaria de visualisar a lista de velocidade para o pêndulo com mola? [True == 1] '))
    if resposta15 == 1:
        print(v_list2)   
    resposta16 = int(input('\n Gostaria de visualisar a lista de valores de x para o pêndulo com mola? [True == 1] '))
    if resposta16 == 1:
        print(x_list2)   
    resposta17 = int(input('\n Gostaria de visualisar a lista de valores de z para o pêndulo com mola? [True == 1] '))
    if resposta17 == 1:
        print(z_list2) 
    
tabela()

#Gráficos relativos ao pêndulo com mola
fig = plot.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlabel('X axis')
ax.set_ylabel('-Z axis')

resposta18 = int(input('\n Gostaria de visualisar o gráfico de x vs z para o pêndulo com mola? [True == 1] '))
if resposta18 == 1:
	plot.plot(x_list2, z_list2)
	#plot.axis([(-l-0.25), (l+0.25), (-l-0.25), 0])
	plot.show()

resposta19 = int(input('Gostaria de visualisar o gráfico de a vs t para o pêndulo com mola? [True == 1] '))
if resposta19 == 1:
	plot.plot(t_list2, a_list2)
	plot.show()

resposta20 = int(input('Gostaria de visualisar o gráfico de v vs t para o pêndulo com mola? [True == 1] '))
if resposta20 == 1:
	plot.plot(t_list2, v_list2)
	plot.show()

resposta21 = int(input('Gostaria de visualisar o gráfico de vx vs x para o pêndulo com mola? [True == 1] '))
if resposta21 == 1:
	plot.plot(x_list2, vx_list2)
	plot.show()

resposta22 = int(input('Gostaria de visualisar o gráfico de vz vs z para o pêndulo com mola? [True == 1] '))
if resposta22 == 1:
	plot.plot(z_list2, vz_list2)
	plot.show()
    
#Conservação da energia
energia_list=[]

tf=30                                              # instante final
dt2=0.001                                          #intervalo de tempo entre os instantes

def calcula_energia(r,z,v):
    t=0                                            #instante inicial
    while(t<tf):
        cinética = (1/2)*m*v**2                                   # energia cinética
        potencial_grav = m*g*(l0-z)                               # energia potencial gravitacional
        potencial_elast = (1/2)*k*(l0-r)**2                      # energia potencial elástica
        energia = cinética + potencial_grav + potencial_elast    # energia mecânica
        energia_list.append(energia)       # acrescenta a lista energia_lista o valor de energia
        t=t+dt2
    
    resposta24 = int(input('Gostaria de visualisar os valores de energia para o pêndulo com mola? [True == 1] '))
    if resposta24 == 1:
        print(energia_list)

calcula_energia(3,-1.41,1.41)

""" Com base na função calcula_energia podemos ver que a energia é conservada, uma vez
que não consideramos dissipação de energia pelo ar."""