# Abstracción
from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Deportivo(Auto):
    def arrancar(self):
        return f"El {self.marca} {self.modelo} ha arrancado con gran potencia."

    def frenar(self):
        return f"El {self.marca} {self.modelo} ha frenado de manera deportiva."

    def acelerar(self):
        return f"El {self.marca} {self.modelo} está acelerando a gran velocidad."

#-----------------------------------------------------------
# Creando un objeto de la clase Deportivo
mi_auto = Deportivo("Ferrari", "F8 Tributo")

print(mi_auto.arrancar())
print(mi_auto.acelerar())
print(mi_auto.frenar())