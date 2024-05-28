def generador_numeros(inicio, final):
    """
    Devuelve números de forma dinámica usando la terminación yield.
    :param inicio:
    :param final:
    :return:
    """
    for num in range(inicio, final):
        yield num


def generador_infinito():
    x = 1
    while True:
        x += 1
        yield x

def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1


def perder_vidas():
    vida = 3

    while True:
        if vida > 0:
            if vida != 1:
                yield f"Te quedan {vida} vidas"
            else:
                yield f"Te queda {vida} vida."
            vida -= 1
        else:
            yield "GAME OVER"
            while True:
                yield "Ya no tienes vidas."


# Se define el rango y la funcion se guarda como objeto en una variable.
generador_rango = generador_numeros(-1, 3)

# Usamos el método next para ir generando los valores del contador.
print(next(generador_rango))
print(next(generador_rango))
print(next(generador_rango))

# Generador infinito
generador_sin_limite = generador_infinito()
print(next(generador_sin_limite))
print(next(generador_sin_limite))
print(next(generador_sin_limite))


generador_multiplos_siete = multiplos_siete()
print(next(generador_multiplos_siete))
print(next(generador_multiplos_siete))
print(next(generador_multiplos_siete))


vidas = perder_vidas()
print(next(vidas))
print(next(vidas))
print(next(vidas))
print(next(vidas))
print(next(vidas))
print(next(vidas))
print(next(vidas))
print(next(vidas))


