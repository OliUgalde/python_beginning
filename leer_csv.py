#los archivos csv son valores separados por comas
""" 
import csv
with open('archivo.csv') as archivo:
    print(csv.reader(archivo))
    reader= csv.reader(archivo)
    for row in reader:
        print(row)
 """       
#leer csv con pandas
""" 
archivo= pd.read_csv("archivo.csv")
print(archivo)
"""
#df o data frame son estructuras de datos similares a hojas de calculo, tiene dos parametros: filas y columnas

import pandas as pd
 
df= pd.read_csv("archivo.csv", names=["name", "lastname", "age"])#asi se nombran las columnas para los datos del archivo.csv

#print(df["name"])#obtiene los datos de la columna name 

df= pd.read_csv("archivo.csv")

nombres= df["nombre"]

#ordenar df 
#orden ascendente

df_ordenado_a= df.sort_values("age")
#print(df_ordenado_a)

#orden descendente

df_ordenado_d= df.sort_values("age", ascending=False)
#print(df_ordenado_d)

#concatenando los 2 dataframes

df2= pd.read_csv("archivo.csv", names=["name", "lastname", "age"])

df_concatenado= pd.concat([df,df2])
#print(df_concatenado)

#acceder a la primer fila (de arriba para abajo)
""" 
primer_fila= df.head(3)
print(primer_fila)
 """
#acceder a las ultimas filas (de abajo para arriba)
""" 
ultimas_filas= df.tail(2)
print(ultimas_filas)
 """
#acceder a cantidad de filas y columnas totales con shape
""" 
filas_y_columnas_totales= df.shape
 """
#o
""" 
filas_totales, columnas_totales= df.shape
print(filas_y_columnas_totales, filas_totales, columnas_totales)
 """
#estadisticas del dataframe

df_info= df.describe()

#accediendo a un elemento especifico con loc

elemento_especifico_loc = df.loc[2,"age"]

#accediendo a un elemento especifico del df con loc

elemento_especifico_iloc = df.iloc[2,2]

#accediendo a columnas completas con iloc

apellidosi= df.iloc[:,1]

#accediendo a columnas completas con loc

apellidos= df.loc[:,"lastname"]

#accediendo a filas con iloc

fila_3i= df.iloc[2,:]

#accediendo a filas con loc

fila_3= df.loc[2,:]

#accediendo a las filas donde la edad >30

mayor_que_30= df.loc[df["age"]>30,:]

