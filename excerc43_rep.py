# Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria 
# sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

#Declarar

a = 1.1
m = 1.5
contador=0

#Início

print(f"Ano {contador}, Ana mede {a}m e Maria mede {m}m ")

while (a<=m):
    a += 0.03
    m += 0.02
    contador += 1
    print(f"Ano {contador}, Ana mede {a:.2f}m e Maria mede {m:.2f}m ")
print(f"Total de {contador} anos para Ana ser maior que maria ")



