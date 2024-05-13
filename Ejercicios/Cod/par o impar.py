print("#4")
try:
    n= int((input("ingrese un numero: \n")))
    if (n%2==0):
        print("numero par")
    else:
        print("numero impar")
except ValueError:
    print("Por favor ingresar numero valido")