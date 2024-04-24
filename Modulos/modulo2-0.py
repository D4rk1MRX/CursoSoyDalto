#si el modulo en una carpeta en la misma ruta se importa:
#import funciones_buenas.saludar as m_saludar
import sys

sys.path.append("C:\\Users\\D4rk1_53n7wl0\\Desktop\\Curso Practice Python\\funciones_buenas")

import saludar

print(saludar.saludar("dalto"))