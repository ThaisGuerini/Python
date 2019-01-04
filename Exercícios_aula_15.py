# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:54:10 2018

@author: thais
"""

#Transposição de matriz
def transpor(A):
    #print(len(A))
    B=[]
    for i in range(len(A)):
        B.append(A[i])
    for i in range(len(A)):
        #print(i)
        k = A[i]
        for j in range(len(k)):
           B[i][j]=A[j][i]
    print(A)

transpor([[2,1,3],[4,5,6],[7,8,9]])
