#Calcular fatorial

#Declarar

n: int=0
cont: int=1
result: int=1

#Início

n = int(input("Insira um número:"))

while(cont <= n):
    result = result*cont
    cont +=1

print(result)

#Fim 