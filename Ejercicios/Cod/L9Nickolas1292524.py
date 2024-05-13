print ("Ejercicio 1: operaciones aritmeticas")
n1 = input("insertar un numero:\n")
n2 = input("insertar otro numero:\n")
n1 = (int(n1))
n2 = (int(n2))
r1 = n1+n2
r2 = n1-n2
r3 = n1*n2
r4 = n1/n2
r5 = n1%n2
print(n1, "+", n2, "=", r1)
print(n1, "-", n2, "=", r2)
print(n1, "*", n2, "=", r3)
print(n1, "/", n2, "=", r4)
print( n1, "/",n1, f"= {r4:.2f}")
print(n1, "%", n2,"=", r5)

print ("Ejercicio 2: operaciones booleanas")
r1=bool(r1)
r2=bool(r2)
r3=bool(r3)
r4=bool(r4)
n1= str(n1)
n2= str(n2)
r1= n1>n2
r2= n1<n2
r3= n1==n2
r4= n1!=n2

print(n1, ">", n2, "=", r1)
print(n1, "<", n2, "=", r2)
print(n1, "=", n2, "=", r3)
print(n1, "!=", n2, "=", r4)

a = input("insertar un numero:\n")
b = input("insertar otro numero:\n")
c = input("insertar otro numero otra vez:\n")
a = (int(a))
b = (int(b))
c= (int(c))
a1 = (a*b)+c
a2 = a*(b+c)
a3 = a/(b+c)
a4 = (3*a+2*b)/c**2
print(a1)
print(a2)
print(a3)
print(a4)