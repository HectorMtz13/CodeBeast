import math
class Figura:
    def area(nLados, vLado):
        #Triangulo
        if nLados == 3:
            preH = (vLado/2)**2 + vLado**2
            h = math.sqrt(preH)
            b = vLado
            areaFigura = (b*h)/2
            print("El area del triangulo es: ", areaFigura)

        #cuadrado
        if nLados == 4:
            b = vLado
            h = vLado
            areaFigura = b*h
            print("El area del cuadrado es: ", areaFigura)
        
        #poligono regular
        if nLados > 0:
            angulo = math.radians(360 / (nLados * 2))
            apotema = vLado / (2 * (math.tan(angulo)))
            p = vLado * nLados
            areaFigura = (p * apotema) / 2
            print("El area de la figura es: ", areaFigura)

    def perimetro(nLados, vLado):
        if nLados == 3:
            perimetroFigura = vLado * 3
            print("El perimetro del triangulo es: ", perimetroFigura)
        
        if nLados == 4:
            perimetroFigura = vLado * 4
            print("El perimetro del cuadrado es: ", perimetroFigura)
        
        if nLados == 5:
            perimetroFigura = vLado * 5
            print("El perimetro del pentagono es: ", perimetroFigura)

#--------------------------------------------------------
unaFigura = Figura
unaFigura.area(4,4)
unaFigura.perimetro(4,4)