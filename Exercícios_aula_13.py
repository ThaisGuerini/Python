# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:20:21 2018

@author: thais
"""

#Exercício 1
idade=[]
altura=[]
massa=[]
def histograma(): 
    alunos=open('dados_alunos.txt')
    linhas=alunos.readlines()
    #print(linhas)
    for line in linhas:
        coluna= line.strip().split('\t')
        #print(coluna)
        idade.append(coluna[0])
        altura.append(coluna[1])
        massa.append(coluna[2])
    print(idade)
    print(altura)
    print(massa)
    
    #import matplotlib
    #fig=matplotlib.plot.figure()
    #matplotlib.plot.plot(idade)
    #matplotlib.plot.show()

histograma()

#Exercício 2


    



