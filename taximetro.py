# Importar librerías necesarias
import unittest
import random

# Variables que contienen el estado del viaje y tarifas (en dictionaries)
trip = {
    "espera": float(0),
    "avanzado": float(0),
    "tripCost": float(0)
}

tarifs = {
    "valueWait": float(2),  # 2 cent/segundo por esperar
    "valueMove": float(5)   # 5 cent/segundo por moverse
}


# Inicia el flujo del viajes
def StartRute(SRval, SRtrip, SRtarifs, isTrueq):
    while SRval:
        # Mensaje de bienvenida o nuevo viaje
        if isTrueq:
            print("Bienvenido a TaxisF5, ¿quiere iniciar un viaje?")
            isTrueq = False
        else:
            print("¿Quiere iniciar un nuevo viaje?")

        sino = input("s/n: ")

        if sino.lower() == "s":
            SRtrip = {
                "espera": float(0),
                "avanzado": float(0),
                "tripCost": float(0)
            }
            # Comienza el ciclo del viaje
            SRval = CheckAction(SRval, SRtrip, SRtarifs)
        else:
            SRval = False

    print("Gracias por viajar con TaxisF5. Hasta la próxima.")


# Gestiona si se quiere cambiar tarifas y llama a la función que controla el viaje
def CheckAction(CAval, CAtrip, CAtarifs) -> bool:
    while CAval:
        print(f"Tarifa actual: {CAtarifs['valueWait']} cent/seg en espera, "
              f"{CAtarifs['valueMove']} cent/seg en movimiento")

        nVal = input("¿Desea cambiar las tarifas? (s/n): ")
        if nVal.lower() == "s":
            CheckPrices(CAtarifs)

        # Ejecuta el viaje en sí
        CAval = CountCM(CAtrip, CAtarifs)

    return True

def save_trip(trip):
    
    # Guarda los datos del viaje en un archivo de texto, o crea uno nuevo si no existe
    # Nombre, formato y contenido del archivo

    '''
``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
    '''

    #Count number of trips

# Controla el flujo del viaje: avanzar, esperar o finalizar
def CountCM(trip, tarifs) -> bool:
    # \n es un salto de línea
    print("\nAvanzamos = 0\nEsperamos = 1\nHemos llegado = q")
    m = input("Responde: ")

    if m == "0":
        # Movimiento del taxi
        try:
            n = float(input("¿Cuánto tiempo avanzamos (segundos)?: "))
            coste = CalcularCosto("mov", n, tarifs["valueWait"], tarifs["valueMove"])
            trip["avanzado"] += n
            trip["tripCost"] += coste
            print(f"Coste total actual: {trip['tripCost'] / 100:.2f}€")
        except ValueError as e:
            print(f"Error: {e}")
        return True

    elif m == "1":
        # Espera del taxi
        try:
            n = float(input("¿Cuánto tiempo esperamos (segundos)?: "))
            coste = CalcularCosto("wai", n, tarifs["valueWait"], tarifs["valueMove"])
            trip["espera"] += n
            trip["tripCost"] += coste
            print(f"Coste total actual: {trip['tripCost'] / 100:.2f}€")
        except ValueError as e:
            print(f"Error: {e}")
        return True

    elif m == "q":
        # Finalización del viaje
        print("Viaje finalizado gracias por viajar con TaxisF5.")
        print(f"Tiempo en movimiento: {trip['avanzado']}s")
        print(f"Tiempo en espera: {trip['espera']}s")
        print(f"Costo total: {trip['tripCost'] / 100:.2f}€")

        save_trip(trip)  # Guarda los datos del viaje
        return False

    else:
        print("Opción no válida.")
        return True


# Calcula el coste según el tipo de acción y las tarifas
def CalcularCosto(modo, t, tar_wai, tar_mov):
    """
    Calcula el coste en centavos según el modo ('wai' o 'mov'),
    el tiempo en segundos y las tarifas proporcionadas.
    """
    if t < 0:
        raise ValueError("El tiempo no puede ser negativo")

    if modo == 'wai':
        print(f"Esperamos {t}s con tarifa {tar_wai} cent/s. Tramo: {t * tar_wai} cent")
        return t * tar_wai

    elif modo == 'mov':
        print(f"Avanzamos {t}s con tarifa {tar_mov} cent/s. Tramo: {t * tar_mov} cent")
        return t * tar_mov

    else:
        raise ValueError("Modo inválido")


# Permite cambiar los valores de las tarifas de espera y movimiento
def CheckPrices(CPtarifs):
    try:
        CPtarifs["valueWait"] = float(input("Inserta nueva tarifa de ESPERA (cent/seg): "))
        CPtarifs["valueMove"] = float(input("Inserta nueva tarifa de MOVIMIENTO (cent/seg): "))
    except ValueError:
        print("Tarifas no válidas. Intenta de nuevo.")


# PRUEBAS UNITARIAS
class TestCounterClass(unittest.TestCase):
    def test_random_movimiento(self):
        # Prueba 10 valores aleatorios para 'mov'
        for _ in range(10):  
            tiempo = random.randint(1, 100)             
            tarifa = random.randint(1, 10)              
            esperado = tiempo * tarifa
            resultado = CalcularCosto('mov', tiempo, 0, tarifa)
            self.assertEqual(resultado, esperado)

    def test_random_espera(self):
        for _ in range(10):
            tiempo = random.randint(1, 100)
            tarifa = random.randint(1, 10)
            esperado = tiempo * tarifa
            resultado = CalcularCosto('wai', tiempo, tarifa, 0)
            self.assertEqual(resultado, esperado)

    def test_error_modo(self):
        # Verifica que se lanza un error con modo inválido
        with self.assertRaises(ValueError):
            CalcularCosto('volar', 10, 2, 5)


# Guardar en archivo


# Utf-8 añade compatibilidad con caracteres especiales
    # y evita problemas con caracteres no ASCII (Hacentos, ñ, € importantes)
    with open("trip_data.txt", "a+", encoding="utf-8") as file:
        file.write(f"--- Iniciar viaje ---\n")
        file.write(f"Tiempo en movimiento: {trip['avanzado']}s\n")
        file.write(f"Tiempo en espera: {trip['espera']}s\n")
        file.write(f"Costo total: {trip['tripCost'] / 100:.2f}€\n")
    print("Datos del viaje guardados en 'trip_data.txt'.")

# Si ejecutamos el script directamente, preguntamos qué modo quiere el usuario
if __name__ == '__main__':
    modo = input("¿Quieres ejecutar tests (t) o iniciar la app (a)?: ").lower()
    if modo == "t":
        unittest.main(exit=False)
    elif modo == "a":
        StartRute(True, trip, tarifs, True)
