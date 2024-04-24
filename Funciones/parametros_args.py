#forma no optima de sumar valores
# def suma (lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados  

# resultado = suma ([5,3,9,10,20])

#utilizando el parametro args

# def suma (*numeros):
#     return sum(numeros)
# resultado = suma(5,3,9,10,20)
# print(resultado)

def suma_total(numeros):
    return sum(numeros)  

resultado = suma_total([5,3,9,10,20])

print(resultado)

