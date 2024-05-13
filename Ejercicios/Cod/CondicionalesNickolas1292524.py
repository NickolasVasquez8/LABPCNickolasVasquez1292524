#Problema 1
monto= int(input("Ingresese monto de compra"))
descuento=0
if (monto<0):
    print("Error, monto no valido")
else:
    if (monto<=400):
        descuento=0
    elif (400< monto <=1000):
        descuento=0.07
    elif (1000<monto<=5000):
        descuento=0.1
    elif (5000<monto<=15000):
        descuento=0.25
    else:
        descuento=0.25

    res= input("tiene codigo de descuento (s/n)")
    if (res== "si") or res=="sí" or res== "s":
        descuento= descuento +0.5
        monto= monto*(1-descuento)

        print("El precio final es "+ str(monto))
        print("Se le aplico descuento de: ", str(descuento))
    elif (res== "no") or res== "n":
        print("El precio final es "+ str(monto))
        print("Se le aplico descuento de: ", str(descuento))
    else:
        print("Error, respuesta no valida")

#Problema 2
print("Ingrese tipo el tipo de envio")
TipoEnvio= int(input("1. Motocicleta, 2. Vehiculo"))

if TipoEnvio!= 1 and TipoEnvio!=2:
    print("Error, tipo de envio no valido")
else:
    Km= int(input("Ingreso el numero de kilometros a recorrer"))
    if Km<=0:
        print("Error, Distancia no valida")
    else:
        if(TipoEnvio==1):
            CostoFijo =10
            if(Km<5):
                CostoVariable=Km*3
            elif (Km<10):
                CostoVariable=Km*2.5
            else:
                CostoVariable=Km*2
        if (TipoEnvio==2):
            CostoFijo=20
            if(Km<5):
                CostoVariable=Km*6
            elif (Km<10):
                CostoVariable=Km*5
            else:
                CostoVariable=Km*4
    CostoTotal= CostoFijo+ CostoVariable
    print("Su costo de envio es "+ str(CostoTotal)+ " quetzales")

#Problema 3
