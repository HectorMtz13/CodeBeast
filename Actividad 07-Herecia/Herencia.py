#Herencia 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def comer(self):
        print("Estoy comiendo")
    
    def presentarse(self):
        print("Soy ", self.nombre, " y tengo ", self.edad, " años")
    
class Trabajador(Persona):
    def __init__(self, nombre, edad, ocupacion):
        super().__init__(nombre, edad) # Permite a las subclases acceder y extender los métodos y atributos de su superclase. 
        self.ocupacion = ocupacion
    
    def trabajar(self):
        print("Estoy trabajando como", self.ocupacion)

#------------------------------------------------------
unRandom = Trabajador("Alex Turner", 26, "cantante de opera")
unRandom.comer()
unRandom.presentarse()
unRandom.trabajar()