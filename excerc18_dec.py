#Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menos valor.

#Declarar
N1: int=0
N2: int=0

#Início

N1 =int (input("Insira o primeiro número:"))
N2 = int(input("Insira o segundo número:"))

if (N1 > N2):
    print ("A diferença do maior pelo menor é", N1 - N2) 
elif (N1 < N2):
    print ("A diferença do maior pelo menor é", N2 - N1) 
else: 
    print ("A diferença do maior pelo menor é", N2 - N1)
    
#Fim
    
