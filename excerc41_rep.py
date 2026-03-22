#possibilidades da soma de dois dados com resultado 7 

#Declarar
contador: int=0

#Inicio

for i in range (1,7):
    
    for j in range (1,7):
        if i+j == 7:
            print (f"{i}+{j}={i+j}")
            contador +=1
print("Total de combinações:",contador )