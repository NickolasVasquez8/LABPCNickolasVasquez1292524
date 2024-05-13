print("#1")
edad= input("Escriba su edad: \n")
edad=int(edad)
if (edad<=0 or edad>=150):
    print("Edad no valida")
elif (edad>=18):
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")


print("#2")
nota= int((input("ingrese su nota: \n")))
if (nota>100 or nota<0):
    print("Nota no valida")
elif (nota>65):
    print("aprovo")
else:
    print("no aprovo")


print("#3")
try:
    nota= int((input("ingrese su nota: \n")))
    if (nota>100 or nota<0):
        print("Nota no valida")
    elif (nota>80 and nota<=100):
        print("Facultad 1")
    elif (nota>60 and nota<=80):
        print("Facultad 2")
    elif (nota>40 and nota<=60):
        print("Facultad 3")
    elif (nota>20 and nota<=40):
        print("Facultad 4")
    elif (nota>=0 and nota<=20):
        print("Facultad 5")
except ValueError:
    print("Por favor ingresar numero valido")
print("#4")
try:
    n= int((input("ingrese un numero: \n")))
    if (n%2==0):
        print("numero par")
    else:
        print("numero impar")
except ValueError:
    print("Por favor ingresar numero valido")
print("#5")
try:
    n= int((input("ingrese un numero: \n")))
    if (n==0):
        print("numero neutro")
    elif (n>0):
        print("numero positivo")
    else:
        print("numero negativo")
except ValueError:
    print("Por favor ingresar numero valido")