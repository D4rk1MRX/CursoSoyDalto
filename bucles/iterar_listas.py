animales = ["perro", "gato","loro","cocodrilo"]
numeros = [10,10,10,10]

#recorriendo la lista animales
for animal in animales:
    print(animal)

#recorriendo la lista numero y multiplicandolos
for numero in numeros:
    resultado = numero * 5
    print(resultado)
    
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print (f"Recorriendo lista 2: {animal}")
    
for num in range(20):
    print(num)
    
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print()
    
#usando el else

for numero in numeros:
    print (f"ejecutando el numero: {numero}")
else:
    print ("el bucle termino")