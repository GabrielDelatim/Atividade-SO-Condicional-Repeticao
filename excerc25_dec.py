#Calcular tempo de jogo de uma partida

#Declarar

h_inicio: int
h_final: int
mm_inicio: int
mm_final: int

#Inicio

h_inicio = int(input("Insira a hora inicial:"))
mm_inicio = int(input("Insira os minutos iniciais:"))
h_final = int(input("Insira a hora final:"))
mm_final = int(input("Insira os minutos finais:"))

if mm_final >= mm_inicio:
    minuto = mm_final - mm_inicio
    ajuste_hora = 0
else:
    minuto = (mm_final + 60) - mm_inicio
    ajuste_hora = 1

h_final_ajustada = h_final - ajuste_hora

if h_final_ajustada >= h_inicio:
    hora = h_final_ajustada - h_inicio
else:
    hora = (h_final_ajustada + 24) - h_inicio

print("Duração do jogo:", hora, "horas e", minuto, "minutos")