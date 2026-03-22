# Verificar números primos entre dois valores

# Declarar
n1: int = 0
n2: int = 0
i: int = 0
j: int = 0
primo: bool = True

# Início

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1 > n2:
    n1, n2 = n2, n1

print("Números primos entre", n1, "e", n2, ":")

for i in range (n1, n2+1):
    if i < 2:
        continue
    
    primo = True
    
    for j in range (2 , i):
        if i%j == 0:
            primo = False
            break
    if primo:
       print(i)