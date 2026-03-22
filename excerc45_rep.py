# Calcular série 1 – 2/4 + 3/9 – 4/16 + 5/25 -... + 15/225

# Declarar
result = 1

# Início
print(f"Resultado da série: {result}")

for i in range(2, 16):
    if i % 2 == 0:   
        result -= i / (i * i)
    else:            
        result += i / (i * i)
    
    print(f"Resultado da série: {result:.3f}")