#Importar librerias

#Testing framework
import unittest
import random
#Import where we whannt to test
from taximetro import calcular_costo

#Variables
espera = float(0)
avanzado = float(0)
tripCost = float(0)

valueWait = float(2)
valueMove = float(5)

firstTime = True

def StartRute(SRval):
    # Hay que usar global [???] si editas los valores
    global espera,avanzado,tripCost,firstTime
    espera=0
    avanzado=0

    while SRval:
        if firstTime:
            print("Bienvenido a TaxisF5 que quiere iniciar un viaje?")
            firstTime = False
        else:
            print("Quiere iniciar un nuevo viaje?")
        sino = input("s/n: ")
        if sino == "s" or sino == "S": 
            SRval = CheckAction(True)
        else:
            SRval = False
    print("Gracias por viajar con TaxisF5 hasta la proxima")
        

def CheckAction(CAval) -> bool:
    while CAval:
        # Cambiar tarifa
        print(f"La tarifa actual es {valueWait}cen/s en espera y {valueMove}cent/s en movimiento")
        nVal = input("Si quieres cambiarlo ingrese 's': ")
        if nVal == "S" or nVal == "s":
            CheckPrices()
        CAval = CountCM()
    return CAval
    


def CountCM() -> bool:
    global valueMove,valueWait,tripCost,avanzado,espera
    print("Avanzamos? = 0")
    print("Esperamos? = 1")
    print("Hemos llegado a nuestro destino? = q")
    m = input("Responde: ")
    if m == "0":
        n = float(input("cuanto tiempo avanzamos?: "))
        print(f"avanzamos {n}s con una tarifa de: {valueMove} tramo cuesta {n*valueMove}")
        tripCost += calcular_costo("mov", n, valueWait, valueMove)
        print(f"Coste total del viaje de momento = {tripCost/100}€")
        avanzado += n
        return True
    elif m == "1":
        n = float(input("cuanto tiempo esperamos: "))
        print(f"esperamos {n}s con una tarifa de: {valueWait} tramo cuesta {n*valueWait}")
        tripCost += calcular_costo("wai", n, valueWait, valueMove)
        print(f"Coste total del viaje de momento = {tripCost/100}€")
        espera += n
        return True
    elif m == "q":
        print(f"El viaje ha consistido de {avanzado}s de recorrido y {espera}s de espera")
        tot = float(espera*valueWait/100 + avanzado*valueMove/100)
        print(f"El viaje le sale a {tot}€")
        return False
    
# Separating the calculations from the rest of the code is necesay for testing to work
def calcular_costo(modo, t, tar_wai, tar_mov):
    """
    Calcula el coste basado en el tipo de acción y tiempo.
    
    modo: 'espera' o 'movimiento'
    tiempo: segundos
    tarifa_espera: cent/seg
    tarifa_movimiento: cent/seg
    """
    if modo == 'wai':
        return t * tar_wai
    elif modo == 'mov':
        return t * tar_mov
    else:
        raise ValueError("Modo inválido")

def CheckPrices():
    global espera,avanzado,tripCost,valueMove,valueWait
    valueWait = float(input("Inserta el valor actual de ESPERAR en cent/seg: "))
    valueMove = float(input("Inserta el valor actual de MOOVERSE en cent/seg: "))

# Unitest {class -> }
# unittest.TestCase -> gives class acces to specific tessting methods that i need [???]
class TestCounterClass(unittest.TestCase):
    def test_random_movimiento(self):
        # Use random numbers for more acurate testing
        for _ in range(10):  
            tiempo = random.randint(1, 100)             
            tarifa = random.randint(1, 10)              
            esperado = tiempo * tarifa
            resultado = calcular_costo('mov', tiempo, 0, tarifa)
            self.assertEqual(resultado, esperado)
    
    def test_random_espera(self):
        for _ in range(10):
            tiempo = random.randint(1, 100)
            tarifa = random.randint(1, 10)
            esperado = tiempo * tarifa
            resultado = calcular_costo('wai', tiempo, tarifa, 0)
            self.assertEqual(resultado, esperado)
    
    def test_error_modo(self):
        # Verificamos que se lanza un error si el modo es incorrecto
        with self.assertRaises(ValueError):
            calcular_costo('volar', 10, 2, 5)

if __name__ == '__main__':
    unittest.main()
#Begin
StartRute()
