import math
n1=input("ingrese el radio de una circunferencia\n")
n1=float(n1)

r1= (math.pi*n1**2)
r2= (2*math.pi*n1)

print(f"El area de la circunferencia es: {r1:.2f}")
print(f"El perimetro de la circunferencia es: {r2:.2f}")