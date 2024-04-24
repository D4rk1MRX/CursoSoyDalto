import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\cofla_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente", y="ingresos",data=df)

#obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum()

#mostrando resultado
print(f"El total de los ingresos de cofla es: {total_ingresos}$ al mes")

#mostrando el resultado
plt.show()