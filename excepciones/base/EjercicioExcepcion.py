class InvalidColorError(Exception):
    pass


def buscar_color(diccionario_colores):
    color_a_buscar = input("Por favor, ingresa el color que deseas buscar: ")

    if not color_a_buscar.isalpha():
        raise InvalidColorError("El color no debe contener números")

    try:
        return diccionario_colores[color_a_buscar]
    except KeyError:
        return "El color no se encuentra en el diccionario"


colores = {"rojo": "#FF0000", "azul": "#0000FF", "verde": "#008000", "amarillo": "#FFFF00"}
try:
    print(buscar_color(colores))
except InvalidColorError as e:
    print(e)

x = lambda r: r + 10
print(x(5))
