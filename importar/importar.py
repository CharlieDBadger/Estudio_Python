from modulos_propios import *  # Importar absolutamente todo, no es aconsejable.
import modulos_propios  # Importamos todas las clases de este paquete
from modulos_propios import modulo_prueba  # Importamos solamente esta clase del paquete
from modulos_propios.SubModulo import sub_modulo_prueba  # Importamos una clase desde un sub-módulo
from modulos_propios.modulo_unifuncion import saludo_unifuncion  # Y aquí solo importamos 1 funcion específica de una clase

# Importar paquete entero
modulos_propios.modulo_prueba.saludo()
# Importar solo una clase del paquete
modulo_prueba.despedida()
# Al importar un sub-módulo usamos los puntos para ir accediendo desde el módulo principal
sub_modulo_prueba.saludo_submodulo()
# También podemos importar exclusivamente una funcion
saludo_unifuncion()

'''
IMPORTANTE:
Es obligatorio tener una clase __init__ en los modulos para poder que se inicialicen, 
pueden no tener contenido.
'''