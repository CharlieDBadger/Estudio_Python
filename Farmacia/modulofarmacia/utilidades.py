import os
import platform


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


def seleccion_opcion_index(menu, indicaciones):
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
                    print(f"Ingrese una opcion entre 1 y {len(menu)}.")
            except ValueError:
                limpiar_pantalla()
                print("Debes ingresar un número.")


def seleccion_opcion_match(menu, indicaciones):
    """
    :param menu: Lista, tupla o conjunto (set) que contiene las opciones del menú, no puede estar vacía.
    :param indicaciones: Mensaje que se muestra al usuario para solicitar la selección.
    :return: Devuelve la numeración de la opción seleccionada, por ejemplo, '1' para la opción '1. Opción'.
    """

    return seleccion_opcion_index(menu, indicaciones) + 1


