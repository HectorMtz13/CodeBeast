import math
class figura:

 def calculocuadrado(lado):
        perimetro = 4 * lado 
        area = lado * lado 
        return perimetro , area

 def calculotriangulo(lado):
        perimetro = 3 * lado
        area = (lado ** 2) * (math.sqrt(3)/4)
        return perimetro , area

 def calculopentagono(lado):
      perimetro = 5 * lado 
      area = (5 / 4) * (lado ** 2) * (1 / math.tan(math.pi / 5))
      return perimetro , area 
    

print ("Cual figura deseas enconyrarle su area y su perimetro")
print("1. Cuadrado")
print("2. Triángulo")
print("3. Pentágono")
opcion = int(input("Elige 1 de las 3 opciones : "))

if opcion == 1:
    lado = float(input("Ingresingrese el lado del cuadrado"))
    perimetro , area = figura.calculocuadrado(lado)
    print(f"El perímetro del cuadrado es:  {perimetro}")
    print(f"El área del cuadrado es: {area}")
elif opcion == 2:
    lado = float(input("Ingresa el lado del triángulo: "))
    perimetro , area = figura.calculotriangulo(lado)
    print(f"El perímetro del triángulo es: {perimetro}")
    print(f"El área del triángulo es: {area}")
elif opcion == 3:
    lado = float(input("Ingresa el lado del pentagono: "))
    perimetro , area = figura.calculopentagono(lado)
    print(f"Elperimetro del pentagono es :{perimetro}")
    print(f"el area del pentagono es : {area}")

else:
 print("Esa opcion no se encuentra en las opciones")