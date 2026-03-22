#Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço

#Declarar

preco = 0.0 
med_mensal = 0.0

#Início

preco = float(input("Insira o preço atual:"))
med_mensal = float(input("Insira a média mensal:"))

if ((med_mensal < 500) and (preco < 30.00)):
    print(f"O novo preço é {(preco*1.1):.2f}")
elif ((med_mensal >= 500 and med_mensal < 1000) and ( preco >= 30.00 and preco < 80.00)):
    print(f"O novo preço é {(preco*1.15):.2f}")
elif((med_mensal >= 1000)and(preco >= 80.00)):
    print(f"O novo preço é  {(preco*0.95):.2f}")
else:
    print(f"O preço se manterá {preco:.2f}")
    
#Fim
