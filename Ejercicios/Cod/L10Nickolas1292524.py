print( "Semana No. 10: Ejercicio 1")

mes= int(input("Ingrese numero del 1 a 12 \n"))
Msa=""
match mes:
    case 1:
     Msa= "enero"
    case 2:
        Msa= "febrero"
    case 3:
        Msa= "marzo"
    case 4:
        Msa= "abril"
    case 5:
     Msa= "mayo"
    case 6:
        Msa= "junio"
    case 7:
        Msa= "julio"
    case 8:
     Msa= "agosto"
    case 9:
     Msa= "septiembre"
    case 10:
        Msa= "octubre"
    case 11:
        Msa= "noviembre"
    case 12:
       Msa= "diciembre"
    case _:
      print("Error: El número a ingresar debe estar contenido entre 1 y 12")
print("Mes:", Msa)

print( "Semana No. 10: Ejercicio 1")
n1= int(input("Ingrese numero A: \n"))
n2= int(input("Ingrese numero B: \n"))
n3= int(input("Ingrese numero C: \n"))

if(n1<=0 and n2<=0 and n3<=0):
   print ("Error ingrese numeros mayores a 0")

if (n1>n2):
    if (n1>n3):
       print("A es el mayor")
    else:
       if (n1==n3):
        print ("A es mayor a B, A es igual a C")
       else: 
        print("A es mayor a B y menor a C")
elif (n1==n2):
   if (n1>n3):
      print("A es igual a B y A es mayor a C")
   else:
      if(n1==n3):
        print("Todos son iguales")
      else:
         print("A es igual a B y A es menor a C")
elif (n2>n3):
   print("B es mayor a A y C")
else:
   if(n2==n3):
    print("B igual a C y B mayor que A")
   else:
      print("B mayor A y A igual C")