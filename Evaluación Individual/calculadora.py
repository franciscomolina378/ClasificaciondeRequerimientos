class Calculadora:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0

    def ingresarValores(self):
        self.valor1 = int(input("Ingrese el primer valor entero: "))
        self.valor2 = int(input("Ingrese el segundo valor entero: "))

    def calcularSuma(self):
        suma = self.valor1 + self.valor2
        print("Suma:", suma)

    def calcularResta(self):
        resta = self.valor1 - self.valor2
        print("Resta:", resta)

    def calcularMultiplicacion(self):
        multiplicacion = self.valor1 * self.valor2
        print("Multiplicación:", multiplicacion)

    def calcularDivision(self):
        if self.valor2 != 0:
            division = self.valor1 / self.valor2
            print("División:", division)
        else:
            print("No se puede dividir entre cero.")

# Crear una instancia de la clase Calculadora
mi_calculadora = Calculadora()

# Ingresar valores
mi_calculadora.ingresarValores()

# Realizar cálculos e imprimir resultados
mi_calculadora.calcularSuma()
mi_calculadora.calcularResta()
mi_calculadora.calcularMultiplicacion()
mi_calculadora.calcularDivision()
