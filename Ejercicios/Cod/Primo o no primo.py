i=1
r=0
n1= int(input("Ingresese un numero entero positivo\n"))

if  n1>0:
    for i in range (1, n1+1):
        if n1%i==0:
            r+=1
    if r>2:
        print("El numero no es primo")
    else:
        print("El numero es primo")
else:
    print("ingrese un numero valido")