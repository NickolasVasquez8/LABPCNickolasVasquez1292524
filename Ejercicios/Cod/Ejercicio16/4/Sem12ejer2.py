X=0
Y=0

def move(cantx,canty):
    global X, Y
    X+=cantx
    Y+=canty

op=""
while op!="a" or op!="b" or op!="c" or op!="d" or op!="e" :
    op=str(input("Ingrese un numero para seleccionar sus opciones \n a. Sube \n b. Baja \n c. Izquierda \n d. Derecha \n e. Salir \n"))
    match op:
        case "a":
            (move(0,1))
        case "b":
            (move(0,-1))
        case "c":
            (move(-1,0))
        case "d":
            (move(1,0))
        case "e":
            break
        case _:
            print("Opcion no valida intente de nuevo")

print("LAs coordenadas del personaje son: ("+str(X)+","+str(Y)+")")