lista = list([42,47,46])

#Crear Lista
cadena = 545
resultado = len(lista)
print(resultado)

#agrega elemento
agregando = lista.append(45)
#Agregarlo solo a la lista sin variable
lista.append(45)
print (lista)

#Agregando elemento a la lista en un indice especifico
lista.insert(2, 45)
print(lista)

#Agregando varios elementos
lista.extend([2030])
print(lista)

#Eliminar un elemento por su indice
lista.pop(0)
print(lista)

#Removiendo un elemento un elemento de la lista por el  elemento
lista.remove(45)
print(lista)
#Eliminando todo los elementos de la lista
#lista.clear()
print(lista)

#Ordenando la lista y si usamos el parametro Reverse=True lo ordenamos en reversa
lista.sort() 
print(lista)
lista.sort(reverse=True) 
print(lista)

#Invirtiendo los elementos de una lista
lista.reverse()
print(lista)

#Encontrando elementos
encontrar = lista.index(46)
print (encontrar)

