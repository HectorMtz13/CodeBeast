#---------- CONJUNTOS ---------- 1/04/25
# Si tenemos un conjunto c = {1,2,3}
# c.add(4) -> Añade elementos
# c.remove(1) -> Elimina el elemento del conjunto, cuando no se encuentra, existe un error
# c.discard(5) -> Elimina el elemento del conjunto, cuando no se encuentra, no pasa nada
#   n in c -> si existe el valor n dentro del conjunto, saldrá True

#----------------------------------EJERCICIO-----------------------------------------------
# Crear un conjunto de 5 elementos  c = {}
b = {0,1,2,3,4}
print("Conjunto de 5 elementos: ", b)
# agregar un valor  b.add
b.add(5)
print("Agregar un valor: ", b)
# eliminar un valor que existe  b.remove
b.remove(0)
print("Eliminar un valor que existe: ", b)
# eliminar un valor que no existe   b.remove
b.discard(6)
print("Eliminar un valor que no existe: ", b)
# verificar si existe un valor  n in b
print("verificar un valor que existe: ", 1 in b)
# agregar un valor repetido     b.add
b.add(2)
print("Agregar un valor repetido: ", b)

#------------------UNION------------------------
print("----------------UNION-----------------------")
a = {5,6,7,8}
u = b.union(a)
print(u)
u = a|b
print(u)

#------------------INTERSECTION------------------------
print("-----------------INTERSECTION----------------------")
i = a.intersection(b)
print(i)
i = a & b
print(i)

#------------------DIFFERENCE------------------------
print("-----------------DIFFERENCE----------------------")
d = a.difference(b)
print(d)
d = a - b
print(d)
print("-----------------SYMETRIC DIFFERENT----------------------")
sd = a.symmetric_difference(b)
print(sd)
sd = a^b
print(sd)

#------------------PERTENECE------------------------
print("-----------------PERTENECE----------------------")
a = {1,2,3}
b = {1,2,3,4,5}

print(a.issubset(b))
print(b.issuperset(a))

#------------------NUMERO DE ELEMENTOS------------------------
print("-----------------NUMERO DE ELEMENTOS----------------------")
n = len(a)
print(n)

#------------------CONJUNTO VACIO------------------------
print("-----------------CONJUNTO VACIO----------------------")
a.clear()
print(a)

#------------------COPIAR CONJUNTO------------------------
print("-----------------COPIAR CONJUNTO----------------------")
e = b.copy()
print(e)