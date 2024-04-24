archivo = open("archivos\\Archivo.txt",encoding="UTF-8")
#leer archivo completo
#archivo = archivo_sin_leer.read()
#leer linea por lineas
#lineas = archivo_sin_leer.readlines()

#leer una sola linea

linea = archivo.readline()

#cerrar archivo

archivo.close()

print(archivo.read()) 