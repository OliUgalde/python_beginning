# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#variable
my_string_variable= "my string Variable"
print(my_string_variable)

my_int_variable= 5
print(my_int_variable)

my_int_to_str_variable= str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable= False
print(my_bool_variable)

#variables en una sola linea (NO RECOMENDABLE)

name, surname, alias= "Olivia", "Ugalde", "Oro"
print("Me llamo:", name, surname, "me dicen:", alias)

#concatenacion de variables en un print

print(my_string_variable, my_int_variable, my_bool_variable)

#dia 2

#funciones del sistema

print("hola")
#retorna "hola"

len("hola")
#cuenta el numero de caracteres incluyendo los espacios

type("hola")
#revisa el tipo de dato, en este caso es un 'str'

str(4)
#convierte un numero en una string

int(10)
#convierte el dato en un numero

float(10)
#convierte enteros a decimales (10.0)

input('enter your name:')
#toma datos de un usuario

help('keywords')
#imprime todas las palabras reservadas de python

print(min(20, 40, 60)) 
#da el menor valor

print(max(20,60,70))
#da el mayor valor

print(sum([20, 100, 40]))
#suma los valores

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

