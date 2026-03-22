#Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3. 

#Declaração de variáveis

N:int = 0

#Início

N = int(input("Insira um número:"))

if ((N%6) == 0):
    print ("O número é divisível por 2 e 3")
else:
    print ("O número não é divisível por 2 e 3")
    
#Fim