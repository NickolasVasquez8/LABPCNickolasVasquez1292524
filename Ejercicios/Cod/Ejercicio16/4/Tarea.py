def Fac(num1):
    Total=1
    for i in range(1, num1+1):
        Total*=i
    return Total
def Sumar(num1,num2):
    Total=num1+num2
    return Total
def Restar(num1,num2):
    Total=num1-num2
    return Total
def Mult(num1,num2):
    Total=num1*num2
    return Total
def Dividir(num1,num2):
    Total=num1/num2
    return Total
def Root(num1):
    Total=num1**(1/2)
    return Total
def Pot(num1,num2):
    Total=num1**num2
    return Total
op=0
while op!=1 or op!=2 or op!=3 or op!=4 or op!=5 or op!=6:
    op=int(input("Ingrese un numero para seleccionar sus opciones \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Raiz cuadrada \n 6. Potencia \n 7. Factorial \n 8. Salir"))
    match op:
        case 1:
            n1=int(input("Ingrese numero para hacer suma "))
            n2=int(input("Ingrese numero para hacer suma "))
            print("La suma es: "+str(Sumar(n1,n2)))
        case 2:
            n1=int(input("Ingrese numero para hacer resta "))
            n2=int(input("Ingrese numero para hacer resta "))
            print("La resta es: "+str(Restar(n1,n2)))
        case 3:
            n1=int(input("Ingrese numero para hacer Multiplicacion "))
            n2=int(input("Ingrese numero para hacer Multiplicacion "))
            print("La multiplicacion es: "+str(Mult(n1,n2)))
        case 4:
            n1=int(input("Ingrese numero para hacer Dividir "))
            n2=int(input("Ingrese numero para hacer Dividir "))
            if n2==0:
                print("No se puede hacer la divicion")
            else: 
                print("La divicion es: "+str(Dividir(n1,n2)))
        case 5:
            n1=int(input("Ingrese numero para hacer Raiz cuadrada "))
            print("La raiz cuadrada es: "+str(Root(n1)))
        case 6:
            n1=int(input("Ingrese numero para la base "))
            n2=int(input("Ingrese numero para el exponente "))
            print("EL resultado es: "+str(Pot(n1,n2)))
        case 7:
            n=int(input("Ingrese numero para sacar su factorial \n"))
            print("El factorial de "+str(n)+" es: "+str(Fac(n)))
        case 8:
            break
        case _:
            print("Opcion no valida intente de nuevo")