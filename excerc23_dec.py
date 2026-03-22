#Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente. 

#Declarar 

n1: int
n2: int
n3: int
n4: int

#Procedimento mostrar números em em ordem crescente

def mostr_num():
    if (n4 < n1):
        print (n4,n1,n2,n3)
    elif(n4 < n2):
        print (n1,n4,n2,n3)
    elif(n4 < n3):
        print (n1,n2,n4,n3)
    else:
        print(n1,n2,n3,n4)
None
#Início Progama Principal

n1 = int(input("Insira o primeiro valor:"))
n2 = int(input("Insira o segundo valor:"))
n3 = int(input("Insira o terceiro valor:"))
n4 = int(input("Insira o quarto valor:"))

mostr_num()

#Fim

