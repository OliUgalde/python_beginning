#creando funcion que suma numeros
def sumar_dos():
    #iniciando el bucle
    while true:
        #pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try: #le dice que a pesar de que haya un error, lo siga intentando
            resultado= int(a) + int(b)
        except Exception as a: #si lanza una excepcion
            print("te pedi un numero")
            print(f"error{type(e)._name_}")#muestra la excepcion 
        else:
            break
        finally: #se ejecuta siempre
            print("esto se ejecuta siempre")
    return resultado

print(sumar_dos())