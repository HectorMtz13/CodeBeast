from math import pi, tan, sqrt

class Figura:
    def __init__(self, lado, numlados=None):
        self.lado = lado
        self.numlados = numlados

    def calculocuadrado(self):
        perimetro = 4 * self.lado
        area = self.lado ** 2
        return perimetro, area

    def calculotriangulo(self):
        perimetro = 3 * self.lado
        area = (self.lado ** 2) * (sqrt(3)/4)
        return perimetro, area

    def calculopentagono(self):
        perimetro = 5 * self.lado
        area = (5 / 4) * (self.lado ** 2) * (1 / tan(pi / 5))
        return perimetro, area


print("¿Qué figura deseas calcular su área y su perímetro?")
print("1. Cuadrado")
print("2. Triángulo")
print("3. Pentágono")

opcion = int(input("Elige una opción (1-4): "))

lado = float(input("Ingresa el lado de la figura: "))
figura = Figura(lado)

if opcion == 1:
    perimetro, area = figura.calculocuadrado()
    print(f"El perímetro del cuadrado es: {perimetro}")
    print(f"El área del cuadrado es: {area}")
elif opcion == 2:
    perimetro, area = figura.calculotriangulo()
    print(f"El perímetro del triángulo es: {perimetro}")
    print(f"El área del triángulo es: {area}")
elif opcion == 3:
    perimetro, area = figura.calculopentagono()
    print(f"El perímetro del pentágono es: {perimetro}")
    print(f"El área del pentágono es: {area}")
else:
    print("Esa opción no se encuentra disponible.")