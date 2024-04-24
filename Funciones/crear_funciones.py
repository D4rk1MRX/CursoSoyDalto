#creando una fuuncion simple
def saludar():
    print("hola lucas")
    
#ejecutando la funcion simple
#saludar()

#crear una funcion con parametros
def saludar(nombre,sexo):
    sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "princesa"
    elif (sexo == "hombre"): 
        adjetivo = "titan"
    else:
        adjetivo = "amor"

    print(f"hola {nombre},mi {adjetivo} como esta")
    
saludar("master", "no binario")

#crear una funcion que retorna valores  
def crear_contraseña_random(num):
    chars =  "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña
    
    