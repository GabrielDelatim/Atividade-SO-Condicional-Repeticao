#Calcular quantidade de grãos contidos em um tabuleiro de xadrez

#Declarar

casa: int=1
qtd: int=1

#Início

for casa in range (casa,64+1, +1):
    print(f"A {casa}ª contém {qtd} grãos")
    qtd *= 2
    
#Fim
