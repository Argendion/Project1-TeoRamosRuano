#Importar librerias
#import pandas as pd

#Variables
espera = float(0)
avanzado = float(0)


def CheckAction():
    print("Avanzamos? = 0")
    print("Esperamos? = 1")
    print("Hemos llegado a nuestro destino? = 2")
    inicioString = int(input("Responde: "))
    CountCM(inicioString)


def CountCM(m=int):
    val = True
    if m == 0:
        n = float(input("cuanto tiempo avanzamos?: "))*5
        avanzado = avanzado + n
    elif m == 1:
        n = float(input("cuanto tiempo esperamos: "))*2
        espera = espera + n
    else:
        print(f"El recorrido a consistido de {avanzado}s de recorrido y {espera}s de espera")
        tot = float((espera*2 + avanzado*5)/100)
        print(f"El viaje le sale a {tot}€")
        res = input("Iniciar nuevo trayecto? S/N: ")
        if res == "S" or res == "s":
            print("introduzca ruta:")
        else:
            print("Hasta la proxima, que tenga un vuen día")
            val=False
    if val:
        CheckAction()
    
    

#Begining
print("Bienvenido, vas a iniciar un trayecto con este taxi esperamos que sea dde su agrado")
print("introduzca ruta:")
CheckAction()
