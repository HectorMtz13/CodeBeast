class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        return "guau"

class Gato(Animal):
    def hacerSonido(self):
        return "miau"

class Caballo(Animal):
    def hacerSonido(self):
        return "bufuru"

#-------------------------------------Progaming iniciating------------------------------------------
unAnimal = Perro("Alex Turner")
otroAnimal = Gato("Estación3030")
elAnimal = Caballo("Gertrudis")
print(unAnimal.nombre, " hace ", unAnimal.hacerSonido())
print(otroAnimal.nombre, " hace ", otroAnimal.hacerSonido())
print(elAnimal.nombre, " hace ", elAnimal.hacerSonido())