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
n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese un numero: "))

print("La suma es: "+str(Sumar(n1,n2)))
print("La resta es: "+str(Restar(n1,n2)))
print("La multiplicacion es: "+str(Mult(n1,n2)))
print("La divicion es: "+str(Dividir(n1,n2)))