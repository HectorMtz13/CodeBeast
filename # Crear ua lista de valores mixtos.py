# Crear ua lista de valores mixtos 
# Crear una lista de 5 valores del mismo tipo con numpy
# las listas anteriores convertirlas a tuplas y conjuntos 
# crear un diccionario de 5 elementos con valore de distinto tipo

from numpy import numpy
import numpy as np

Mi_lista = [1,"Karol",3,"hector",5]

array = np.array([1,2,3,4,5])

#Convertir a un conjunto
conjunto = set(tuple(Mi_lista),tuple(array))
print(conjunto)
#Convertir a tupla
Convertir_tupla = tuple(Mi_lista, array)
print(Convertir_tupla)
#Convertir a diccionario
diccionario = {
    "Nombre" = ["Benito Juarez","Vicente Fernandez","Don Omar"], 
    "edad" = ["-1","99", "120"],
    "nacionalidad"=["peru", "venezuela", "mexico"]
    }
print(diccionario)

