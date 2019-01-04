# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 12:17:05 2018

@author: thais
"""
class  MeuTempo0 : 
    # Métodos previamente definidos aqui ... 
    def  __init__ ( self ,  hrs = 0 ,  mins = 0 ,  segs = 0 ): 
        """ Criar um novo objeto MeuTempo inicializado para hrs, min, segs. 
           Os valores de mins e segs podem estar fora do intervalo de 0-59, 
           mas o objecto MeuTempo resultante será normalizado.  """ 
        # Calcular total de segundos para representar 
        self.totalsegs =  hrs * 3600  +  mins * 60  +  segs 
        self.horas =  self.totalsegs  //  3600         # Divisão em h, m, s 
        restosegs =  self.totalsegs  %  3600 
        self.minutos  =  restosegs  //  60 
        self.segundos  =  restosegs  %  60
        if self.horas >=24:
            self.horas = self.horas%24
    def  to_seconds ( self ): 
        "" "Retorna o número de segundos representados por esta instância " "" 
        return  self.totalsegs
    
    def  __sub__ ( self ,  other ): 
        """ Retorna a soma do tempo atual e outro, para utilizar com o simbolo + """
        return  MeuTempo0 ( 0 ,  0 ,  self.to_seconds()  -  other.to_seconds())
    
    def __str__(self):
        """Retorna uma representação do objeto como string, legível para humanos."""
        return '%.2d:%.2d:%.2d' % (self.horas, self.minutos, self.segundos)  
    
a=MeuTempo0(1,2,3)
b=MeuTempo0(0,0,50)
print(a-b)

#Exercício 1
class  MeuTempo : 
    # Métodos previamente definidos aqui ... 
    def  __init__ ( self ,  hrs = 0 ,  mins = 0 ,  segs = 0 ): 
        """ Criar um novo objeto MeuTempo inicializado para hrs, min, segs. 
           Os valores de mins e segs podem estar fora do intervalo de 0-59, 
           mas o objecto MeuTempo resultante será normalizado.  """ 
        # Calcular total de segundos para representar 
        self.totalsegs =  hrs * 3600  +  mins * 60  +  segs 
        self.horas =  self.totalsegs  //  3600         # Divisão em h, m, s 
        restosegs =  self.totalsegs  %  3600 
        self.minutos  =  restosegs  //  60 
        self.segundos  =  restosegs  %  60
        if self.horas >=24:
            self.horas = self.horas%24
            
    
            
    def  depois ( self ,  other ): 
        "" "Retorna True se self for estritamente maior que other" "" 
        return(self.totalsegs>other.totalsegs)
        
    def  antes ( self ,  other ): 
        "" "Retorna True se self for estritamente menor que other" "" 
        return(self.totalsegs<other.totalsegs)
        
    def  igual ( self ,  other ): 
        "" "Retorna True se self for estritamente maior que other" "" 
        return(self.totalsegs==other.totalsegs)
        
           
    def entre(self,t1,t2):
             
        if self.depois(t1) and self.antes(t2):
            return True

        if self.igual(t1) and self.antes(t2):
            return True
        else:
            return False

t=MeuTempo(10,30,40)
q=t.entre(MeuTempo(10,20,11),MeuTempo(10,55,15))
print(q)