#Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

#declarar variáveis

n1:int = 0
n2:int = 0

# Início

n1 = int(input("Insira o primeiro número:"))
n2 = int(input("Insira o segundo número:"))

if (n1 < n2):
    print (n1,n2)
else:
    print (n2,n1)
    
#Fim