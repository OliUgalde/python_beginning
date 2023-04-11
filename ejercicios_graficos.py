import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("pedos.csv")
print(df)

#en lineplot se espedifican las columnas y al ultimo los datos a usarse en el grafico cartesiano 
sns.lineplot(x="fecha", y="pedos",data=df)

#creando un punto en el momento de mas pedos
plt.plot("01-09",17,"o")

#para mostrar el grafico se usa la siguiente linea
plt.show()