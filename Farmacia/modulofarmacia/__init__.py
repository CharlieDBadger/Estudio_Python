def anotacion_texto_espera(funcion):
    def generador():
        print("Tu turno es el: ")
        resultado = funcion()  # Llamamos a la función original y almacenamos su resultado
        print(resultado)
        print("Espere a ser atendido.")
        return resultado  # Devolvemos el resultado de la función original
    return generador  # Devolvemos la función generador que envuelve a la función original


def anotacion_texto_espera_dummie(funcion):
    def generador(letra):
        print("Tu turno es el: ")
        resultado = funcion(letra)  # Llamamos a la función original y almacenamos su resultado
        print(resultado)
        print("Espere a ser atendido.")
        return resultado  # Devolvemos el resultado de la función original
    return generador  # Devolvemos la función generador que envuelve a la función original


def generador_de_numeros_infinito():
    x = 0
    while True:
        x += 1
        yield x

