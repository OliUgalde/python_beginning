"""
num_one= 5
num_two= 4

total= num_one + num_two
diff= num_one - num_two
product= num_two * num_one
division= num_one / num_two
remainder= num_two % num_one
exp= num_one ** num_two
floor= num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor)

P= 3.1416
radio= int(input("cual es el radio de tu circulo?"))

radio_al_cuadrado= radio * radio

Area_of_cicle = P * radio_al_cuadrado

print("el area es:", Area_of_cicle)

circum_of_cicle= (2 * P) * radio

print("la circunferencia es:", circum_of_cicle)
"""
#area de un triangulo
"""
Base= int(input("cual es la base?"))
Altura= int(input("cual es la altura?"))

print(type(Base))
print(type(Altura))

Area= Base * Altura * 0.5 

print(Area)
"""
#perimetro de un triangulo
"""
a= int(input("ingresa lado a"))
b= int(input("ingresa lado b"))
c= int(input("ingresa lado c"))

Perimeter= a + b + c

print(Perimeter)
"""
#perimetro de un rectangulo
"""
length= int(input("largo"))
width= int(input("ancho"))

perimetro= 2 * (length + width)
area= length * width

print("perimetro=", perimetro, "area=", area)
"""
#slope (inclinacion)
"""
y1, x1 = int(input("valor de y1")) , int(input("valor de x1"))
y2, x2= int(input("valor de y2")), int(input("valor de x2"))

print(x1, y1, x2, y2)

m = (y2-y1)/(x2-x1)
print(m)

x = float(input("valor de x"))
print(type(x))
y = x ^ 2 + (6 * x) + 9

print(y)
"""
#comparacion
"""
python= len("python")
dragon= len("dragon")
print(python, dragon)

comparacion= (python != dragon)
print(comparacion)

python= "python"
dragon= "dragon"

print("o" in dragon)

python= len("python")
print(python)
print(type(float(python)))
print(str(python))
print(type(python))

x= int(input("numero"))
divisible = x % 2
print(divisible)

string= ("thirty", "days", "of", "python")
result= ' '.join(string)
print(result)

a= 8
b= 6

print( '{} + {} = {}'.format( a, b, a + b))
print( '{} - {} = {}'.format( a, b, a - b))
print( '{} * {} = {}'.format( a, b, a * b))
print( '{} / {} = {:.2f}'.format( a, b, a / b))
print( '{} % {} = {}'.format( a, b, a % b))
print( '{} // {} = {}'.format( a, b, a // b))
print( '{} ** {} = {}'.format( a, b, a ** b))

radius= 10
area= 3.14 * radius ** 2

print('the area of a circle with radius {} is {} meters square'.format(radius, area))

# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

print(list1, list2)

list= []
list2= [1,2,3,4,5]

print(len(list2))

print(list2[0])
print(list2[-1])
print(list2[2])

mixed_data_types= ["olivia", 32, 1.64, "in a relation", "mexico"]

it_companies= ["facebook", "google", "microsoft", "apple", "ibm", "oracle", "amazon"]

print(it_companies)
print("Numero de companias: ", len(it_companies))
print(it_companies[0], it_companies[4], it_companies[-1])
it_companies[2]= "nvidia"
print(it_companies)
it_companies.insert(3, "intel")
print(it_companies)
print(it_companies[5].swapcase())
it_companies[5]= "IBM"
unir= '#, '.join(it_companies)
print(unir)
does_exist= "nvidia" in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
threeFirst= it_companies[0:3]
print(threeFirst)
threeLast= it_companies[-4:8]
print(threeLast)
it_companies.remove("IBM")
print(it_companies)
it_companies.clear()
print(it_companies)
front_end=['HTML', 'CSS', 'JS', 'REACT', 'REDUX']
back_end=['Node', 'Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

ages= [19,22,19,24,20,25,26,24,25,24]

ages.sort()

print(max(ages))
print(min(ages))
print(ages)

st= {1,2,3,4,5,6}
st.discard(7)
print(st)

dog = {
    'name' : 'Golfi',
    'color' : 'black',
    'breed' : 'coli',
    'age' : 2
}
student = {
    'first_name' : 'Oli',
    "last_name" : 'Ugalde',
    'gender' : 'mujer',
    'age' : 32,
    'marital_status' : 'in a relation',
    'skills' : ["html", "css", "java", "python"]
}

student['skills'].append("c++")
print(student.get('skills'))
print(len(student['skills']))

key = student.keys()
print(key)

values = student.values()
print(values)

tupla = student.items()
print(tupla)

del student['first_name']
print(student)

del student
print(student)

age = int(input("enter your age: "))

if age >= 18:
    print('you are old enough to drive')
else:
    difference = 18 - age
    print(f'you need {difference} more years to learn to drive')
    
score = int(input("ingresa tu calificacion? "))

if score <= 49:
    print("F")
elif score >= 50:
    print("D")
elif score >= 60:
    print("C")
elif score >= 70:
    print("B")
elif score >= 80:
    print("A")

#loops
count= 0
while count < 5:
    print(count)
    count = count + 1
    
language = 'Python'
for i in range(len(language)):
    print(language[i])
   
it_companies = {'facebook', 'google', 'Microsoft', 'Apple','IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break
    
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('next number should be', number + 1) if number != 5 else print("loop's end")
print('outside the loop')

age = int(input("tu edad es: "))

if age >= 18:
    print('you are old enough to drive')
else:
    difference = 18 - age
    print(f'you need {difference} more years to learn to drive')

my_age = 30
your_age = int(input("cual es tu edad? "))

if my_age > your_age:
    diferencia = my_age - your_age
    print(f"eres {diferencia} anios mas joven que yo")
else:
    your_age < your_age
    diferencia1 = your_age - my_age
    print(f"eres {diferencia1} anios mayor que yo")
    
list = (0,1,2,3,4,5,6)

for number in list:
    line = "#"
    print(line * (number + 1))

list = (0,1,2,3,4,5,6,7,8,9,10)

for number in list:
    resultado = number * number
    print(f"{number} X {number} = {resultado}")

language = "python"

for letter in language:
    print(letter)
""" 
#numeros pares even numbers
"""
conteo = range(101)

for numero in conteo:
    if numero % 2 == 0:
        print(numero)
"""
#numeros impares odd numbers
"""
conteo = range(101)

for numero in conteo:
    if numero % 2 != 0:
        print(numero)

x = 1
suma = 0

while x <= 100:
    suma = suma + x
    x += 1
    print(suma)

animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [53, 57, 78, 11]

for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

for numero in numeros:
    resultados = numero * 10
    print(resultados)
""" 
#iterar dos listas a la vez:
""" 
for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
""" 
#forma de recorrer una lista con sus indices
"""
for num in enumerate(numeros):
    print(num) #asi nos mostrara el indice y el valor
    print(num[0]) #de esta forma nos va a mostrar los indices
    print(num[1]) #nos mostrara los valores solamente
    
    indice = num[0]
    valor = num[1]
"""
# uso del for/else
"""
for numero in numeros
   print(f'ejecutando el ultimo bucle, valor actual: {}')
else: #se muestra solo una vez al final del bucle
   print('el bucle termino)

language = 'python'

for letter in language:
    print(letter)
    
for i in range(len(language)):
    print(i)
"""
#iterar diccionarios 
"""
diccionario = {
    "nombre": "olivia",
    "apellido": "ugalde",
    "edad": 32
}
for key in diccionario.items():
    print(key)
""" 
# continue hace que el bucle se salte un elemento
"""
frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

for fruta in frutas:
    if fruta == "manzana":
        continue
    print (f'Me voy a comer una {fruta}')
"""  
#break termina el bucle
"""
for fruta in frutas:
    print (f'Me voy a comer una {fruta}')
    if fruta == "pera":
        break
print("buble terminado")
"""
#iterar una cadena de texto
"""
cadena = 'hola oli'

for letra in cadena:
    print(letra)
"""    
# for en una sola linea de codigo
"""
numeros = [2,5,8,10]

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
"""
# while, mientras que la condicion se cumpla el bucle se va a ejecutar
"""
contador = 0 
while contador < 10:
    print(contador)
    contador += 1
print("el contador llego a su fin")
"""
#funciones integradas
"""
print(max(1,2,3,4,5,6,0))
print(min(1,2,3,4,5,6,0))
print(round(12.34567, 2))
print(bool(2))
print(all([1,2,3,4]))
print(sum([1,2,3,4]))
"""
#construccion de funciones
"""
def saludar():
    print("hola oli, como andas?")

saludar()
"""
#funciones con parametros

""" def saludar(nombre,sexo):
    sexo = sexo.lower() #se va a minusculas
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    
    print(f'hola {nombre}, mi {adjetivo}, como andas?')

saludar("olivia","mujer") """

#crear una funcion que retorne valores con RETURN

""" def crear_contrasena_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num -5
    contrasena = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contrasena,num #de esta manera se guarda el dato pero no se muestra en consola
#desempaquetado de funcion mostrando datos obtenidos y datos utilizados
password, primer_numero = crear_contrasena_random(3)
frase = f"tu contrasena es {password}, el numero utilizado para crearla fue {primer_numero}"
print(frase)
 """
#Utilizando el parametro ARGS
"""
def suma(nombre, *numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado = suma("oli",4,5,6,7,7,7)
#print(resultado)

#forma 2

def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([1,2,3,3,4,55])

print(resultado2)

#funciones datos extra u opcionales
def frase(nombre,apellido,adjetivo = "sonso"): #aqui se define el adjetivo, sonso es el valor predeterminado
    return f'hola {nombre} {apellido}, eres muy {adjetivo}'
frase_resultante = frase("olivia", "ugalde", "inteligente")#sin embargo lo podemos modificar en la ejecucion de la funcion, agregando el tercer parametro
print(frase_resultante) 
"""
#funcion LAMBDA (funcion flecha en javascript)
#lambda crea funciones anonimas para hacer algo sencillo y rapido
""" multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(5))
 """
#usando FILTER
""" numeros = [1,2,3,4,5,6,7,8,9]
def es_par(num):
    if (num % 2 == 0):
        return True
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares)) """

#haciendo lo mismo con lambda

""" numeros = [1,2,3,4,5,6,7,8,9]
numeros_pares = filter(lambda numero:numero%2 == 0, numeros) #index, operacion a realizar, lista
print(list(numeros_pares)) """

#ejercicio 2
""" 
def obtener_companeros(cantidad_de_companeros):#creacion de la funcion
    companeros = [] #lista a llenar con los datos
    for i in range(cantidad_de_companeros):#bucle
    #se obtienen los datos
        nombre = input("ingrese el nombre del companero: ")
        edad = int(input("ingrese la edad del companero: "))
        companero = (nombre,edad)
        companeros.append(companero)#se agregan los datos a la lista
    companeros.sort(key=lambda x:x[1]) #aqui se ordenan los companeros agregados a la lista
    asistente = companeros[0][0]#nos lleva al primer elemento de la lista ya ordenada previamente
    profesor = companeros [-1][0]#nos lleva al ultimo elemento de la lista ya ordenada previamente
    return asistente, profesor

asistente, profesor = obtener_companeros(5)#desempaquetado
print(f'el profesor es: {profesor} y su asistente es {asistente}') """

#numeros primos entre el 0 y el parametro que pasamos
#funcion que nos dice si un numero es primo
""" def es_primo(num):
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
print(resultado) """

#serie fibonacci entre 0 y el numero dado
""" def fibonacci(num):
    a,b=0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b
    return num
resultado = fibonacci(20)
print(resultado) """

# modulo, es cualquier archivo .py
""" import modulo as mod #as para asignar nombres que no tendran interferencia con nuestro codigo

saludo = mod.saludar("oro") """

#para llamar solo una funcion del modulo, usamos:

""" from modulo import saludar """

#cambiar nombre de funcion 

""" from modulo import saludar as salu """

#para importar todo (no recomendado):

""" from modulo import* """
#enrutamiento de modulos
#modulos en otra carpeta
""" from nombre_de_carpeta.modulo import funcion """
#acceder modulos built-in de python
""" import sys

print(sys.builtin_module_names) """
#conocer la ruta de los modulos de python
""" import sys

print(sys.path)
 """
#importar desde la ruta que nos aparece con el codigo anterior

""" import sys

sys.path.append("ruta") """

#archivos txt

#es un contenedor de informacion 
#los archivos txt en python se llaman con open(ruta_del_archivo_txt\\)
""" archivo = open("archivo\\texto.txt" encouding= "UTF-8")
print(archivo.read()) """

#Para leer lineas individuales:
""" lineas= archivo.readlines() """#muestra todas las lineas
""" line_1= archivo.readline(2) """#muestra la linea que le indicamos en el parentesis


#una vez leida una linea no se puede volver a leer a menos que se cierre 
""" archivo.close() """ #para cerrar el archivo txt

#se debe cerrar el archivo para evitar perdida de informacion, ademas de que las veces que se puede acceder a el son limitadas
""" with open('archivo\\leer.txt', encoding= "UTF-8") as archivo: """ #de esta manera se abre y se cierra cuando se ejecuta el comando que le indicamos
""" print(archivo.read()) """
    
#escribir txt.py con .write()
""" with open("archivo\\leer.txt", "w", encoding= "UTF-8") as archivo: """ #se debe agregar un segundo parametro "w" indicando permiso de write

""" archivo.write("jajaja holi") """ #de esta manera se sobreescribe el archivo txt

""" archivo.writelines(["hola como estas\n","jeje"]) """#de esta manera, se sobrescribe junto a lo que hay en el archivo txt en la linea que le indiquemos

#con writeline lo que le indicamos que escriba se va acumulando

#para agregar informacion en archivos txt en el segundo parametro se escribe "a" de append
#with open('archivo\\leer.txt', 'a' encoding= "UTF-8") as archivo:

#slicing

cadena= "01234567"
#print(cadena[2:6])

#problemas de archivos

#listas de datos a escribir

nombres=["oli", "Andreas","guillermono", "mariana"]
apellidos=["ugalde", "grossauer", "ugalde", "Lopez"]

#registrar info en archivo txt

with open("nombres_y_apellidos.txt","w", encoding="UTF-8") as arch:
    arch.writelines("Los Datos son:\n")
    [arch.writelines(f"el nombre es: {n},\ny el apellido es: {a}\n__________\n") for n,a in zip(nombres, apellidos)]

#hacerlo en dos linea:  

    for n,a in zip(nombres, apellidos):
        arch.writelines(f"el nombre es: {n},\ny el apellido es: {a}\n__________\n")  
