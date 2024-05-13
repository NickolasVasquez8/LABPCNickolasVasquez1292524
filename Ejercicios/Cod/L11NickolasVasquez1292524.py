print("Semana No. 11: Ejercicio 1")

n= int(input("Ingrese numero mayor a 0\n"))
A=0
B=1
C=0
i=2
resultado= ""
if n <= 0:
    print("Error, el numero tiene que ser mayor a 0")
else:
    resultado= str(A)
    if n>1:
        resultado += ","+str(B)
        while i<n :
            C= A+B
            resultado += ","+ str(C)
            A=B
            B=C
            i=i+1
            if n==i:
                break
        print(resultado)
    else:
        print(resultado)

print("Semana No. 11: Ejercicio 2")
n2= int(input("Ingrese numero mayor a 0\n"))
a=0
b=0
c=0
i=1
if n2 <= 0:
    print("Error, el numero tiene que ser mayor a 0")
else:
    #Inciso A
    while i<=n2:
        a= a + 1/i
        i=i+1
    i=1
    print("El resultado del inciso A es: ", a)
    #Inciso B
    while i<=n2:
        b= b + 1/2**i
        i=i+1
    i=1
    print("El resultado del inciso B es: ", b)
    #inciso C
    x= int(input("Ingrese numero I\n"))
    a1= int(input("Ingrese numero II\n"))
    n3= int(input("Ingrese numero III\n"))
    for i in range(0, n3+1):
        c= c+(x**i)+a1**(n3-i)
    print("El resultado del inciso c es: ", c)