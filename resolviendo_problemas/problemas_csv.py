import pandas as pd
df = pd.read_csv("resolviendo_problemas\\archivocsv.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

# #mostrar el tipo de dato del primer elemento de la columna edad
# print(type(df['edad'][0]))

