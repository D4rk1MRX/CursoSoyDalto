#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#creamos una funcion que verifique si el numero es primo
def es_primo(num):
    #vericamos que el numero pasado no puede dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
        #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#creanmos funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que lo sea lo llamamos a la lista
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta()
print (resultado)
        
    