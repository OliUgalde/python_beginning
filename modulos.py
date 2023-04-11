import os
""" 
Using python os module it is possible to automatically perform many operating system tasks. 
The OS module in Python provides functions for creating, changing current working directory, 
and removing a directory (folder), fetching its contents, changing and identifying the current directory.
"""
#lo que se puede hacer con este modulo:
#print(dir(os))

import sys
""" 
The sys module provides functions and variables used to manipulate different parts of the Python runtime 
environment. Function sys.argv returns a list of command line arguments passed to a Python script. 
The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from 
the command line.
"""
#print(dir(sys))

import statistics
""" 
The statistics module provides functions for mathematical statistics of numeric data. The popular 
statistical functions which are defined in this module: mean, median, mode, stdev etc. 
"""
#print(dir(statistics))

import math
""" 
Module containing many mathematical operations and constants.
"""
#print(dir(math))

import string

#print(dir(string))

import random
""" 
random module which gives us a random number between 0 and 0.9999.... The random module has lots of
functions but in this section we will only use random and randint. 
"""
#random()  # it doesn't take any arguments; it returns a value between 0 and 0.9999
#random.randint(5, 20) # it returns a random integer number between [5, 20] inclusive
#print(dir(random))

import secrets
"""
Este modulo da acceso a la fuente mas segura de random contrasenas
"""

#ejercicios

#contrasena random de seis digitos

def letras_random(letras):
    lista=[]
    for letra in range(letras):
        x=random.choice(string.ascii_letters)
        lista.append(x)
    rand= "".join(lista)
    return rand 
    
def random_user_id():
    u=random.randint(0,9)
    x=letras_random(2)
    y=random.randint(10,99)
    z=letras_random(1)
    contrasena=(str(u)+x+str(y)+z)
    return contrasena

def user_id_gen_by_user(ids,longitud):
    for id in range(ids):
        x=letras_random(longitud)
        contrasena=(x)
        print(contrasena)
    return f'Se generaron {ids} contrasenas de {longitud} letras de largo'

def rgb_color_gen(nums):
    lista=[]
    for i in range(nums):
        x=random.randint(0,255)
        y=random.randint(0,255)
        z=random.randint(0,255)
        lista.append('rgb('+ str(x) + "," + str(y) + "," + str(z) +")")
    return lista
#print(rgb_color_gen(3))

import uuid

#generar colores hexadecimales 

def generate_colors(num,long):
    rgb=[]
    for i in range(long):
        x= uuid.uuid4().hex
        startLoc= 0
        endLoc= num
        x1=x[startLoc:endLoc]
        rgb.append('#'+ x1)
    return rgb
#print(generate_colors(6,3))

#shuffled list

def shuffle_list(*args):
    lista=[]
    for arg in args:
        lista.append(arg)
    random.shuffle(lista)
    return lista
#print(shuffle_list("platano", "pepino","naranja"))

#generar array de siete numeros random con numeros unicos
def array_numeros_unicos(nums):
    unicos=[]
    for num in range(nums+1):
        x=random.randint(0,9)
        if x not in unicos:
            unicos.append(x)
    return unicos
#print(array_numeros_unicos(4))

#problemas archivos csv

import pandas as pd

#df= pd.read_csv("archivo.csv")

#convertir a string datos de una columna
#df['edad']= df['edad'].astype(str)

#reemplazar datos

#df['apellido'].replace("dalto","maestro",inplace=True)
#print(df['apellido'])

#eliminar filas con datos faltantes con dropna()

#df= df.dropna()#para eliminar columnas se usa dentro de los parentesis axis=1

#eliminar filas repetidas

#df= df.drop_duplicates()

#DATATIME 

from datetime import datetime

#print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

now = datetime.now()
#print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
#print(day, month, year, hour, minute)
#print('timestamp', timestamp)
#print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
#print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
#print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
#print("time two:", time_two)

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
#print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
#print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
#print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
#print("d =", d)

