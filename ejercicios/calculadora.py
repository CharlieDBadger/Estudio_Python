def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b


def calculadora():
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        operacion = input("Ingresa la operación (suma, resta, multiplicacion, division): ")

        if operacion == "suma":
            resultado = suma(a, b)
        elif operacion == "resta":
            resultado = resta(a, b)
        elif operacion == "multiplicacion":
            resultado = multiplicacion(a, b)
        elif operacion == "division":
            resultado = division(a, b)
        else:
            resultado = "Operación no reconocida"

        print("El resultado es: ", resultado)
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresa un número.")
    except ZeroDivisionError:
        print("Error: División por cero.")


calculadora()
