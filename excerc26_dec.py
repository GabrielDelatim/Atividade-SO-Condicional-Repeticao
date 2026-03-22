#Receba 2 números inteiros. Verifique e mostre se o maior número é multiplo do menor.

#Declaração

n1: int=0
n2: int=0

#Início

n1 = int(input("Insira o primeiro número:"))
n2 = int(input("Insira o segundo número:"))

if (n1 > n2):
    if (n1%n2 == 0):
        print("O número maior,", n1, " é multiplo do número menor ", n2)
    else:
        print("O número maior,", n1, " não é multiplo do número menor ", n2)
else:
    if (n2%n1 == 0):
        print("O número maior,", n2, " é multiplo do número menor ", n1)
    else:
        print("O número maior,", n2, " não é multiplo do número menor ", n1)

#Fim 