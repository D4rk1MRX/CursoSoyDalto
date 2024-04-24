#Importar y añadir un modulo de otro archivo.
from funciones_buenas.modulo_saludar import saludar,saludar_Raro

#Probamos el modulo
saludo = saludar("Lucas")
saludo = saludar_Raro("Aron")
print(saludo)

#para ver las propiedades del modulo
#print(dir(m_saludar))

#acceder al nombre del modulo que llamamos
#print(m_saludar.__name__)
