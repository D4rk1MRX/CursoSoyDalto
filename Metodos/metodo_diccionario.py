diccionario = {
    "nombre" : "Lucas",
    "apellido" : "dalto",
    "Subs": 100000
}

#Nos devuelve un objeto dict_items 
claves = diccionario.keys()
print(claves)

#obteniendo un elemento con get() y si no me encuentra me lanza none
claves2 = diccionario.get("nombre")
print(claves2)
 
#Obteniendo un elemento de un diccionario iterable
diccionario_itera = diccionario.items()
print(diccionario_itera)
  