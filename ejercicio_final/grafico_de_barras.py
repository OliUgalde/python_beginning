import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("ejercicio_final\\cofla.csv")
print(df)

#en barplot se espedifican las columnas y al ultimo los datos a usarse en el grafico cartesiano 
sns.barplot(x="fuente", y="ingresos",data=df)

#para mostrar el grafico se usa la siguiente linea
plt.show()

total_ingresos= df['ingresos'].sum()
print(total_ingresos)