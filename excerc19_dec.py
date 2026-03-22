#Receba 2 valores reais. Calcule e mostre o maior deles.

#Declarar
N1: float = 0.0
N2: float = 0.0

#Início

N1 = float(input("Insira o primeiro número:"))
N2 = float(input("Insira o segundo número:"))

if (N1 > N2):
    print ("O maior número é ", N1)
elif (N1 < N2):
    print ("O maior número é ", N2)
else:
    print ("Os valores são iguais.")
    
#Fim