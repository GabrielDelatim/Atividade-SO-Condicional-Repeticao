#Serie Fibonacci

#Declarar 

n: int=0
a: int=0
b: int=1

#Início

n = int(input("Insira a quantidade de termos da serie:"))

for i in range(n):
    print(a)
    
    soma = a + b
    a = b
    b = soma
    
#Fim