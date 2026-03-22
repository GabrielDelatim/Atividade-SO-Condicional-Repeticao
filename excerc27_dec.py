#Calculo de velocidade média de um circuito

#Declarar

voltas: float=0
durac_minutos: float=0
extenc: float=0

#Início

extenc = float(input("Insira a extensão do circuito em metros:"))
voltas = float(input("Insira o número de voltas:"))
durac_minutos = float(input("Insira a duração em minutos:"))

distancia_km = (voltas * extenc) / 1000

durac_horas = durac_minutos / 60

vel_media = distancia_km / durac_horas

print(f"Velocidade média: {vel_media:.2f} km/h")

#Fim