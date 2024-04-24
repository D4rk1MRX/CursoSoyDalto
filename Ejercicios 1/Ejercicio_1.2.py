#Pedimos la palabra al usuario
frase = input("Dime una frase y calculo cuanto durarias en decirla: ")
#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#usamos len()
cantidad_De_palabras = len(palabras_separadas)
#En caso de que tarde mas de 120
if cantidad_De_palabras > 120:
    print ("Para Flaco asi no")
#Calculamos cuanto tardaria dalto y tu
print(f"Dijiste {cantidad_De_palabras} palabras, y tardarias {cantidad_De_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_De_palabras * 100 // 2 * 1.3 / 100} segundos en decirlo")