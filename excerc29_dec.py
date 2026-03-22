#calculo de rendimento de investimento

#Declarar

valor: float = 0.0
tipo: int = 0

#Início

valor = float(input("Insira o valor investido:"))
tipo = int(input("Insira 1 para poupança ou 2 para renda fixa:"))

if(tipo == 1):
    print(f"O valor investido na poupança corrigido em 30 dias é R${(valor*1.03):.2f}")
elif(tipo == 2):
    print(f"O valor investido na renda fixa corrigido em 30 dias é R${(valor*1.05):.2f}")
else:
    print("Tipo de investimento inválido")
    
#Fim