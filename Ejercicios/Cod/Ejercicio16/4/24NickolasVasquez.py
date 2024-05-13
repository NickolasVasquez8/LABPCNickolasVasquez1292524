a=0
a=int(input("Ingrese la cantidad de edades que va a ingresar \n"))
N=[]
i=0
r=0

while i<a:
   e=int(input("Ingrese numero: "))
   if e>0:
       N.append(e)
       i+=1
   else:
       print("ingrese numero valido") 

i=0

while i<a:
    if N[i]>N[r]:
        r = i
    i+=1

print("El mayor es: "+ str(N[r]))