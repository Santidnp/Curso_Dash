###Ejemplo 1 sin parametros:

def funcion_decoradora(funcion_parametro):

    def funcion_interior():
        #acciones adicionales
        print("Vamos a realizar un calculo")
        funcion_parametro()
        #Mas acciones
        print("Se ha terminado la ejecución")
    
    return funcion_interior


@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)



suma()
resta()

## Ejemplo2 con parametros:


def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args):
        #acciones adicionales
        print("Vamos a realizar un calculo")
        funcion_parametro(*args)
        #Mas acciones
        print("Se ha terminado la ejecución")
    
    return funcion_interior


@funcion_decoradora
def suma(a,b,c):
    print(a+b+c)

@funcion_decoradora
def resta(a,b):
    print(a-b)



suma(7,5,10)
resta(12,10)


#### Ejemplo 3:

def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args,**kwargs):
        #acciones adicionales
        print("Vamos a realizar un calculo")
        funcion_parametro(*args,**kwargs)
        #Mas acciones
        print("Se ha terminado la ejecución")
    
    return funcion_interior


@funcion_decoradora
def potencia(base,exponente):

    print(pow(base,exponente))


potencia(base = 5,exponente = 3)