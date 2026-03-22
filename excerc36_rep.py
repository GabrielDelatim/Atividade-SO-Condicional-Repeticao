#Calcular serie 1/N!

#Declarar
n: int=0
result: int=0

#Início

n = int(input("Insira um número:"))

result = 0

for i in range(1, n + 1):
    fatorial = 1  
    
    for j in range(1, i + 1):
        fatorial *= j
    
    result += 1 / fatorial
    print(result)
 