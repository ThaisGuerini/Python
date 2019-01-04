# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:52:51 2018

@author: thais
"""

#Exercício 1
def ler_arquivos(nome):
    arq=open(nome)
    linhas=arq.readlines()
    #print(linhas)
    #print(arq.readline(0))
    coluna=[]
    for line in linhas:
        coluna= line.strip().split('\t')
        #print(coluna)
    dic={}
    for i in range(len(coluna)):
        dic[i]=[]
       
        #dic[i].append(coluna[i])
        
    for i in range(len(coluna)):
        for line in linhas:
            print(line)
            dic[i].append(coluna[i])
    print(dic)
    
    
ler_arquivos('dados_alunos.txt')