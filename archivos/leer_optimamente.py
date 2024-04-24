#abriendo el archivo con with open
with open("archivos\\Archivo.txt",encoding="UTF-8") as archivo:
    print(archivo.read())
    
    #leemos el archivo
    
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    