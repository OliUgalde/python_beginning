import re

texto= '''hola .como abbbbestas, es la cadena 1, como estas mi capitan
esta es la. segundaabbb () 3 linea de texto
esta es la 4, final definitiva.'''

#haciendo una busqueda simple
resultado= re.findall("Esta",texto)

#\d -> busca digitos numericos del 0 al 9
resultado= re.findall(r"\d", texto)

#\D -> busca todo menos digitos numericos del 0 al 9
resultado= re.findall(r"\D", texto)

#\w -> busca caracteres alfanumericos [a-z , A-Z, 0-9, _]
resultado= re.findall(r"\w", texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z , A-Z, 0-9, _]
resultado= re.findall(r"\W", texto)

#\s -> busca espacios en blanco y saltos en linea
resultado= re.findall(r"\s", texto)

#\S -> busca TODO MENOS espacios en blanco y saltos en linea
resultado= re.findall(r"\s", texto)

#. -> busca TODO MENOS saltos en linea
resultado= re.findall(r".", texto)

#\n -> busca saltos en linea
resultado= re.findall(r"\n", texto)

#\ -> cancelar caracteres especiales (todo lo que no son alfanumericos)
resultado= re.findall(r"\.", texto)#despues de la barra ponemos el caracter especial que queremos buscar, en este caso es el punto

#cadena que busca cadena que busque numero, seguido de un punto y luego un espacio
resultado= re.findall(r'\d\.\s', texto)

#buscando el principio de una linea
#^ -> busca el comienzo de una linea
resultado= re.findall(r'^Hola',texto, flags=re.M)#flags=re.M indica que se tome el comienzo de todas las lineas, no solo el principio 

#$ -> busca el final de una linea
resultado= re.findall(r'$definitiva',texto, flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
resultado= re.findall(r'\d{3}', texto)

#{n,m} -> busca n cantidad de veces el valor de la izquierda como maximo m
resultado= re.findall(r'ab{2,4}', texto)

# | -> busca una cosa o la otra
resultado= re.findall(r'\d{2,5}|hola', texto)

#* -> devuelve TODOS los caracteres que le indiques, sin importar el numero
text= "The quick brown fox jumps over the lazy dog"
x= re.search(r"^The.*dog$",text)
""" 
if x:
    print("si")
else:
    print("no")
 """
#se buscara un patron para reemplazarlo posteriormente
tex= "La fecha es 23/06/2021 y el telefono +1-555-555-5555"

#el patron a buscar
pattern= r"\d{2}/\d{2}/\d{4}"

#el texto con el que se reemplazara el patron
replacement= "fecha oculta"

#reemplazar todas las apariciones del patron
new_text= re.sub(pattern, replacement,tex)

""" print("texto modificado:", new_text) """

#reemplazar vocales por asteriscos
te= "reemplazando todas las vocales por el asterisco"

new_tex= re.sub("[aeiou]","*", te)

""" print(new_tex) """

#validando correo electronico

email= "example@example.com"

pattern1= "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"#+ encuentra al menos alguna vez algun caracter, el {2,} indica el rango de letras de al final, sin limite de longitud

result= re.match(pattern1, email)
""" 
if result:
    print("Direccion de correo valida")
else:
    print("Direccion de correo invalida")
 """
 
#validando una url

t= "Este es un ejemplo de una pagina web: https://www.example.com y tambien podemos visitarla"

parttern2= "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"#? le indicamos que encuentre alguna coincidencia si no no pasa nada

resulta= re.findall(parttern2, t)
""" 
print(resulta)
"""

