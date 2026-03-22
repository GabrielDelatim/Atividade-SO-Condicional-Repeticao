#Calcular tabuada

#Declarar

n: int=0
result: int=0

#Início

n = int(input("Insira um número:"))

print("Tabuada do ", n)

for i in range (1,11):
    result = n*i
    print(i , "X", n , " = ",result) 