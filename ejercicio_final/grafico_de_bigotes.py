import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("ejercicio_final\\bigotes.csv")

#en boxplot se espedifican las columnas y al ultimo los datos a usarse en el grafico 
sns.boxplot(x="categoria", y="valor",data=df)

#para mostrar el grafico se usa la siguiente linea
plt.show()