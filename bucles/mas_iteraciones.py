#creando las listas
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "hola dalto"
numero = [2, 15, 31]
#evitando que se coma una manzana con la sentencia continue
#for fruta in frutas:
    #if fruta == "manzana":
     #   continue
    #print(f"Me voy a comer una {fruta}")
    
#evitar que el bucle siga ejecutandose

for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == 'pera':
        break

else: 
    print("termminado")
    
#recorrer una cadena de texto

for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
numero_duplicados2 = [x*2 for x in numero]
print(numero_duplicados2) 

