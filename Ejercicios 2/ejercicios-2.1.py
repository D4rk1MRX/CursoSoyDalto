#falto el profe y los pides van a armar la clase

#pedir el nombre y la edad de los compañeros que vinieron hoy a clase
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(7):
        nombre = input("Ingrese el nombre del compañero")
        edad = int(input("Ingrese la edad del compañero"))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    assistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return assistente,profesor

assistente,profesor = obtener_compañeros(5)

print(f"El profesor es: {profesor} y su asistente es {assistente}")