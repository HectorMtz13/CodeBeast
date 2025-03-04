#Primer clase de laboratorio
# 28/Ene/2025


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado
    def calcular_perimetro(self):
        return  self.lado * 4

micuadrado = Cuadrado(5)

area = micuadrado.calcular_area()
perimetro = micuadrado.calcular_perimetro()

print(f"Área : {area}")
print(f"Perímetro : {perimetro}")
