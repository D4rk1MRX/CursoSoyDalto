import pandas as pd
df = pd.read_csv("archivos\\archivocsv.csv",names=["name","lastname","age"])
df2 = pd.read_csv("archivos\\archivocsv.csv")

#ordenando el dataframe fomr desendente
df_ordenado = df.sort_values("age")

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("age",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 3 fila con head()
primer_fila = df.head()
#print(primer_fila)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(0)
#print(ultimas_filas)

#accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

#print(columnas_totales)

#obteniendo data estadistica del dataframe
df_info = df.describe()
#print(df_info)

#accediendo a un elemento del df con loc
elemento_especifico = df.loc[2,"age"]
#print(elemento_especifico)

#accediendo a un elemento del df con iloc
elemento_especifico_iloc = df.iloc[2,]
#print(elemento_especifico)

#accediendo a todas las filas de una columna
apellidos = df.loc[:,1]
print(apellidos)