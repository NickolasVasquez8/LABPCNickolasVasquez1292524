def Fac(num1):
    r=1
    for i in range(1, num1+1):
        r=r*i
    return r

n=int(input("Ingrese numero para sacar su factorial \n"))
r=1
if n>=0:
    print("El factorial de "+str(n)+" es: "+str(Fac(n)))
else:
    print("Numero no valido")