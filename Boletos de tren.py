print("Bienvenido al sistema de expedición de boletos de tren")

class TarjetaCredito:
    def __init__(self, identificacion, numero):
        self.identificacion = identificacion
        self.numero = numero

class MaquinaExpendedora:
    def __init__(self):
        self.tarjetas_registradas = []
        self.destinos = {
            "londres": 150,
            "manchester": 120,
            "madrid": 200
        }
        self.destino_seleccionado = None

    def registrar_tarjeta(self, identificacion, numero):
        tarjeta = TarjetaCredito(identificacion, numero)
        self.tarjetas_registradas.append(tarjeta)
        print("Tarjeta registrada con éxito.")

    def seleccionar_destino(self):
        print("Seleccione su destino:")
        for i, destino in enumerate(self.destinos.keys(), start=1):
            print(f"{i}. {destino} - Precio: ${self.destinos[destino]:.2f}")
        
        seleccion = int(input())
        destinos_list = list(self.destinos.keys())
        if seleccion >= 1 and seleccion <= len(destinos_list):
            self.destino_seleccionado = destinos_list[seleccion - 1]
            print(f"Destino '{self.destino_seleccionado}' seleccionado.")

    def validar_identificacion(self, identificacion):
        for tarjeta in self.tarjetas_registradas:
            if tarjeta.identificacion == identificacion:
                return True
        return False

    def expender_boleto(self, identificacion, nombre):
        if self.destino_seleccionado and self.validar_identificacion(identificacion):
            precio_boleto = self.destinos[self.destino_seleccionado]
            print("¡Boleto expedido!")
            print(f"Nombre: {nombre}")
            print(f"Identificación: {identificacion}")
            print(f"Destino: {self.destino_seleccionado}")
            print(f"Precio del Boleto: ${precio_boleto:.2f}")

            confirmacion = input("¿Confirmar compra? (si/no): ")
            if confirmacion.lower() == 'si':
                print("Compra exitosa. Monto cargado: ${:.2f}".format(precio_boleto))
            else:
                print("Compra cancelada.")
        else:
            print("No se puede expedir el boleto.")

def main():
    maquina = MaquinaExpendedora()

    identificacion = input("Ingrese su identificación: ")
    numero_tarjeta = input("Ingrese el número de tarjeta de crédito: ")
    maquina.registrar_tarjeta(identificacion, numero_tarjeta)

    print("Tarjeta y registro confirmados.")

    maquina.seleccionar_destino()

    identificacion_validacion = input("Ingrese su identificación para validar: ")
    if maquina.validar_identificacion(identificacion_validacion):
        nombre = input("Ingrese su nombre: ")
        maquina.expender_boleto(identificacion_validacion, nombre)
    else:
        print("Identificación no válida.")

if __name__ == "__main__":
    main()
