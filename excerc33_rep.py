#Calcular serie 1/N

#Declarar
n: int=0
cont: int=0
result: int=0

#Início

n = int(input("Insira um número:"))

for i in range (1 , n+1):
    result = result + (1/i)
    print(result)