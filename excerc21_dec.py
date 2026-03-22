#Calculo da média de 4 notas bimestrais 

#Programa calculo da média

def calc_media():
    
    med =  ((N1 + N2 + N3 + N4)/4) 
    if (med >= 6):
        print ("Aprovado, sua média foi ", med)
    elif (med >= 3):
        print ("Exame, sua média foi ", med)
    else:
        print ("Retido, sua média foi ", med)
None

#Programa principal

N1= float(input("Insira a primeira nota:"))
N2 = float(input("Insira a segunda nota:"))
N3 = float(input("Insira a terceira nota:"))
N4 = float(input("Insira a quarta nota:"))

calc_media()

#Fim