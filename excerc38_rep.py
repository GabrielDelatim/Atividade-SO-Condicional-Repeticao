#Verificar maior e menor número da entrada de 100 de valores reais positivos

#Declarar

num: float = 0
maior: float = 0
menor: float = 0
contador: int = 0
tem_positivo: bool = False

# Início
while contador < 100:
    num = float(input(f"Digite o {contador + 1}º número: "))

    if num <= 0:
        print("Apenas números positivos são permitidos!\n")
        continue

    if not tem_positivo:
        maior = num
        menor = num
        tem_positivo = True
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    contador += 1

    print(f"Maior até agora: {maior}")
    print(f"Menor até agora: {menor}\n")
    
    #Fim