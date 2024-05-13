saludo = 'Hola Mundo'
print(saludo)
nom = input("ingrese su nombre:\n")
print("Hola", nom)

x=input("insertar un numero x:\n")
y=input("insertar un numero y:\n")
y = (int(y))
x = (int(x))
r1 = x+y
r2 = x-y
r3 = x*y
r4 = x/y
print("suma de", x, "y", y, "es", r1)
print("resta de", x, "y", y, "es", r2)
print("multiplicacion de", x, "y", y, "es", r3)
print("divicion de", x, "y", y, "es", r4)

n1 = input("insertar un numero:\n")
n2 = input("insertar otro numero:\n")
n1 = (int(n1))
n2 = (int(n2))
if (n1>n2):
    print(n1, "es mayor a", n2)
elif (n1==n2):
    print(n1, "y", n2 ,"son iguales")
else:
    print(n1, "es menor a", n2)