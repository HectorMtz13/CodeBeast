import threading
import time
# Definimos la clase hilo que hereda de threading.Thread
class hilo(threading.Thread):
    def __init__(self, nombre, intervalo):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.intervalo = intervalo 
# Definimos el método run que es el que se ejecuta al iniciar el hilo
    def run(self):
        print(f"El hilo {self.nombre} ha comenzado") 
        for i in range(5):
           print(f"el hilo {self.nombre} se encuentra en la iteracion {i}")
           time.sleep(self.intervalo)
           print(f"el hilo{self.nombre} ha finalizado")
# Creamos dos hilos
hilo1 = hilo("Hilo1", 2) # Hilo que duerme 1 segundo
hilo2 = hilo("Hilo2", 4) # Hilo que duerme 2 segundos