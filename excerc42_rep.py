#Serie 1+2/3+3/5+...+50/99

# Declarar
soma: float = 1

# Início

print(f"Resultado da série: {soma}")

for i in range(2, 51):
    soma += i / (2*i - 1)
    print(f"Resultado da série: {soma:.4f}")
    