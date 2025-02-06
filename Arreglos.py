# Arreglos and listas

class Arreglos:
    def __init__(self):
        self.lista = []

    def insertar(self, elemento):
        self.lista.append(elemento)
        print(f"'{elemento}' agregado a la lista.")

    def modificar(self, indice, nuevo_valor):
        if 0 <= indice < len(self.lista):
            self.lista[indice] = nuevo_valor
            print(f"Elemento en la posición {indice} modificado a '{nuevo_valor}'.")
    def eliminar(self, indice):
        if 0 <= indice < len(self.lista):
            eliminado = self.lista.pop(indice)
            print(f"'{eliminado}' eliminado de la lista.")
        else:
            print("Índice fuera de rango.")

    def mostrar(self):
        print("Lista actual:", self.lista)

arreglo = Arreglos()
while True:
    print("\nValores dentro de la lista")
    print("1 - Insertar valor a la lista")
    print("2 - Modificar valor en la lista")
    print("3 - Eliminar valor de la lista")
    print("4 - Mostrar lista")
    print("5 - Salir")
    
    opcion = int(input("Selecciona una opción: "))
    
    if opcion == 1:
        elemento = input("Ingresa el valor a agregar: ")
        arreglo.insertar(elemento)
    elif opcion == 2:
        indice = int(input("Ingresa el índice a modificar: "))
        nuevo_valor = input("Ingresa el nuevo valor: ")
        arreglo.modificar(indice, nuevo_valor)
    elif opcion == 3:
        indice = int(input("Ingresa el índice a eliminar: "))
        arreglo.eliminar(indice)
    elif opcion == 4:
        arreglo.mostrar()
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
