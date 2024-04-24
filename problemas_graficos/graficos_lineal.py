import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\pedos.csv")

#creando el grafico
sns.lineplot(x="fecha", y="pedos",data=df)
#creando un punto en el momento de mas pedos
plt.plot("01-010",17.5,"o")
#mostrando el resultado
plt.show()