print("Semana No.12; Ejercicio 1")
op=str(input("ingrese una opcion \n a. Sumatoria \n b. Factorial \n c. Tablas de Multiplicas\n d. Numero perfeto \n"))
i=0
r=1
titulofila=""
match op:
        case "a": 
          n=int(input("ingrese un numero entero positivo \n"))
          if (n>0):
             for i in range (1, n+1):
                 r += i
                
             print(f"la sumatoria es ", r)
          else:
              print("Numero no valido")
            
        case "b":
          n=int(input("ingrese un numero entero positivo \n"))
          if (n>0):
             for i in range (1, n+1):
                 r= r*i
             print(f"el factorial es ", r)
          else:
              print("Numero no valido")
              
        case "c":
          titulocol="\t"
          for i in range(1, 11):
              titulocol += str(i)+"\t"
          print(titulocol)
          textofila=""
          for fila in range(1,11):
              textofila = str(fila)+ "\t"
              for col in range (1,11):
                  textofila += str(fila*col)+"\t"

        case "d":
            n=int(input("ingrese un numero entero positivo \n")) 
            a=0
            for i in range(1, n//2+1):
                if (n%i ==0):
                    a += i
            if (a==n):
                print("el numero "+ str(n)+ " es perfecto")
            else:
                print("el numero "+ str(n)+ " no es perfecto")
        case _:
            print("valor no valido")