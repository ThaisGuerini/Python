#Exercício 1
def conj_collatz(n):
    while n>1:
        if n % 2==1:
            n=3*n+1
        else:
            n=n/2
    return n

#print(conj_collatz(13))
#print(conj_collatz(20))

#Exercício 2
def counter_0_5(n):
    count = 0
    k=n
    while k!=0:
        i=k%10
        k=k//10
        if i==0 or i==5:
            count = count + 1
                          
    return count

#print(counter_0_5(123456))
#print(counter_0_5(1010105))

#Exercício 3
def imprimir_pares(xs):
    for i in xs:
           if i % 2 == 1:  
              break        
           print(i)
    print("done")
    
#imprimir_pares([2,4,7,8])

#Exercício 4
def raiz_quadrada(n):
    aprox=n/2
    melhor=1
    while abs(melhor-aprox)>0.001:
        aprox=melhor
        melhor=(aprox+n/aprox)/2
    print(melhor)       
    return melhor
    
raiz_quadrada(9)
raiz_quadrada(16)


