#Receba 3 coeficientes A, B, e C de uma equação do 2o grau da fórmula AX2+BX+C=0. Verifique
#e mostre a existência de raízes reais e se caso exista, calcule e mostre.

import math

#Procedimento Calcular Equação do 2º Grau
def calc_equac():
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        raiz = -b / (2*a)
        print("A equação tem apenas uma raiz real:", raiz)
    else:
        raiz1 = (-b - math.sqrt(delta)) / (2*a)
        raiz2 = (-b + math.sqrt(delta)) / (2*a)
        print("As raízes da equação são:", raiz1, "e", raiz2)

# Programa principal
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

calc_equac()

#Fim