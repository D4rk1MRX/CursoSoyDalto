#creando funcion uqe suma numeros
def suma_dos():
    #iniciando un bucle while
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a)+int(b)
        #si lanza excepcion pedirle que reeingrese los datos
        except Exception as e:
            print("Te pedi un numero")
            print(f"Error: {type(e).__name__}")
        #si sale todo bien terminar
        else:
            break
        finally:
            print("Administracion de Excepciones utilizado")
            
    return resultado
print(suma_dos())