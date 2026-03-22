#Calculo de velocidade média de um circuito

#Declarar

voltas: float=0
durac_minutos: float=0
extenc: float=0

#Início

while(extenc <=0):
    extenc = float(input("Insira a extensão do circuito em metros:"))
    if (extenc <= 0):
        print("Insira apenas valores positivos!")
        
while(voltas <=0):
    voltas = float(input("Insira o número de voltas:"))
    if (voltas <= 0):
        print("Insira apenas valores positivos!")
        
while(durac_minutos <=0): 
    durac_minutos = float(input("Insira a duração em minutos:"))
    if (durac_minutos <= 0):
        print("Insira apenas valores positivos!") 

distancia_km = (voltas * extenc) / 1000

durac_horas = durac_minutos / 60

vel_media = distancia_km / durac_horas

print(f"Velocidade média: {vel_media:.2f} km/h")

#Fim
