#sumar todos los numeros de 0 a 100

numeros= range(101)
for numero in numeros:
    if numero == 100:
        suma= sum([*numeros])
        #print(f'la suma de todos los numeros del 0 al 100 es: {suma}')
      
#sumar the evens from 0 to 100

numeros= range(0,101,2)
for numero in numeros:
    if numero == 100:
        suma= sum([*numeros])
        #print(f'la suma de los numeros pares del 0 al 100 es: {suma}')

#sumar the odds

numeros= range(101)
impares = []
for numero in numeros:
    if numero%2 != 0:
        impares.append(numero)
        suma= sum([*impares])
#else:
    #print(f'la suma de todos los numeros impares del 0 al {numero} es: {suma}')
    
# definiendo funciones
#suma de numeros

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total

#funcion suma

def add_two_numbers(num1,num2):
    suma= num1 + num2
    return suma
#print(add_two_numbers(4,6)) 

#area de un circulo

def area_circle(r):
    pi= 3.1416
    area= pi*r*r
    return area

#suma todos los numeros dados

def suma_todo(*nums):
    total=0
    for num in nums:
        total += num
    return total
#print(suma_todo(3,6,4,7,10))    
  
#convertir grados celsius a fahrenheit 

def convert_celsius_to_fahrenheit(c):
    f= (c*(9/5))+32
    return f
#print(convert_celsius_to_fahrenheit(5))

#check season

def check_season(month):
    if month.lower() in ("december","january","febrary"):
        return "winter"
    elif month.lower() in ("march","april","may"):
        return "spring"
    elif month.lower() in ("june","july","august"):
        return "summer"
    elif month.lower() in ("september","october","november"):
        return "autum"
#print(check_season("december"))

#imprimir lista

def imprimir_lista(*args):
    lista=[]
    for i in args:
        lista.append(i)
    return f'tu lista es: {lista}'
#print(imprimir_lista("ajo","oregano","limon")) 

#imprimir listas en reversa

def reverse_list(*args):
    lista=[]
    for i in args:
        lista.append(i)
        lista.sort(reverse=True)
    return f'tu lista es: {lista}'
#print(reverse_list("a","b","c")) 

#capitalized list of items

def capitalize_list(*args):
    lista=[]
    for i in args:
        lista.append(i)
        lista_capitalizada= [i.capitalize() for i in lista]
    return f'tu lista es: {lista_capitalizada}'
#print(capitalize_list("ale","Beto","CARLOS")) 

#sumar impares en el rango

def sum_of_odds(nums):
    total=0
    for num in range(nums+1):
        if num%2!=0:
            total += num 
    return total

#print(sum_of_odds(6))

#sumar pares en el rango

def sum_of_odds(nums):
    total=0
    for num in range(nums+1):
        if num%2==0:
            total += num 
    return total

#print(sum_of_odds(6))

#numeros impares y pares

def evens_and_odds(num):
    num_pares=[]
    num_impares=[]
    for i in range(1,num+1):
        if i%2==0:
            num_pares.append(i)
        elif i%2!=0:
           num_impares.append(i)
    respuesta=(f'hay {len(num_pares)} numeros pares y {len(num_impares)} numeros impares hasta el {num}')
    return respuesta
#print(evens_and_odds(8)) 

#funcion que nos dice los numeros primos en el rango indicado
def es_primo(num):
    for i in range(2,num-1):#verificamos que el numero no pueda dividirse por ningun numero entre 2 y el mismo numero
        if num%i==0:return False
    return True
def primos_hasta(num):
    primos=[]
    for i in range(3,num+1):
        resultado = es_primo(i)#verificamos si el valor es primo
        if resultado == True: primos.append(i) #si es primo, lo agregamos a la lista
    return primos
        
resultado = primos_hasta(98)
#print(resultado)

#funcion que nos dice si un numero es primo

def es_primo(num):
    for i in range(2,num-1):#verificamos que el numero no pueda dividirse por ningun numero entre 2 y el mismo numero
        if num%i==0:return False
    return True
#print(es_primo(31))

#checar si hay un elemento repetido
""" 
def checar_elementos_repetidos(*nums):
    unicos=[]
    for num in nums:
        if num not in unicos:
            unicos.append(num)
            respuesta= (f'el numero {unicos} son unicos')
            return respuesta
"""        
#print(checar_elementos_repetidos(6,8,5,4,5,3))

#filtrar numeros negativos
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtrar= [number for number in numbers if number<1]

#print(filtrar)

#aplanar listas
def flatten_list():
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    return [x for sub in list_of_lists for sub2 in sub for x in sub2]
#print(flatten_list())

def abreviatura_en_medio():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    countries = [[sub2[0].upper(), sub2[1].upper()] for sub in countries for sub2 in sub]
    countries = [[sub[0], sub[0].upper()[:3],sub[1]] for sub in countries]
    return countries
#print(abreviatura_en_medio())
  
#output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

def list_to_list_dict():
    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    countries = [[sub2[0].upper(), sub2[1].upper()] for sub in countries for sub2 in sub]
    countries = [x for sub in countries for x in sub]
    print(countries)
    keys = ["country", "city"]
    return [{keys[0]: countries[idx], keys[1]: countries[idx + 1]} for idx in range(0, len(countries), 2)]
#print(list_to_list_dict())

def generar_tuplas():
    tupla=[(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
    return tupla
#print(generar_tuplas())


def juntar_nombres():
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    names = [[lastname[0],lastname[1]] for name in names for lastname in name]
    names = [' '.join(name) for name in names]
    return names
#print(juntar_nombres())

#EJERCICIOS DIA 14

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#convertir a mayusculas una lista
def change_to_upper(name):
    return name.upper()

def lista_a_mayusculas(lis):
    lista= list(map(change_to_upper,lis))
    return lista

#cambiar numeros a sus cuadrados

numbers_new= list(map(lambda x:x**2, numbers))
#print(numbers_new)

#usar filter para ver paises que tienen 'land'
import re
def encontrar_land(lista):
    busqueda= re.search(r'land',lista)
    return busqueda

land= list(filter(encontrar_land,countries))
#print(land)

#encontrar pais con seis letras
def cuantas_letras_6(palabra):
    if len(palabra)==6:
        return True
    return False

seis_letras= list(filter(cuantas_letras_6,countries))
#print(seis_letras)

#encontrar paises con seis letras y mas
def cuantas_letras_mas_de_6(palabra):
    if len(palabra)>=6:
        return True
    return False

seis_letras2= list(filter(cuantas_letras_mas_de_6,countries))
#print(seis_letras2)

#usar filter para encontrar paises que empiezan con E

def empieza_con_e(lista):
    letra_e= re.findall(r'^E',lista)
    return letra_e

letra_e= list(filter(empieza_con_e,countries))
#print(letra_e)

#sumar sum para sumar todos los num de una lista
from functools import reduce

suma_de_todo= reduce(lambda a,b:a+b,numbers)
#print(suma_de_todo)

#declarar funcion get_string_list

def get_string_lists(lista):
    cadena= [str(i) for i in lista]
    return cadena 

#print(get_string_lists(numbers))

#dia 17
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries,es,ru= names
#print(*nordic_countries,es,ru)
#print(nordic_countries)

#dia 18

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and MATCH
match = re.search('first', txt, re.I)
#print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
#print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
#print(start, end)  # 100 105
substring = txt[start:end]
#print(substring)       # first

#FINDALL()
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
#print(matches)  # ['language', 'language']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
#print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
#print(matches)  # ['Python', 'python']

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
#print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
#print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
#print(re.split('\n', txt)) # splitting using \n - end of line symbol

"""    
[]: A set of characters
[a-c] means, a or b or c
[a-z] means, any letter from a to z
[A-Z] means, any character from A to Z
[0-3] means, 0 or 1 or 2 or 3
[0-9] means any number from 0 to 9
[A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
\: uses to escape special characters
\d means: match where the string contains digits (numbers from 0-9)
\D means: match where the string does not contain digits
. : any character except new line character(\n)
^: starts with
r'^substring' eg r'^love', a sentence that starts with a word love
r'[^abc] means not a, not b, not c.
$: ends with
r'substring$' eg r'love$', sentence that ends with a word love
*: zero or more times
r'[a]*' means a optional or it can occur many times.
+: one or more times
r'[a]+' means at least once (or more)
?: zero or one time
r'[a]?' means zero times or once
{3}: Exactly 3 characters
{3,}: At least 3 characters
{3,8}: 3 to 8 characters
|: Either or
r'apple|banana' means either apple or a banana
(): Capture and group
"""
#Special caracter \d+ 
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
#print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

paragraph = 'I love teaching. If you do not love teaching what else can you love I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'

from collections import Counter

def most_common_words(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common()
    # Cnter.sort(reverse=True)
    return Cnter
 
#print(palabra_mas_repetida(paragraph))
#print(most_common_words(paragraph))

para = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction. """

num_list = list(map(int, re.findall(r"[-+]?[.]?[\d]+", para)))
num_list.sort()
#print(num_list)
dist = num_list[-1] - num_list[0]
#print(dist)

def is_valid_variable(potential_variable):
    if re.search(r"^[a-zA-Z_]\w*$", potential_variable):
        return True
    else:
        return False

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(lista):
    limpia= re.sub("[%$@&#;.]","",lista)
    return limpia

#print(clean_text(sentence))
limpio=clean_text(sentence)
#print(most_common_words(limpio)[:3])

#DIA 19
x=open("nombres_y_apellidos.txt")
#print(x.read())
x.close()
