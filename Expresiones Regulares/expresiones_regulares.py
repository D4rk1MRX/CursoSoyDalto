import re 

texto = '''Hola Loco, Esta es la cadena 1. como estas?
esta es la final somos como la linea 2.
y esta la peor y somos la linea 3.'''
#haciendo una busqueda simple
#resultado = re.search("esta",texto, flags=re.IGNORECASE)

#\d -> busca digito numerico del 0 al 9
#resultado = re.findall(r"\d",texto)

#\D -> busca TODO Menos digito numerico del 0 al 9
resultado = re.findall(r"\D",texto)


#\w -> busca caracteres alfanumericos {a-z A-Z 0-9}
#resultado = re.findall(r"\w",texto)

#\W -> busca TODO MENOS caracteres alfanumericos {a-z A-Z 0-9}
#resultado = re.findall(r"\W",texto)

#\s-> busca espacios en blancos -> espacios, tabs, saltos en linea
#resultado = re.findall(r"\s",texto)

#\s-> busca TODO Menos espacios en blancos -> espacios, tabs, saltos en linea
#resultado = re.findall(r"\S",texto)

#\.-> Busca TODO Menos saltos en lineas
#resultado = re.findall(r"\.",texto)

#\n-> Busca saltos en linea
#resultado = re.findall(r"\n",texto)

#\- > cancelr caracteres especiales, cancelando la fncion del punto y buscando punto
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r'\d\.\s', texto)

#\^ -> busca el comienzo de una linea
#flags=re.M activa la multilinea
#resultado = re.findall(r'^esta', texto,flags=re.M) 

#\$ -> busca el final de una linea
#resultado = re.findall(r'3$', texto,flags=re.M) 

#{n} -> busca n cantidad de veces el valor de la izquierda (3 numeros junto esta vez)
#resultado = re.findall(r'\d{3}', texto,flags=re.M) 

#{n,m} -> al menos n, como maximo m
#resultado = re.findall(r'\d{2,4}', texto,flags=re.M)

# | -> busca na cosa o la otra
#resultado = re.findall(r'\d{2,4}|Hola', texto,flags=re.M)

#* -> 


print(resultado) 


