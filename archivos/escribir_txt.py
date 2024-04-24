with open("archivos\\Archivo.txt",'w',encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Jajajaja te mate")
    #agregando 2 lineas con writelines
    archivo.writelines(["Hola Maestro como andas\n","Hola maestro\n"])
    #agegando otras 2 lineas
    archivo.writelines(["Hola Maestro como andas\n","Hola maestro"])