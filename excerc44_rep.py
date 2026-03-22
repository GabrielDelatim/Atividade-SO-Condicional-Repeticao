#Calculo de potência

#Declarar
base: float = 0
exp: int = 0
result: float = 1

#Início

base = float(input("Insira a base:"))
exp = int(input("Insira o expoente:"))

if (base == 0 and exp < 0):
    print("Erro: divisão por zero!")
else:
    if (exp > 0):
        for i in range(exp):
            result *= base
    
    elif (exp < 0):
        for i in range(-exp):
            result *= base
        result = 1 / result
    
    else:
        result = 1 
        
    print(result)