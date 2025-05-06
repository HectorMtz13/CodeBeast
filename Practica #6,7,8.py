
# Herencia 
class persona: 
    def __init__(self,persona):
        self._nombre = nombre

    def obtener_nombre(self):
        return self._nombre
p = persona("Karol")
print(p.obtener_nombre())





#Polimorfismo

class ave:
    def volar(self):
        return "algunas aves pueden volar"
    
class aguila(ave):
    def volar(self):
        return "El aguila vuela alto"
    
class pinguino(ave):
    def volar(self):  
        return "el pinguino no puede volar"
    
aves = [aguila() , pinguino()]  #define un arreglo tipo lista[]
for ave in aves:  # se define una variable ave
    print(ave.volar()) # cada elemento de este arreglo se va a imprimir con la funcion ave


# Abstraccion

from abc import ABC , abstractclassmethod

class auto(abc):
    def __init__(self, marca, modelo):
        self.marca = marca
        self,modelo = modelo
    
    @abstractmethod
    def arrancar(self):
        pass
    @abstractmethod
    def frenar(self):
        pass

class deportivo(auto):
    def arrancar(self):
        return (f"el") 
