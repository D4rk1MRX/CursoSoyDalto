#creando un conjunto con set()

conjunto = set(["Dato1","Dato2"])

#Poniendo listas variables dentro de set

conjunto2 = set(["Dato1",("Datotuple1","Datotuple2")])

#metiendo un conjunto dentro de otro conjunto

conjunto3 = frozenset({"Dato1","Dato2"})
conjunto4 = {conjunto3, "Dato3"}

#print(conjunto4)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#verificando si es un subconjnto
#resultado = conjunto2.issubset(conjunto1)
#resultado2 = conjunto2 <= conjunto1

#verificando si es un super
#resultado = conjunto2.issuperset(conjunto1)
#resultado2 = conjunto2 >= conjunto1

#verificar si hay un numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)