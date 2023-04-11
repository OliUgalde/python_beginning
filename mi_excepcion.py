class MiExcepcion(Exception):
    def _init_(self,err):
        print(f"impresionante, cometiste el siquiente error: {err}")
#manejando la excepcion
try:
    raise MiExcepcion("jajaja , persona poco culta") #raise es la palabra clave para lanzar excepciones
except:
    print("como vas a cometer ese error")

#lanzando excepcion    
raise MiExcepcion("jajaja , persona poco culta") #raise es la palabra clave para lanzar excepciones