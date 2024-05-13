a=0
a=int(input("Ingrese la cantidad de edades que va a ingresar \n"))
N=[]
i=0
r=0
lim=int(input("Ingrese la edad minima"))
while i<a:
   e=int(input("Ingrese edad: "))
   if e>0:
       N.append(e)
       i+=1
   else:
       print("ingrese numero valido") 
i=0
r=0
for i in N:
    if(i>=lim):
       r+=1

print("Hay, "+str(r)+ " mayores a "+str(lim))