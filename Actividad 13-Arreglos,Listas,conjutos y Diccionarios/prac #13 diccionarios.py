dic = {'x' : "equis", 'y' : "ye", 'd' : "de"}
dic2 = dict(x = "equis", y = "ye", d = "de")

#Encontrar un valor
print(dic['x']) #equis
print(dic.get('x')) #equis
print(dic.get('z')) #none
#print(dic['z'])
#Aunque hagan lo mismo, con "[]" manda un error y con get te manda un valor nulo.

#Modificar un valor existente
dic['x'] = "equis :O"
print(dic['x']) #equis :O

#Agregar elementos, si no existe, lo agrega
dic['z'] = "zeta"
print(dic['z']) #zeta

#Eliminar un elemento
del dic['y']
print(dic)

dic = {'x' : "equis", 'y' : "ye", 'd' : "de"}
x = dic.pop('y') #El elemento que se elimina, se almacenará en esta variable
print(dic)
print(x)

#Encontrar un elemento dentro del diccionario
print('x' in dic) # true

#Acceder a las llaves
llaves = dic.keys()
print(llaves)

#Acceder a los valores
valores = dic.values()
print(valores)

#El diccionario se convertira en una tupla
p = dic.items()
print(p)

#Vaciar el diccionario
dic2.clear()
print(dic2)

#Modificar multiples elementos existentes o agragar elementos inexistentes
dic.update({'x' : "wasaa", 'y' : "wesee", 'd': "wisii"})
print(dic)