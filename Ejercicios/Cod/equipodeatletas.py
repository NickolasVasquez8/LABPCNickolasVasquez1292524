n1=input("ingrese el tiempo qu integrante 1 le llevo recorrer 100mts \n")
n2=input("ingrese el tiempo qu integrante 2 le llevo recorrer 100mts \n")
n3=input("ingrese el tiempo qu integrante 3 le llevo recorrer 100mts \n")
n4=input("ingrese el tiempo qu integrante 4 le llevo recorrer 100mts \n")

n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)

nr1= 100/n1
nr2= 100/n2
nr3= 100/n3
nr4= 100/n4

r1= (n1+n2+n3+n4)/4

print(f"La velocidad promedio del equipo de 4 integrantes es: {r1:.2f}")