n=int(input("ingrese un numero entero positivo \n")) 
n2=int(input("ingrese otro numero entero positivo \n")) 
a=0
a1=0
if n<=0 and n2<=0:
    print("Numero o numeros no valido/s")
else:
    for i in range(1, n):
            if (n%i ==0):
                a += i
    for i in range(1, n2):
            if (n2%i ==0):
                a1 += i
                
    if n2==a and n==a1:
         print("los numeros "+str(n)+" y "+str(n2)+ " son amigos")
    else:
         print("los numeros "+str(n)+" y "+str(n2)+ " no son amigos")