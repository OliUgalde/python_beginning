import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("ejercicio_final\\dispersion.csv")
print(df)

#en barplot se espedifican las columnas y al ultimo los datos a usarse en el grafico cartesiano 
sns.scatterplot(x="tiempo", y="dinero",data=df)

#para mostrar el grafico se usa la siguiente linea
plt.show()
