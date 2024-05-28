import os
import platform
from os import system
from random import choice
import re


def reemplazar_guion_bajo(texto):
    return re.sub(r'\w', '_', texto)


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.

    Nota:
        - Para que esta función funcione correctamente en Windows, asegúrate de que la consola
          esté configurada para emular la terminal del sistema operativo. En algunos IDE, esto
          puede lograrse seleccionando una opción para emular la terminal del sistema operativo
          en lugar de una terminal genérica. De lo contrario, los caracteres especiales utilizados
          para limpiar la pantalla podrían no mostrarse correctamente.
    """
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system("cls")
    elif sistema_operativo in ["Linux", "Darwin"]:  # Para sistemas basados en Unix (Linux, macOS)
        os.system("clear")
    else:
        # Si no se reconoce el sistema operativo, se imprime un mensaje de advertencia
        print("No se puede limpiar la pantalla en este sistema operativo.")


def select_option_index(menu, indicaciones):
    """
    :param menu: Lista, tupla o conjunto (set) que contiene las opciones del menú, no puede estar vacía.
    :param indicaciones: Mensaje que se muestra al usuario para solicitar la selección.
    :return: La posición de la opción seleccionada dentro de la colección de opciones, un Integer.
    """

    if not isinstance(menu, (list, tuple, set)) or not menu:
        print("El menú está vacío o no es de un tipo de datos admitido (lista, tupla o conjunto).")
        return None
    else:
        check_seleccion = False
        while not check_seleccion:
            print(indicaciones)
            for opcion in menu:
                print(f"[{menu.index(opcion) + 1}] {opcion}.")
            try:
                seleccion = int(input("Escoja una opción: "))
                if 1 <= seleccion <= len(menu):
                    check_seleccion = True
                    limpiar_pantalla()
                    return seleccion - 1
                else:
                    limpiar_pantalla()
                    print(f"Ingrese una opción entre 1  y {len(menu)}.")
            except ValueError:
                limpiar_pantalla()
                print("Debes ingresar un número.")


# BANCO DE PALABRAS
palabras = ["PYTHON", "PROGRAMACIÓN", "ALGORITMO", "COMPUTADORA", "DESARROLLO",
            "INTELIGENCIA", "ARTIFICIAL", "ESTRUCTURA", "DATOS", "FUNCION"]

new_game = "YES"

while new_game == "YES":

    vidas = 5
    letra = None
    palabra_seleccionada = choice(palabras)
    palabra_oculta = list(reemplazar_guion_bajo(palabra_seleccionada))
    letras_usadas = []

    print(f"AHORCADO:")

    while vidas != 0 and "_" in palabra_oculta:

        # CONTROL LETRA INGRESADA
        check_letra = False
        while not check_letra:
            print(f"Descubre la palabra oculta:\n"
                  f"❤ {vidas}\n"
                  f"{''.join(palabra_oculta)}")

            if len(letras_usadas) != 0:
                print(f"Te has equivocado con las siguientes letras: {'-'.join(letras_usadas)}")

            letra = str(input("Introduzca una letra: ").upper())
            if len(letra) == 1:
                if not letra.isalpha():
                    system("cls")
                    print(f"AHORCADO:")
                    print("Solo se admiten caracteres alfabéticos.[A-Z]")
                else:
                    check_letra = True
            else:
                system("cls")
                print(f"AHORCADO:")
                print("Solo se permite un carácter por intento. ")

        if check_letra:
            if letra not in palabra_oculta and letra not in letras_usadas:
                # GENERANDO POSICIÓN DE LA LETRA
                posicion = palabra_seleccionada.find(letra)

                # BÚSQUEDA DE LETRA EN LA PALABRA OCULTA
                if posicion == -1:
                    system("cls")
                    print(f"AHORCADO:")
                    print(f"La letra no se encuentra en la palabra oculta")
                    vidas -= 1
                    # AÑADIENDO LETRA A LAS LETRAS USADAS
                    letras_usadas.append(letra)
                else:
                    system("cls")
                    print(f"AHORCADO:")
                    print(f"¡Muy bien! la letra '{letra}' hace parte de la palabra oculta.")
                    while posicion != -1:
                        # print(f"La letra '{letra}' se encuentra en la posición {posicion}.")

                        # REVELANDO PALABRA OCULTA
                        palabra_oculta[posicion] = letra

                        # RESTABLECIENDO POSICION DE BÚSQUEDA HASTA EL FINAL DE LA CADENA PARA EVITAR BUCLE INFINITO
                        posicion = palabra_seleccionada.find(letra, posicion + 1, len(palabra_seleccionada))
            else:
                system("cls")
                print(f"AHORCADO:")
                print("Ya has usado esta letra, intenta con otra.")

    else:
        system("cls")
        print("GAME OVER.")
        if vidas == 0:
            print("Has perdido. † ")
        else:
            system("cls")
            print(f"¡Felicidades!¡Has ganado!\n"
                  f"La palabra oculta era: {palabra_seleccionada}")

    new_game_option = select_option_index(["YES", "NO"], "¿Desea continuar el juego?")
    if new_game_option != 0:
        new_game = "NO"
else:
    print("Gracias por Jugar")
