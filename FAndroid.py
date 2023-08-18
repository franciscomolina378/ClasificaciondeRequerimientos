print("Bienvenido a FAndroid")
class TarjetaCredito:
    def __init__(self, marca, numero, vencimiento, codigo):
        self.marca = marca
        self.numero = numero
        self.vencimiento = vencimiento
        self.codigo = codigo

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjeta = None
        self.historial_compras = []
        self.puntos = 0

    def agregar_tarjeta(self, marca, numero, vencimiento, codigo):
        self.tarjeta = TarjetaCredito(marca, numero, vencimiento, codigo)
        print("Tarjeta registrada con éxito.")

    def comprar_producto(self, producto):
        if self.tarjeta:
            self.historial_compras.append((producto, producto.precio))
            self.puntos += producto.puntos_requeridos  # Corrección aquí
            print("Compra exitosa. Se ganaron puntos.")
        else:
            print("No se puede comprar sin tarjeta registrada.")

    def canjear_producto(self, producto):
        if self.puntos >= producto.puntos_requeridos:
            self.puntos -= producto.puntos_requeridos
            print(f"Canje exitoso. Se ha canjeado '{producto.nombre}' por puntos.")
        else:
            print("Puntos insuficientes para el canje.")

class Producto:
    def __init__(self, nombre, precio, puntos_requeridos):
        self.nombre = nombre
        self.precio = precio
        self.puntos_requeridos = puntos_requeridos

def mostrar_productos(productos):
    print("----- Productos Disponibles -----")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto.nombre} - Precio: ${producto.precio:.2f} - Puntos requeridos: {producto.puntos_requeridos}")

def main():
    cuentas = []
    productos = [
        Producto("tik tok", 2, 20),
        Producto("whatsapp", 1, 10),
        Producto("nequi", 3, 30),
        Producto("youtube", 5, 40),
        Producto("gmail", 4, 35)
    ]
    productos_canjeables = [
        Producto("auriculares bluetooth", 10, 50),
        Producto("ps4", 15, 70),
        Producto("celular iphone", 20, 90)
    ]

    while True:
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            usuario = Usuario(nombre)
            cuentas.append(usuario)
            print("Usuario registrado con éxito.")

        elif opcion == "2":
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            usuario_encontrado = None
            for cuenta in cuentas:
                if cuenta.nombre == nombre_usuario:
                    usuario_encontrado = cuenta
                    break
            if usuario_encontrado:
                print(f"Bienvenido, {nombre_usuario}!")
                while True:
                    print("4. Registrar tarjeta de crédito")
                    print("5. Comprar producto")
                    print("6. Canjear producto")
                    print("7. Ver historial de compras")
                    print("8. Ver puntos acumulados")
                    print("9. Cerrar sesión")
                    accion = input("Seleccione una acción: ")
                    if accion == "4":
                        if usuario_encontrado.tarjeta:
                            print("Tarjeta ya registrada.")
                        else:
                            marca = input("Ingrese la marca de su tarjeta: ")
                            numero = input("Ingrese el número de su tarjeta: ")
                            vencimiento = input("Ingrese la fecha de vencimiento de su tarjeta: ")
                            codigo = input("Ingrese el código de verificación de su tarjeta: ")
                            usuario_encontrado.agregar_tarjeta(marca, numero, vencimiento, codigo)

                    elif accion == "5":
                        mostrar_productos(productos)
                        seleccion_producto = int(input("Seleccione un producto para comprar: "))
                        if 1 <= seleccion_producto <= len(productos):
                            producto_seleccionado = productos[seleccion_producto - 1]
                            usuario_encontrado.comprar_producto(producto_seleccionado)
                        else:
                            print("Opción no válida.")

                    elif accion == "6":
                        mostrar_productos(productos_canjeables)
                        seleccion_producto = int(input("Seleccione un producto para canjear: "))
                        if 1 <= seleccion_producto <= len(productos_canjeables):
                            producto_seleccionado = productos_canjeables[seleccion_producto - 1]
                            usuario_encontrado.canjear_producto(producto_seleccionado)
                        else:
                            print("Opción no válida.")

                    elif accion == "7":
                        print("----- Historial de Compras -----")
                        for compra in usuario_encontrado.historial_compras:
                            producto, precio = compra
                            print(f"{producto.nombre} - Precio: ${precio:.2f}")

                    elif accion == "8":
                        print(f"Puntos acumulados: {usuario_encontrado.puntos}")

                    elif accion == "9":
                        print(f"Hasta luego, {nombre_usuario}!")
                        break

                    else:
                        print("Acción no válida.")

            else:
                print("Usuario no encontrado.")

        elif opcion == "3":
            print("Gracias por usar la plataforma. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()


