# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 14:44:59 2019

@author: thais
"""

#Exercício 1

class Ponto1:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto1(mx, my)
    
    def para_string(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def distancia_entre_pontos(self,alvo2):
        """Calcula distancia entre dois pontos"""
        dx=(self.x-alvo2.x)
        dy=(self.y-alvo2.y)
        d= (dx**2+dy**2)**(0.5)
        return (d)

p=Ponto1(3,2)
q=Ponto1(4,5)
r=print(p.distancia_entre_pontos(q))

#Exercício 2

class Ponto2:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto2(mx, my)
    
    def para_string(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def reflexao_x(self):
        return"({0},{1})".format(self.x,-self.y)

p=Ponto2(3,2)
r=print(p.reflexao_x())

#Exercício 3
import math

class Ponto3:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto3(mx, my)
    
    def para_string(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def inclinacao_da_origem(self):
        """Retorna a inclinação da linha que liga o ponto à origem"""
        m=self.y/self.x
        return(m)

p=Ponto3(3,2)    
r=print(p.inclinacao_da_origem())

"""O que poderia dar de errado é com relação ao quadarante do ponto, pois 0<theta<pi/2"""

#Exercício 4
class Ponto4:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y

    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto4(mx, my)
    
    def para_string(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def parametros_reta(self,alvo3):
        a=(self.y-alvo3.y)/(self.x-alvo3.x)
        b=self.y-a*self.x 
        return "({0},{1})".format(a,b)
        
p=Ponto4(3,2)
q=Ponto4(4,5)
r=print(p.parametros_reta(q))
"""O problema poderia ser gerado caso tenhamos dois pontos em quadrantes distintos"""
