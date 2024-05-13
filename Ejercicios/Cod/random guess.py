#Obtencion de variables e Imports
import random
secreto = random.randint(1,100)
r=0
turnsj1=0
turnsj2=0
j1=str(input("Ingrese nombre del jugador 1 \n"))
j2=str(input("Ingrese nombre del jugador 2 \n"))
#Proceso
while r!=secreto:
    #Turno de Jugador 2
    r=int(input("Jugador 1 " +str(j1)+" Ingrese su prediccion de un numero entre 1 y 100 \n"))
    turnsj1 +=1
    if r==secreto:
        print("Su prediccion fue acertada, Ganaste!!! ",j1, " se tomo: ", str(turnsj1), " intentos")
        break
    elif r<secreto:
        print("su prediccion es menor, intente de nuevo")
    elif r>secreto:
        print("su prediccion es mayor, intente de nuevo")
    #Turno de Jugador 2
    r=int(input("Jugador 2 " +str(j2)+" Ingrese su prediccion de un numero entre 1 y 100 \n"))
    turnsj2 +=1
    if r==secreto:
        print("Su prediccion fue acertada, Ganaste!!! ", j2, " se tomo: ", str(turnsj2), " intentos")
        break
    elif r<secreto:
        print("su prediccion es menor, intente de nuevo") 
    elif r>secreto:
        print("su prediccion es mayor, intente de nuevo")