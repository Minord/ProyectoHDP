

############################ ENTIDADES DEL SISTEMA ##########################################

"""
EL CLIENTE

El cliente de nuestro sistema en forma general una empresa extranjera que tiene un interez
es terciarizar la confeccion de su producto.

El cliente es una entidad permanente en el sistema.

PROPIEDADES

nombre      -   el nombre de la empresa o coorporacion.
pais        -   el pais por el que es mas identificada la empresa
categoria   -   tipos de productos que comercia generalista, zapatos, camisetas, vestidos, etc.
telefono    -   el telefono de contacto dado por la empresa
correo      -   correo electronico de contacto.
sitio web   -   el sitio web que tiene la empresa

"""
class Cliente:

    def __init__(self):
        pass

"""
PEDIDOS 

Los pedidos son el objeto principal del sistema, estas pueden estar activas o archivadas o canceladas. Los pedidos
pueden ser elementos no permanentes en el sistemas tienen una realacion con el tiempo. Un pedido es usualemnte 
un objetivo a cumplir dadas las entradas del CLIENTE

PROPIEDADES

Nota: Para este objeto hay que hacer un analisis mas cuidadoso
"""

class Pedido:

    def __init__(self):
        pass

"""
PROCESOS

Como lo que tratamos de modelar es un ambiente pseudo industrial podriamos compreder que casi todas
las actividades que se llevan a cabo pueden ser llamados procesos podemos enter varios tipos de prosesos
como por ejemplo. En este apartado es buena idea hacer una clasificacion de los presesos que se lleven a cabo.

el proceso tambien podria ser entendido como tarea o actividad.

Punto de Discusion : en este caso un proceso puede tener dependencias de otros prosesos o condiciones
como por ejemplo la entrega de requerimientos o materiales. por lo que existe la pregunta
¿Donde ?


PROPIEDADES

nombre                  -   el nombre que se le asigna
categoria               -   es la categoria a la que pertenese el proceso
tiempo de inicio        -   la fecha y hora en la que se empezo
tiempo de finalizacion  -   la ficha en la que el proceso esta compreto
tiempo estimado         -   estimacion para comparar con otros eventos
estado del proceso      -   puede ser en espera, en ejecucion, cancelado y finalizado

"""

class Proceso:

    def __init__(self):
        pass


"""

"""

"""

"""

"""
"""

