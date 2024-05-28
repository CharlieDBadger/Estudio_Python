def decorar_con_saludo(funcion):
    def presentacion(nombre):
        print("Saludos")
        funcion(nombre)
        print("Hasta luego.")

    return presentacion


@decorar_con_saludo
def presentacion_hombre(nombre):
    print(f"Soy {nombre} ¿Que tal?")


def presentacion_mujer(nombre):
    print(f"Soy {nombre}, encantada de conocerlo.")


# Presentación con anotación
presentacion_hombre("Raul")

# Presentación sin anotación
presentacion_mujer("Serena")

# Presentación simulando anotación
# Almacenamos la función sin () para poder ejecutarla después desde la variable de tipo anotación.
simulacion_anotacion = decorar_con_saludo(presentacion_mujer)
simulacion_anotacion("Clara")
