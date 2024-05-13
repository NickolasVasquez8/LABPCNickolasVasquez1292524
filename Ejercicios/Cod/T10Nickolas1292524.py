print("Nickolas Vasquez \n", "1292524")
try:
    d=int(input("Ingresar dia de nacimiento en numeros \n"))
    m=int(input("ingresar mes de nacimiento en numeros \n"))
    a=int(input("Ingresar año de nacimiento en numeros \n"))
    match m:
        case 1:
         if d<=19:
            print("Capricornio")
         else:
            print("Acuario")
        case 2:
         if d<=18:
            print("Acuario")
         else:
            print("Piscis")   
        case 3:
           if d<=20:
            print("Piscis")
           else:
            print("Aries") 
        case 4:
           if d<=19:
            print("Aries")
           else:
            print("Tauro") 
        case 5:
           if d<=20:
            print("Tauro")
           else:
            print("Geminis") 
        case 6:
           if d<=20:
            print("Geminis")
           else:
            print("Cancer") 
        case 7:
           if d<=22:
            print("Cancer")
           else:
            print("Leo") 
        case 8:
           if d<=22:
            print("Leo")
           else:
            print("Virgo") 
        case 9:
           if d<=22:
            print("Virgo")
           else:
            print("Libra") 
        case 10:
           if d<=22:
            print("Libra")
           else:
            print("Escorpio") 
        case 11:
           if d<=22:
            print("Escorpio")
           else:
            print("Sagitario") 
        case 12:
           if d<=21:
            print("Sagitario")
           else:
             print("Capricornio") 
        case _:
            print("numero no valido")
except ValueError:
  print("Valor no valido")