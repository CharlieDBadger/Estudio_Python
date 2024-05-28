from pathlib import Path
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


def generar_ruta_horizontal():
    """
    :return: Devuelve un objeto Path con la ruta donde se está ejecutando el script.
    """
    return Path(__file__).parent


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


def seleccion_categoria(ruta_relativa_horizontal):
    """
    Selecciona una carpeta/categoria dentro de una carpeta especificada por la ruta.

    :param ruta_relativa_horizontal: Objeto Path con la ruta de la carpeta principal que contiene las categorías.
    :return: La ruta completa de la categoría seleccionada, o None si no se encuentra ninguna carpeta/categoría.
    """
    # Verificar si la ruta existe y es una carpeta
    if ruta_relativa_horizontal.is_dir():
        # Obtener una lista de nombres de las carpetas dentro de la carpeta de la ruta
        carpetas = [carpeta.name for carpeta in ruta_relativa_horizontal.iterdir() if carpeta.is_dir()]
        if not list(carpetas):
            print("No se encontraron carpetas en este Directorio.")
            return None
        else:
            # Solicitar al usuario que seleccione una categoría
            categoria = carpetas[seleccion_opcion_index(carpetas, "Seleccione una categoria")]
            # Devolver la ruta completa de la categoría seleccionada
            return ruta_relativa_horizontal / categoria
    else:
        # Informar al usuario si la carpeta especificada no existe o no es válida
        print("La carpeta 'categorias' especificada no existe o no es una carpeta válida.")
        return None


def seleccion_receta(ruta_categoria):
    """
    Selecciona una receta dentro de una categoría especificada por la ruta.

    :param ruta_categoria: Objeto Path con la ruta de la carpeta que contiene las recetas en formato .txt.
    :return: La ruta completa de la receta seleccionada, o None si no se encuentra ninguna receta.
    """
    # Verificar si la ruta existe y es una carpeta
    if ruta_categoria.is_dir():
        # Obtener una lista de nombres de archivos dentro de la carpeta de la ruta
        archivos = [archivo.name for archivo in ruta_categoria.glob("*.txt") if archivo.is_file()]
        if not list(archivos):
            print("No se encontraron recetas en esta carpeta.")
            return None
        else:
            # Solicitar al usuario que seleccione una receta
            receta_seleccionada = archivos[seleccion_opcion_index(archivos, "Escoja la receta que desea ver.")]
            # Construir la ruta completa de la receta seleccionada
            ruta_receta = ruta_categoria / receta_seleccionada
            return ruta_receta
    else:
        # Informar al usuario si la carpeta especificada no existe o no es válida
        print("La carpeta especificada no existe o no es una carpeta válida.")
        return None


def leer_receta(ruta_receta):
    """
    Lee y muestra el contenido de una receta especificada por su ruta.

    :param ruta_receta: Objeto Path con la ruta del archivo de la receta que se desea leer.
    :return: None
    """
    # Abrir el archivo de la receta en modo lectura
    with open(ruta_receta, "r") as archivo:
        # Imprimir el contenido del archivo
        print(archivo.read())


def crear_receta(ruta_categoria):
    """
    Crea una nueva receta en formato '.txt' en la categoría especificada por la ruta.

    :param ruta_categoria: Objeto Path con la ruta del directorio "categoría" donde se almacenan las recetas.
    :return: None
    """
    # Solicitar al usuario el nombre del archivo de la receta
    nombre_archivo = input("Ingrese el nombre del archivo: ")

    # Obtener el nombre de la categoría desde la ruta proporcionada
    categoria = ruta_categoria.name

    # Generamos la ruta completa de la receta
    ruta_archivo = ruta_categoria / (nombre_archivo + ".txt")

    # Verificar si el archivo de la receta ya existe
    if ruta_archivo.exists():
        print(f"La receta '{nombre_archivo}' ya existe en la Categoría {categoria}.")
    else:
        # Si el archivo no existe, solicitar al usuario el contenido de la receta
        with open(ruta_archivo, "w") as archivo:
            contenido = input("Ingrese el contenido del archivo: ")
            archivo.write(contenido)
        # Informar al usuario que la receta ha sido creada exitosamente
        print(f"Receta '{nombre_archivo}' creada exitosamente en la Categoría {categoria}.")


def crear_categoria(ruta_relativa_horizontal):
    """
    Crea una nueva categoría en el directorio especificado por la ruta.

    :param ruta_relativa_horizontal: Objeto Path con la ruta del directorio donde se guardan las categorías.
    :return: None
    """
    # Solicitar al usuario el nombre de la nueva categoría
    nombre_categoria = input("Ingrese el nombre de la categoría: ")
    # Construir la ruta completa de la nueva categoría
    ruta_categoria = ruta_relativa_horizontal / nombre_categoria

    # Verificar si la categoría ya existe
    if ruta_categoria.exists():
        print(f"La categoría '{nombre_categoria}' ya existe.")
    else:
        # Si la categoría no existe, crearla
        ruta_categoria.mkdir()
        print(f"Categoría '{nombre_categoria}' creada exitosamente.")


def eliminar_receta(ruta_receta):
    """
    Elimina una receta ubicada en la ruta especificada.

    :param ruta_receta: Objeto Path con la ruta del archivo de la receta que se desea eliminar.
    :return: None
    """
    # Crear un objeto Path a partir de la ruta de la receta
    archivo_a_borrar = Path(ruta_receta)

    # Verificar si el archivo existe antes de intentar borrarlo
    if archivo_a_borrar.exists():
        # Si el archivo existe, borrarlo
        archivo_a_borrar.unlink()
        print("Archivo borrado exitosamente.")
    else:
        # Si el archivo no existe, mostrar un mensaje indicando esto
        print("El archivo no existe.")


def eliminar_categoria(ruta_categoria):
    """
    Elimina una categoría especificada, siempre y cuando esté vacía.

    :param ruta_categoria: Objeto Path con la ruta del directorio de la categoría que se desea eliminar.
    :return: None
    """
    # Crear un objeto Path a partir de la ruta de la categoría
    categoria_a_borrar = Path(ruta_categoria)

    # Verificar si el directorio existe y es un directorio
    if categoria_a_borrar.exists() and categoria_a_borrar.is_dir():
        # Obtener una lista de elementos del directorio
        elementos = list(categoria_a_borrar.iterdir())

        # Verificar si el directorio está vacío
        if len(elementos) == 0:
            # El directorio está vacío, se puede eliminar de forma segura
            categoria_a_borrar.rmdir()
            print("Directorio borrado exitosamente.")
        else:
            # El directorio contiene elementos, no se puede eliminar
            print("El directorio no está vacío. No se puede eliminar.")
    else:
        # El directorio no existe o no es un directorio válido
        print("El directorio no existe o no es un directorio válido.")


# MAIN

nombre_programa = "*** BIENVENIDO AL RECETARIO DE CHARLIE DEV ***"
menu_recetario = ["Leer Receta", "Crear Receta", "Crear Categoría", "Eliminar Receta", "Eliminar Categoría", "Salir"]
seleccion_menu = 0

ruta_principal = generar_ruta_horizontal() / 'recetas'

while seleccion_menu != len(menu_recetario):
    seleccion_menu = seleccion_opcion_match(menu_recetario, nombre_programa)

    match seleccion_menu:
        case 1:  # LEER RECETA
            leer_receta(seleccion_receta(seleccion_categoria(ruta_principal)))

        case 2:  # CREAR RECETA
            crear_receta(seleccion_categoria(ruta_principal))

        case 3:  # CREAR CATEGORÍA
            crear_categoria(ruta_principal)

        case 4:  # ELIMINAR RECETA
            eliminar_receta(seleccion_receta(seleccion_categoria(ruta_principal)))

        case 5:  # ELIMINAR CATEGORÍA
            eliminar_categoria(seleccion_categoria(ruta_principal))

        case 6:  # SALIR
            print("Recetario Cerrado\n"
                  "¡Buen provecho!")
            break
