#Soma de números impares entre dois valores

#Declarar

n1: int= 0
n2: int= 0
result: int=0

#Início 

n1 = int(input("Insira o primero número:"))
n2 = int(input("Insira o segundo número:"))

if(n1>n2):
    n1,n2 = n2,n1

for i in range (n1, n2+1):
    if(i%2 != 0):
        result = result+i

print (result)
