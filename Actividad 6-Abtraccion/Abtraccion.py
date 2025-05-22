from abc import ABC, abstractmethod

class Actor(ABC):
    def __init__(self, personaje, papel):
        self.personaje = personaje
        self.papel = papel
    
    @abstractmethod
    def decirDialogo(self):
        pass

class Villano(Actor):
    def decirDialogo(self):
        print(f"Hola, soy {self.personaje} y soy el {self.papel} de la historia. ¡Temedme!")

class Primario(Actor):
    def decirDialogo(self):
        print(f"Hola, soy {self.personaje} y soy el {self.papel} de la historia. ¡Acompáñame en esta aventura!")

#-----------------------------------------------------------
unRandom = Villano("Rumpelstiltskin", "antagonista")
otroRandom = Primario("Shrek", "protagonista")

unRandom.decirDialogo()
otroRandom.decirDialogo()